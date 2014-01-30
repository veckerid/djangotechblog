from techblog.apps.accounts import views
from django.conf.urls import patterns, url, include


urlpatterns = patterns('',

    url(r'^login/$', views.login, name="login" ),
    url(r'^logout/$', views.logout, name="logout" ),
)
