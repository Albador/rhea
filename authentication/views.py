from authtools.forms import CaseInsensitiveUsernameFieldCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class SignupView(CreateView):
    template_name = "registration\\signup.html"
    form_class = CaseInsensitiveUsernameFieldCreationForm
    success_url = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration\\profile.html"
