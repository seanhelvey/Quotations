from django.conf.urls import patterns, url
from frontend import views


urlpatterns = patterns('',
    url(r'^frontend/$', views.IndexView.as_view(), name="index"),    
)