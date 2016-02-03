"""ms URL Configuration

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
from mysite import views as mysite_views
from system_manage import views as system_manage_views
from basic_manage import views as basic_manage_views
from real_time import views as real_time_views
from emergence import views as emergence_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', mysite_views.test),
    url(r'^modify_password/', mysite_views.modify_password),
    url(r'^system/', mysite_views.system_manage),
    url(r'^basic/', mysite_views.basic),
    url(r'^emergence/', mysite_views.emergence),
    url(r'^index/', mysite_views.index),
    url(r'^camera/', mysite_views.camera),
    url(r'^code/', mysite_views.code),
    url(r'^mainpage/', mysite_views.mainpage),
    url(r'^form/', mysite_views.form),
    url(r'^cwd/', mysite_views.cwd),
    url(r'^$', mysite_views.login),
    url(r'^logout/', mysite_views.logout),
    url(r'^add_device/', basic_manage_views.add_device),
]
