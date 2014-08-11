from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from quotations import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^', include('frontend.urls')),        
    url(r'^', include('quotations.urls')),    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)