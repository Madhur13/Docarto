from django.db import models
from django.contrib.auth.models import User
from main.models import Category
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True,blank=True)
    big_image = models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=1000, default="Company")
    page_description = models.CharField(max_length=1000, default="undefined")
    alt_tag = models.CharField(max_length=50, default="undefined")
    metatags = models.CharField(max_length=1000, default="undefined")
    created = models.DateTimeField(default=timezone.now(),null=True, blank=True)
    readonly_fields = ('created',)

    def __str__(self):
        return str(self.id)+' '+str(self.name)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.CharField(max_length=10,null=True, blank=True)
    categories = models.ManyToManyField(Category)
    balance = models.FloatField()
    referral_code = models.CharField(max_length=15,null=True, blank=True)
    referee_code = models.CharField(max_length=15,null=True, blank=True)
    account_name = models.CharField(max_length=100,null=True, blank=True)
    account_no =  models.CharField(max_length=50,null=True, blank=True)
    ifsc = models.CharField(max_length=15,null=True, blank=True)
    paytm_name = models.CharField(max_length=100,null=True, blank=True)
    paytm_no = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now(),null=True, blank=True)
    readonly_fields = ('created',)

    def __str__(self):
        return str(self.id)+' '+str(self.user.username)
