"""microblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from account.views import register, login
from app.views import main, up, follow, comment, home, hot, unfollow, delete, search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', register),
    url(r'^main/$', main),
    url(r'^login/', login),
    url(r'^main/(?P<CID>\d+)/$', up, name='up_link'),
    url(r'^(?P<favor>\w+)/favor/$',follow,name = 'follow_link'),
    url(r'^main/(?P<CID>\d+)/comment/$', comment, name='comment_link'),
    url(r'^(?P<uid>\d+)/home', home, name='home'),
    url(r'^hot/', hot, name='hot'),
    url(r'^(?P<favor>\w+)/un favor/$', unfollow, name='unfollow_link'),
    url(r'^(?P<CID>\d+)/delete/$', delete, name='delete_link'),
    url(r'^search', search,name='search')
]
