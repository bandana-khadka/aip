from django.conf.urls import url
from . import views
from .forms import BookUpdateForm

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<book_id>[0-9]+)/', views.detail, name='detail'),
    url(r'^delete_book/(?P<book_id>[0-9]+)/', views.delete_book, name='delete_book'),
    url(r'^book_detail/(?P<book_id>[0-9]+)/', views.book_detail, name='book_detail'),
    url(r'^add_book/', views.add_book, name='add_book'),
    url(r'^edit_book/(?P<book_id>[0-9]+)/', views.edit_book, name='edit_book'),
    url(r'^edit_book/', views.edit_book, name='edit_book'),
    url(r'^register/', views.register, name='register'),
    url(r'^login_user/', views.login_user, name='login_user'),
    url(r'^logout_user/', views.logout_user, name='logout_user'),
]