from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from .models import Colaborador,CentroDeCustoGestor,CentroDeCustoSolicitante,Direcao,Gerencia,Coordenacao
from .forms import ColaboradorForm,CentroDeCustoGestorForm,CentroDeCustoSolicitanteForm,DirecaoForm,GerenciaForm,CoordenacaoForm

class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'colaborador_list.html'
    context_object_name = 'colaboradores'

class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = 'colaborador_confirm_delete.html'
    success_url = reverse_lazy('colaborador_list')

class CentroDeCustoGestorListView(ListView):
    model = CentroDeCustoGestor
    template_name = 'centrodecustogestor_list.html'
    context_object_name = 'centros'

class CentroDeCustoGestorCreateView(CreateView):
    model = CentroDeCustoGestor
    form_class = CentroDeCustoGestorForm
    template_name = 'centrodecustogestor_form.html'
    success_url = reverse_lazy('centrodecustogestor_list')

class CentroDeCustoGestorUpdateView(UpdateView):
    model = CentroDeCustoGestor
    form_class = CentroDeCustoGestorForm
    template_name = 'centrodecustogestor_form.html'
    success_url = reverse_lazy('centrodecustogestor_list')

class CentroDeCustoGestorDeleteView(DeleteView):
    model = CentroDeCustoGestor
    template_name = 'centrodecustogestor_confirm_delete.html'
    success_url = reverse_lazy('centrodecustogestor_list')

class CentroDeCustoSolicitanteListView(ListView):
    model = CentroDeCustoSolicitante
    template_name = 'centrodeustosolicitante_list.html'
    context_object_name = 'solicitantes'

class CentroDeCustoSolicitanteCreateView(CreateView):
    model = CentroDeCustoSolicitante
    form_class = CentroDeCustoSolicitanteForm
    template_name = 'centrodeustosolicitante_form.html'
    success_url = reverse_lazy('centrodeustosolicitante_list')

class CentroDeCustoSolicitanteUpdateView(UpdateView):
    model = CentroDeCustoSolicitante
    form_class = CentroDeCustoSolicitanteForm
    template_name = 'centrodeustosolicitante_form.html'
    success_url = reverse_lazy('centrodeustosolicitante_list')

class CentroDeCustoSolicitanteDeleteView(DeleteView):
    model = CentroDeCustoSolicitante
    template_name = 'centrodeustosolicitante_confirm_delete.html'
    success_url = reverse_lazy('centrodeustosolicitante_list')

class DirecaoListView(ListView):
    model = Direcao
    template_name = 'direcao_list.html'
    context_object_name = 'direcoes'

class DirecaoCreateView(CreateView):
    model = Direcao
    form_class = DirecaoForm
    template_name = 'direcao_form.html'
    success_url = reverse_lazy('direcao_list')

class DirecaoUpdateView(UpdateView):
    model = Direcao
    form_class = DirecaoForm
    template_name = 'direcao_form.html'
    success_url = reverse_lazy('direcao_list')

class DirecaoDeleteView(DeleteView):
    model = Direcao
    template_name = 'direcao_confirm_delete.html'
    success_url = reverse_lazy('direcao_list')

class GerenciaListView(ListView):
    model = Gerencia
    template_name = 'gerencia_list.html'
    context_object_name = 'gerencias'

class GerenciaCreateView(CreateView):
    model = Gerencia
    form_class = GerenciaForm
    template_name = 'gerencia_form.html'
    success_url = reverse_lazy('gerencia_list')

class GerenciaUpdateView(UpdateView):
    model = Gerencia
    form_class = GerenciaForm
    template_name = 'gerencia_form.html'
    success_url = reverse_lazy('gerencia_list')

class GerenciaDeleteView(DeleteView):
    model = Gerencia
    template_name = 'gerencia_confirm_delete.html'
    success_url = reverse_lazy('gerencia_list')

class CoordenacaoListView(ListView):
    model = Coordenacao
    template_name = 'coordenacao_list.html'
    context_object_name = 'coordenacoes'

class CoordenacaoCreateView(CreateView):
    model = Coordenacao
    form_class = CoordenacaoForm
    template_name = 'coordenacao_form.html'
    success_url = reverse_lazy('coordenacao_list')

class CoordenacaoUpdateView(UpdateView):
    model = Coordenacao
    form_class = CoordenacaoForm
    template_name = 'coordenacao_form.html'
    success_url = reverse_lazy('coordenacao_list')

class CoordenacaoDeleteView(DeleteView):
    model = Coordenacao
    template_name = 'coordenacao_confirm_delete.html'
    success_url = reverse_lazy('coordenacao_list')

class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'colaborador_list.html'
    context_object_name = 'colaboradores'

class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = 'colaborador_confirm_delete.html'
    success_url = reverse_lazy('colaborador_list')