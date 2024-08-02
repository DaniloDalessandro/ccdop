from django.urls import reverse_lazy
from django.views import generic
from .forms import UsuarioCreationForm

class UsuarioRegisterView(generic.CreateView):
    form_class = UsuarioCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'usuarios/register.html'
