from django.conf.urls import url
from rest_framework.authtoken import views as rest_framework_views

from accommodation import views

urlpatterns = [
    url(r'^$', views.AccommodationHome.as_view(), name='accommodation-home'),
    url(r'^create/$', views.AccommodationCreate.as_view(), name='accommodation-create'),
]
