from django.shortcuts import render
from django.views.generic import ListView
from .models import Gerencia
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,CreateView, UpdateView, DeleteView
from .models import Colaborador,LinhaOrcamentaria

class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'colaborador_list.html'
    context_object_name = 'colaboradores'
    fields = ['nome_completo', 'mat', 'direcao', 'gerencia', 'coordenacao', 'ramal', 'email']

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

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    template_name = 'colaborador_form.html'
    fields = ['nome_completo', 'mat', 'direcao', 'gerencia', 'coordenacao', 'ramal', 'email']
    success_url = reverse_lazy('colaborador-list')

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = 'colaborador_confirm_delete.html'
    success_url = reverse_lazy('colaborador-list')

class LinhaOrcamentariaCreateView(CreateView):
    model = LinhaOrcamentaria
    template_name = 'linhaorcamentaria_form.html'
    fields = [
        'classe', 'custo_despesa', 'centro_custo_gestor', 'centro_custo_solicitante',
        'descricao_resumida', 'classificacao_orcamento', 'possivel_fiscal', 
        'ano_orcamento', 'tipo_contrato', 'tipo_provavel_contratacao', 'valor_orcado',
        'status_elaboracao_tr', 'necessidade_contratacao', 'status_processo', 
        'status_contratacao', 'obs_contrato'
    ]
    success_url = reverse_lazy('linhaorcamentaria-list')
