from django.shortcuts import render
from django.views.generic import ListView
from .models import Gerencia
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Colaborador

class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'colaborador_list.html'
    context_object_name = 'colaboradores'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        gerencia_id = self.request.GET.get('gerencia')

        if nome:
            queryset = queryset.filter(nome_completo__icontains=nome)
        if gerencia_id:
            queryset = queryset.filter(gerencia_id=gerencia_id)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gerencias'] = Gerencia.objects.all()
        return context



class ColaboradorCreateView(CreateView):
    model = Colaborador
    template_name = 'colaborador_form.html'
    fields = ['nome_completo', 'mat', 'direcao', 'gerencia', 'coordenacao', 'ramal', 'email']
    success_url = reverse_lazy('colaborador-list')
