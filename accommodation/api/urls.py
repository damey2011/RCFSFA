from django.conf.urls import url

from accommodation.api import views

urlpatterns = [
    url(r'^$', views.ListCreateAccommodation.as_view(), name='list-create-acc'),
    # url(r'^(?P<pk>\d+)$', views.RetrieveUpdateDestroyAccommodation.as_view(), name='ret-update-del-acc')
]
