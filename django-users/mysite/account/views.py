from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import UserRegisterForm

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

class UserLoginView(LoginView):
    template_name = 'account/login.html'

class UserLogoutView(LogoutView):
    template_name = 'account/logout.html'
