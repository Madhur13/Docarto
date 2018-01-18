from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import *
from user_login.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from cashback.tasks import SendOfferEmail
from .forms import *
from django.db.models import Count,Q
from django.views.decorators.csrf import ensure_csrf_cookie



def index(request):
    categories = Category.objects.all()
    offers = Offer.objects.filter(hot=1).filter(expired=0)
    sitedata = SiteData.objects.all()
    template = loader.get_template('main/hot_offers.html')
    results = template.render({'offers':offers}, request)
    return render(request, 'main/index.html', {'categories': categories, 'results':results, 'sitedata':sitedata[0]})

def offers(request):
    company_ids = request.POST.getlist('comp_filter[]')
    category_ids = request.POST.getlist('cat_filter[]')
    if len(company_ids)==0 and len(category_ids)>=1:
        offers = Offer.objects.filter(category__id__in=category_ids)
    elif len(company_ids)==1 and len(category_ids)==0:
        offers = Offer.objects.filter(company__id__in=company_ids)
    else:
        offers = Offer.objects.filter(company__id__in=company_ids).filter(category__id__in=category_ids)

    offers.filter(expired=0)
    if request.user.is_superuser:
        return render(request, 'main/emailoffersform.html', {'offers':offers})
    else:
        return render(request, 'main/offers.html', {'offers': offers})

@ensure_csrf_cookie
def company(request,comp_name):
    #categories = Category.objects.all()
    offers = Offer.objects.filter(company__name__iexact=comp_name).filter(expired=0)
    company = get_object_or_404(Company, name__iexact=comp_name)
    comp_id = company.id
    #d=offers.values_list('category',flat=True)
    #categories = Category.objects.filter(id__in=d)
    #filters = Q(offer__company__name__iexact=comp_name)
    all_categories = Category.objects.all().extra(select = {
  "num_offers" : """
  SELECT COUNT(*)
  FROM main_offer
    JOIN user_login_company on main_offer.company_id = user_login_company.id
  WHERE main_offer.category_id = main_category.id
  AND main_offer.expired = 0
  AND main_offer.company_id = %d """ % comp_id,
})
    categories = []
    for category in all_categories:
        if category.num_offers:
            categories.append(category)
    if len(categories) <= 1:
	categories = []
    #categories = Category.objects.annotate(num_offers=Count('offer',filter=filters))
    #print(categories.query)
    template = loader.get_template('main/offers.html')
    results = template.render({'offers':offers}, request)
    return render(request,'main/offer_page.html', {'categories':categories, 'results':results, 'comp_id': comp_id, 'company':company})

@ensure_csrf_cookie
def category(request, cat_name):
    #companies = Company.objects.all()
    category = get_object_or_404(Category, name__iexact=cat_name)
    cat_id = category.id
    offers = Offer.objects.filter(category__name__iexact=cat_name).filter(expired=0)
    #d=offers.values_list('company',flat=True)
    #companies = Company.objects.filter(id__in=d)
    all_companies = Company.objects.all().extra(select = {
  "num_offers" : """
  SELECT COUNT(*)
  FROM main_offer
    JOIN main_category on main_offer.category_id = main_category.id
  WHERE main_offer.company_id = user_login_company.id
  AND main_offer.expired = 0
  AND main_offer.category_id = %d """ % cat_id,
})
    companies = []
    for company in all_companies:
        if company.num_offers:
            companies.append(company)
    if len(companies) <= 1:
	companies = []
    template = loader.get_template('main/offers.html')
    results = template.render({'offers':offers}, request)
    return render(request, 'main/offer_page.html', {'companies':companies, 'results':results, 'cat_id': cat_id, 'category':category})

@login_required
def shop(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    customer = request.user.customer;
    click = Click(user=customer, offer=offer)
    click.save()
    link = offer.url
    return HttpResponseRedirect('https://linksredirect.com/?pub_id=16923CL15205&subid='+str(click.id)+'&source=linkkit&url='+link)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def mailoffers(request):
    if(request.method=='POST'):
        offer_ids = request.POST.getlist('selected_offers[]')
        offers = Offer.objects.filter(id__in=offer_ids)
        category = offers[0].category
        template = loader.get_template('main/email_about_offers.html')
        result = template.render({'offers':offers},request)
        SendOfferEmail.delay(result, category)

    results = 'Please select a category from Filter.'
    categories = Category.objects.all()
    return render(request,'main/offer_page.html', {'categories':categories, 'results':results})

@login_required
def profile(request):
    customer = request.user.customer
    transactions = Transaction.objects.filter(user=customer)
    referrals = Customer.objects.filter(referee_code=customer.referral_code)
    categories = customer.categories.all()
    other_categories = Category.objects.exclude(pk__in=categories)
    return render(request, 'main/profile.html', {'customer': customer, 'transactions':transactions,
                                                 'referrals':referrals, 'categories':categories,
                                                 'other_categories':other_categories})

@login_required
def earningStatus(request):
    customer = request.user.customer
    transactions = Transaction.objects.filter(user=customer).select_related('offer__company')
    referrals = Transaction.objects.filter(user__referee_code=customer.referral_code).select_related('user')
    total = 0
    pending = 0
    approved = 0
    for transaction in transactions:
        if transaction.status == 1:
            total += transaction.commission
            pending += transaction.commission
        elif transaction.status == 2:
            total += transaction.commission
            approved += transaction.commission
    for referral in referrals:
        if referral.status == 1:
            total += referral.referral
            pending += referral.referral
        elif referral.status == 2:
            total += referral.referral
            approved += referral.referral
    context = {
    'customer':customer,
    'transactions': transactions,
    'referrals': referrals,
    'total': total,
    'pending': pending,
    'approved': approved
    }
    return render(request,'main/earningStatus.html',context)


@login_required
def userSettings(request):
    customer = request.user.customer
    if(request.method=='POST'):
        form=UserSettingsForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            customer.phone = phone
            customer.email = email
            customer.save()
            print('user settings updated')

    return profile(request)

# not yet integrated with UI because UI needs change. This page should be entirely different.
@login_required
def changePassword(request):
    user = request.user
    customer = user.customer
    if(request.method=='POST'):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_passwrod = form.cleaned_data['confirm_password']
            if user.check_password(old_password) and new_password==confirm_password:
                user.set_password(new_password)
                user.save()

    return profile(request)

@login_required
def addBankDetails(request):
    customer = request.user.customer
    if(request.method=='POST'):
        form = BankDetailsForm(request.POST)
        if form.is_valid():
            account_name = form.cleaned_data['account_name']
            account_no = form.cleaned_data['account_no']
            ifsc = form.cleaned_data['ifsc']
            customer.account_name = account_name
            customer.account_no = account_no
            customer.ifsc = ifsc
            customer.save()
        else:
            print('error in adding bank details')

    return earningStatus(request)

@login_required
def addPaytmDetails(request):
    customer = request.user.customer
    if(request.method=='POST'):
        form = PaytmDetailsForm(request.POST)
        if form.is_valid():
            paytm_no = form.cleaned_data['paytm_no']
            customer.paytm_no = paytm_no
            customer.save()
        else:
            print('error in adding paytm details')
    return earningStatus(request)

@login_required
def referral(request):
    customer = request.user.customer
    referrals = Customer.objects.filter(referee_code=customer.referral_code)
    sum=0
    for referral in referrals:
        sum+=referral.balance * 0.1
    return render(request,'main/referral.html',{'referral_code':customer.referral_code,'referrals':referrals, 'total_earning':sum})

@login_required
def setCategoryPrefs(request):
    customer = request.user.customer
    if(request.method=='POST'):
        customer.categories.clear()
        for category_id in request.POST.getlist('categories[]'):
            category = Category.objects.get(id=category_id)
            customer.categories.add(category)
    return profile(request)

def aboutUs(request):
    return render(request,'main/aboutUs.html')

def terms(request):
    return render(request,'main/terms.html')

@ensure_csrf_cookie
def allPortals(request):
    categories = Category.objects.all()
    companies = Company.objects.all().order_by('name')
    template = loader.get_template('main/companies_allPortals.html')
    results = template.render({ 'companies':companies })
    return render(request, 'main/allPortals.html',{'categories':categories, 'results':results })

def getPortalsByCategory(request):
    category_ids = request.POST.getlist('all_portals_filter[]')
    if len(category_ids) == 0:
        companies = Company.objects.all().order_by('name');
        return render(request,'main/companies_allPortals.html',{'companies':companies})
    offers = Offer.objects.filter(category__id__in=category_ids).filter(expired=0)
    company_ids = offers.values_list('company', flat=True)
    companies = Company.objects.filter(id__in=company_ids).order_by('name')
    return render(request,'main/companies_allPortals.html',{'companies':companies})

def advertiseWithUs(request):
    return render(request,'main/advertiseWithUs.html')

@login_required
def brandAmbassadorForm(request):
    if request.method == 'GET':
        form = BrandAmbassadorForm()
        return render(request, 'main/brandAmbassadorForm.html', {'form':form})
    elif request.method == 'POST':
        form = BrandAmbassadorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            fb_url = form.cleaned_data['fb_url']
            profession = form.cleaned_data['profession']
            why = form.cleaned_data['why']
            how = form.cleaned_data['how']
            interests = form.cleaned_data['interests']
            brand_ambass = BrandAmbassador(customer=request.user.customer,phone=phone,fb_url=fb_url,profession=profession,why=why,how=how,interests=interests)
            brand_ambass.save()
            return render(request,'main/advertiseWithUs.html', {'brandAmbassador':'success'})
        else:
            return render(request, 'main/brandAmbassadorForm.html', {'form':form})

def contactUs(request):
    if request.method == 'GET':
        form = ContactUsForm()
        return render(request, 'main/contact_us.html',{'form':form})
    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contactUs = ContactUs(name=name, email=email, phone=phone, message=message)
            contactUs.save()
            return render(request, 'main/contact_us.html', {'form':form, 'contact':"success"})
        else:
            return render(request, 'main/contact_us.html', {'form':form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def allClicks(request, clickid):
    click = Click.objects.filter(id=clickid).select_related('offer__company', 'offer__category')[0]
    return render(request, 'main/allClicks.html',{'click':click})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def sendOfferEmail(request):
    if request.method == 'POST':
        form = OfferEmailForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data['body']
            html_template = form.cleaned_data['email_template']
            subject = form.cleaned_data['subject']
            from_email = user.email
            to_email_list = ['madhur@vassarlabs.com']
            email_message = EmailMultiAlternatives(subject, body, from_email, to_email_list)
            email_message.attach_alternative(html_template, 'text/html')
            email_message.send()
            return render(request, 'main/sendOfferEmail.html',{'form':form, 'email_success':'success'})
        else:
            return render(request, 'main/sendOfferEmail.html',{'form':form})
    form = OfferEmailForm()
    return render(request, 'main/sendOfferEmail.html', {'form':form})
