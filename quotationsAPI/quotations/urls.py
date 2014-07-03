from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from quotations import views

urlpatterns = patterns('',
    url(r'^authors/$', views.AuthorList.as_view(), name="author-list"),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view(), name="author-detail"),
    url(r'^quotations/$', views.QuoteList.as_view(), name="quote-list"),
    url(r'^quotations/(?P<pk>[0-9]+)/$', views.QuoteDetail.as_view(), name="quote-detail"),
    url(r'^subjects/$', views.SubjectList.as_view(), name="subject-list"),
    url(r'^subjects/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view(), name="subject-detail"),        
)

urlpatterns = format_suffix_patterns(urlpatterns)