"""rcfsfa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from rcfsfa import views

schema_view = get_schema_view(title='RCFSFA API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^drf-docs/', include('rest_framework_docs.urls')),
    url(r'^api/campus/', include('campus.api.urls')),
    url(r'^api/logs/', include('logs.api.urls')),
    url(r'^api/accounts/', include('accounts.api.urls')),
    url(r'^api/programs/', include('programs.api.urls'), name='programs'),
    url(r'^api/lib/', include('repertoire.api.urls'), name='repertoire'),
    url(r'^api/accommodation/', include('accommodation.api.urls'), name='accommodation'),
    url(r'^api/social/', include('social.api.urls'), name='social'),

    #   Normal View URLS
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^my-admin/$', views.AdminHomePage.as_view(), name='admin-home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^contact/$', views.ContactPage.as_view(), name='contact'),
    url(r'^gallery/$', views.GalleryPage.as_view(), name='gallery'),

    #   Django Apps URLS
    url(r'^accommodation/', include('accommodation.urls')),
    url(r'^blogs/', include('blogs.urls')),
    url(r'^repertoire/', include('repertoire.urls')),
    url(r'^reports/', include('report.urls')),
    url(r'^programmes/', include('programs.urls')),
    url(r'^accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
