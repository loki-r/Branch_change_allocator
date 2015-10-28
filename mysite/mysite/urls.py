"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from branch.views import formdisplay, register, user_login, user_logout

from django.conf.urls import patterns
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^hello$', views.hello, name='hello'),
    url(r'^time$', views.current_datetime, name='current_datetime'),
    url(r'^form$', formdisplay, name='formdisplay'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register$', register, name='register'),
    url(r'^login$', user_login, name='user_login'),
    url(r'^logout$', user_logout, name='user_logout'),
    url(r'^branch/', include('branch.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
