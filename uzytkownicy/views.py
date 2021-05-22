from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import Rejestracja, LoginForm

class UserRejestracjaView(generic.CreateView):
    form_class = Rejestracja
    template_name = 'registration/rejestracja.html'
    success_url = reverse_lazy('login')


class LoginView(generic.CreateView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('login')
