from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^delete_book/(?P<book_id>[0-9]+)/', views.delete_book, name='delete_book'),
    url(r'^book_detail/(?P<book_id>[0-9]+)/', views.book_detail, name='book_detail'),
    url(r'^add_book/', views.add_book, name='add_book'),
    url(r'^edit_book/(?P<book_id>[0-9]+)/', views.edit_book, name='edit_book'),
    url(r'^register/', views.register, name='register'),
    url(r'^login_user/', views.login_user, name='login_user'),
    url(r'^logout_user/', views.logout_user, name='logout_user'),
    url(r'^ajax/username_exists/$', views.username_exists, name='username_exists'),
    url(r'^ajax/email_exists/$', views.email_exists, name='email_exists'),
    url(r'^books/', views.BookList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)