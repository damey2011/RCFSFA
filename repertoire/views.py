from django.shortcuts import render

# Create your views here.
from django.views import View


class RepertoireHome(View):
    def get(self, request):
        pass


class RepertoireCreate(View):
    def get(self, request):
        pass


class RepertoireView(View):
    def get(self, request, pk):
        pass


class RepertoireEdit(View):
    def get(self, request, pk):
        pass


class RepertoireDelete(View):
    def get(self, request, pk):
        pass
