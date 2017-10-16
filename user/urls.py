from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^request_reset_password/', views.request_reset_password, name='request_reset_password'),
    url(r'^reset_password/(?P<user_id>[0-9]+)/(?P<token>[\w{}.-])/', views.reset_password_form, name='reset_password_form'),
    url(r'^reset_password/', views.reset_password, name='reset_password'),
]