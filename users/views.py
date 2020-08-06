from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin


class RegisterView(SuccessMessageMixin, FormView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = '/'
    success_message = 'Your account has been created.'

    def form_valid(self, form):
        form.instance.is_active = False
        form.save()
        return super().form_valid(form)