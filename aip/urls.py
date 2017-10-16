"""aip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('book.urls')),
    url(r'^admin/', admin.site.urls),
    
    # The marked line maps the URL "book" to the name book view created in view.py file.
    url(r'^book/', include('book.urls', namespace='book')),
    
    # The marked line maps the URL "user" to the name user view created in view.py file.
    url(r'^user/', include('user.urls', namespace='user')),
    
    # The marked line maps the URL "rest_framework" to the name rest_framework view created in view.py file.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

