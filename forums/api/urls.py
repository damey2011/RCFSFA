from django.conf.urls import url
from forums.api import views

urlpatterns=[
    url(r'^threads$', views.ThreadListCreateAPI.as_view())
]