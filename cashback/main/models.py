from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    big_image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=1000, default="Category")
    alt_tag = models.CharField(max_length=50, default="undefined")
    metatags = models.CharField(max_length=1000, default="undefined")
    created = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    readonly_fields = ('created',)

    def __str__(self):
        return str(self.id)+self.name


from user_login.models import *

class Offer(models.Model):
    company = models.ForeignKey(Company)
    description = models.CharField(max_length=1000)
    url = models.URLField()
    category = models.ForeignKey(Category)
    mailed = models.IntegerField(default=0)
    hot = models.IntegerField(default=1)
    coupon_code = models.CharField(max_length=15,null=True,blank=True)
    expired = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    readonly_fields = ('created',)

    def __str__(self):
        return str(self.id)+' '+self.description

class Click(models.Model):
    user = models.ForeignKey(Customer)
    offer = models.ForeignKey(Offer)
    created = models.DateTimeField(default=timezone.now(),null=True,blank=True,editable=True)
    readonly_fields = ('created',)

    def __str__(self):
        return str(self.id)+' '+self.user.user.username+' '+self.offer.company.name

class Transaction(models.Model):
    user = models.ForeignKey(Customer)
    offer = models.ForeignKey(Offer)
    status = models.IntegerField()
    commission = models.FloatField(null=True,blank=True)
    cashback = models.FloatField(null=True,blank=True)
    referral = models.FloatField(null=True,blank=True)
    created = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    readonly_fields = ('created',)
    def __str__(self):
        return str(self.id)+' '+str(self.user.user)+' '+str(self.offer.company.name)

class SiteData(models.Model):
    home_image1 = models.ImageField(null=True, blank=True)
    alt_tag1 = models.CharField(max_length=50, default="undefined")
    home_image2 = models.ImageField(null=True, blank=True)
    alt_tag2 = models.CharField(max_length=50, default="undefined")
    home_image3 = models.ImageField(null=True, blank=True)
    alt_tag3 = models.CharField(max_length=50, default="undefined")
    home_image4 = models.ImageField(null=True, blank=True)
    alt_tag4 = models.CharField(max_length=50, default="undefined")

class BrandAmbassador(models.Model):
    customer = models.ForeignKey(Customer)
    phone = models.CharField(max_length=15, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    fb_url = models.URLField(null=True, blank=True)
    profession = models.IntegerField(null=True, blank=True)
    why = models.CharField(max_length=1000, null=True, blank=True)
    how = models.CharField(max_length=1000, null=True, blank=True)
    interests = models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
	return str(self.customer.user)+' '+str(self.phone)

class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField( null=True, blank=True)
    phone =  models.CharField(max_length=15, null=True, blank=True)
    message = models.CharField(max_length=1000, null=True, blank=True)
