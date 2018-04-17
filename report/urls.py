from django.conf.urls import url

from report import views

urlpatterns = [
    url(r'^$', views.ReportHome.as_view(), name='report-home'),
    url(r'^create/$', views.ReportCreate.as_view(), name='report-create'),
]
