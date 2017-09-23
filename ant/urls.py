# from django.conf.urls import url
from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

from django.conf.urls import url, include
from rest_framework import routers
from events import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users/(?P<userPk>[0-9]+)/events', views.EventViewSet),


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
