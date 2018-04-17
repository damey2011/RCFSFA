from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class TokenCreatePage(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class SignUpView(View):
    def get(self, request):
        return render(request, 'accounts/signup.html')


class SignInView(View):
    def get(self, request):
        return render(request, 'accounts/signin.html')


class AdminCreateUser(CreateView):
    queryset = User.objects.all()
    template_name = 'admin_me/manage_users/create_user.html'
    fields = ('username', 'email', 'first_name', 'last_name', 'password')
    success_url = reverse_lazy('user-create-success')


class AdminEditUser(UpdateView):
    queryset = User.objects.all()
    template_name = 'admin_me/manage_users/edit_user.html'
    fields = ('username', 'email', 'first_name', 'last_name')
    success_url = reverse_lazy('user-edit-success')


class AdminDeleteUser(DeleteView):
    queryset = User.objects.all()
    template_name = 'admin_me/manage_users/delete_confirm.html'
    success_url = reverse_lazy('user-delete-success')


class ListUsers(ListView):
    queryset = User.objects.all()
    paginate_by = 3
    context_object_name = 'users'
    template_name = 'admin_me/manage_users/all_users.html'
    model = User


class UserCreateSuccess(View):
    def get(self, request):
        return render(request, 'admin_me/manage_users/create-success.html')


class UserEditSuccess(View):
    def get(self, request):
        return render(request, 'admin_me/manage_users/edit-success.html')


class UserDeleteSuccess(View):
    def get(self, request):
        return render(request, 'admin_me/manage_users/delete_success.html')

