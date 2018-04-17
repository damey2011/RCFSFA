from django.shortcuts import render

# Create your views here.
from django.views import View


class ReportHome(View):
    def get(self, request):
        return render(request, 'reports/index.html')


class ReportCreate(View):
    def get(self, request):
        return render(request, 'reports/create.html')
