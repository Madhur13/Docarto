from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from .forms import *
from django.template import loader, Context
from django.contrib.auth.models import User
from .models import *
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from cashback.tasks import SignupTask,mul

def login_view(request):
    next_page = request.GET.get('next',reverse('index'))
    if request.method == 'GET':
        return render(request, 'user_login/form-login.html',{'next':next_page})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(next_page)
                else:
                    return render(request,'user_login/form-login.html',{'message':'Disabled user','next':next_page})
            else:
                return render(request,'user_login/form-login.html',{'message':'Invalid Username or Password','next':next_page})
        else:
            return render(request,'user_login/form-login.html',{'message':'Invalid Username or Password','next':next_page})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def signup(request):
    if request.method == 'GET':
        form  = SignupForm()
        return render(request, 'user_login/form-signup.html', {'form':form} )
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = username
            #phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            #firstname = form.cleaned_data['firstname']
            #lastname = form.cleaned_data['lastname']
            referral = form.cleaned_data['referral']
            if User.objects.filter(username=username):
                return render(request, 'user_login/form-signup.html', {'form':form, 'message':'Email already registered'})
            if referral and not Customer.objects.filter(referral_code__iexact=referral):
                return render(request, 'user_login/form-signup.html', {'form':form,'message':'Invalid Referral Code'})
            user = User.objects.create_user(username,email,password)
            customer = Customer(user=user, balance=0, referral_code='REFER'+str(user.id))
            if referral:
                customer.referee_code=referral
            customer.save()
	    html_message=loader.render_to_string('user_login/welcome.html')
	    msg = MIMEMultipart('alternative')
	    msg['Subject'] = "Welcome to Docarto"
	    msg['From'] = "madhurmadhur@docarto.com"
	    msg['To'] = email
	    html_message = MIMEText(html_message, "html")
	    msg.attach(html_message)
            try:
		s = smtplib.SMTP('localhost')
                #s = smtplib.SMTP('mail.docarto.com')
                s.login('madhurmadhur@docarto.com', 'madhur123')
                s.sendmail('madhurmadhur@docarto.com', email, msg.as_string())
                s.quit()
            except smtplib.SMTPException:
                print "Error:", sys.exc_info()[0]
	    #html_content=loader.get_template('user_login/welcome.html').render(Context())
	    #send_mail('Welcome', "hhhhhhhh", settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER, email], fail_silently=False,html_message=html_message)
            #SignupTask.delay(user.email)
            #mul.delay(2,5)
            #return HttpResponseRedirect(reverse('login'))
	    return render(request,'user_login/form-login.html',{'emailSentModal':'success'})
        else:
            return render(request, 'user_login/form-signup.html', {'form':form} )
