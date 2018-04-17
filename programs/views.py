from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from programs.forms import ProgrammeForm
from programs.models import Programme


class AllProgramHome(ListView):
    queryset = Programme.objects.all()
    paginate_by = 3
    context_object_name = 'programmes'
    template_name = 'admin_me/programs/all_programs.html'
    model = Programme


class ProgramCreate(View):
    def get(self, request):
        form = ProgrammeForm
        return render(request, 'admin_me/programs/create-program.html', locals())

    def post(self, request):
        form = ProgrammeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('list-programs'))
        else:
            return render(request, 'admin_me/programs/create-program.html', locals())


class ProgramView(View):
    def get(self, request, pk):
        p = Programme.objects.get(pk=pk)
        return render(request,'programs/single.html', locals())


class ProgramEdit(View):
    def get(self, request, pk):
        pass


class ProgramDelete(View):
    def get(self, request, pk):
        pass
