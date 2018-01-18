from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^offers', views.offers, name='offers'),
    url(r'^company/(?P<comp_name>[ A-Za-z0-9_@./#&+\'%:]+)$',views.company, name='company'),
    url(r'^category/(?P<cat_name>[ A-Za-z0-9_@./#&+\'%:]+)$',views.category, name='category'),
    url(r'^shop/(?P<offer_id>[0-9]+)$', views.shop, name='shop'),
    url(r'^mailoffers', views.mailoffers, name='mailoffers'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^addBankDetails$', views.addBankDetails, name='addBankDetails'),
    url(r'^addPaytmDetails$', views.addPaytmDetails, name='addPaytmDetails'),
    url(r'^setCategoryPrefs$', views.setCategoryPrefs, name='setCategoryPrefs'),
    url(r'^aboutUs$', views.aboutUs, name='aboutUs'),
    url(r'^terms$', views.terms, name="terms"),
    url(r'^userSettings$', views.userSettings, name='userSettings'),
    url(r'^earningStatus$', views.earningStatus, name='earningStatus'),
    url(r'^referral$', views.referral, name='referral'),
    url(r'^allPortals$', views.allPortals, name='allPortals'),
    url(r'^getPortalsByCategory$', views.getPortalsByCategory, name='getPortalsByCategory'),
    url(r'^advertiseWithUs$', views.advertiseWithUs, name='advertiseWithUs'),
    url(r'^brandAmbassadorForm$', views.brandAmbassadorForm, name='brandAmbassadorForm'),
    url(r'^contactUs$', views.contactUs, name="contactUs"),
    url(r'^clickRecord/(?P<clickid>[0-9]+)$', views.allClicks, name="clickRecord"),
]
