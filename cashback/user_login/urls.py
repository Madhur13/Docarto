from django.conf.urls import url
from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm,password_reset_complete
from . import views

urlpatterns = [
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^user/password/reset/$', password_reset, {'template_name':'user_login/pass_reset_form.html','subject_template_name':'user_login/password_reset_subject.txt'}, name='pass_reset'),
    url(r'^user/password/reset/done$', password_reset_done, {'template_name':'user_login/pass_reset_done.html'}, name='password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name':'user_login/pass_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^user/password/done/$', password_reset_complete, {'template_name':'user_login/pass_reset_complete.html'}, name='password_reset_complete'),
]
#below is the definition of password_reset, these arguments can be passed to the function if needed
#password_reset(request, template_name='registration/password_reset_form.html',
# email_template_name='registration/password_reset_email.html', subject_template_name='registration/password_reset_subject.txt',
# password_reset_form=PasswordResetForm, token_generator=default_token_generator, post_reset_redirect=None, from_email=None,
#  current_app=None, extra_context=None, html_email_template_name=None, extra_email_context=None)
