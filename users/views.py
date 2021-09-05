from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.conf import settings
from django.core.mail import send_mail


from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
