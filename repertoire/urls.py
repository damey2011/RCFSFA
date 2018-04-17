from django.conf.urls import url

from repertoire import views

urlpatterns = [
    url(r'^$', views.RepertoireHome.as_view(), name='repertoire-home'),
    url(r'^create/$', views.RepertoireCreate.as_view(), name='repertoire-create'),
    url(r'^(?P<pk>\d-)/$', views.RepertoireView.as_view(), name='repertoire-view'),
    url(r'^(?P<pk>\d-)/edit/$', views.RepertoireEdit.as_view(), name='repertoire-edit'),
    url(r'^(?P<pk>\d-)/delete/$', views.RepertoireDelete.as_view(), name='repertoire-delete'),
]