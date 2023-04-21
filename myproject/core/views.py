from django.contrib.auth.views import  LoginView
from django.urls import reverse_lazy

from .forms import LoginForm


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'core/login.html'
    next_page = reverse_lazy('post:index')
    extra_context = {'header': 'Login'}

