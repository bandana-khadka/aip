from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# It’s where we define the mapping between URLs and views.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    # The marked line maps the URL "delete_book" to the name delete_book view created in view.py file.
    url(r'^delete_book/(?P<book_id>[0-9]+)/', views.delete_book, name='delete_book'),
    
    # The marked line maps the URL "book_detail" to the name book_detail view created in view.py file.
    url(r'^book_detail/(?P<book_id>[0-9]+)/', views.book_detail, name='book_detail'),
    
    # The marked line maps the URL "add_book" to the name add_book view created in view.py file.
    url(r'^add_book/', views.add_book, name='add_book'),
    
    # The marked line maps the URL "edit_book" to the name edit_book view created in view.py file.
    url(r'^edit_book/(?P<book_id>[0-9]+)/', views.edit_book, name='edit_book'),
    
    # The marked line maps the URL "register" to the name register view created in view.py file.
    url(r'^register/', views.register, name='register'),
    
    # The marked line maps the URL "login_user" to the name login_user view created in view.py file.
    url(r'^login_user/', views.login_user, name='login_user'),
    
    # The marked line maps the URL "logout_user" to the name logout_user view created in view.py file.
    url(r'^logout_user/', views.logout_user, name='logout_user'),
    
    # The marked line maps the URL "username_exists" to the name username_exists view created in view.py file.
    url(r'^ajax/username_exists/$', views.username_exists, name='username_exists'),
    
    # The marked line maps the URL "email_exists" to the name email_exists view created in view.py file.
    url(r'^ajax/email_exists/$', views.email_exists, name='email_exists'),
    
    url(r'^books/', views.BookList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
