from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class AboutPage(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactPage(View):
    def get(self, request):
        return render(request, 'contact.html')


class GalleryPage(View):
    def get(self, request):
        return render(request, 'gallery.html')


class AdminHomePage(View):
    def get(self, request):
        return render(request, 'admin_me/dashboard.html')
