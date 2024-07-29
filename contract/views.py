from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView, UpdateView, DeleteView,DetailView
from .models import Colaborador,CentroDeCustoGestor,CentroDeCustoSolicitante,Direcao,Gerencia,Coordenacao,Orcamento,OrcamentoExterno
from .forms import ColaboradorForm,CentroDeCustoGestorForm,CentroDeCustoSolicitanteForm,DirecaoForm,GerenciaForm,CoordenacaoForm,OrcamentoExternoForm,OrcamentoForm
from django.shortcuts import redirect

class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'colaborador_list.html'
    context_object_name = 'colaboradores'

class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direcoes'] = Direcao.objects.all()
        context['gerencias'] = Gerencia.objects.all()
        context['coordenacoes'] = Coordenacao.objects.all()
        return context

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direcoes'] = Direcao.objects.all()
        context['gerencias'] = Gerencia.objects.all()
        context['coordenacoes'] = Coordenacao.objects.all()
        return context

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

from django.shortcuts import get_object_or_404, redirect

class OrcamentoListView(ListView):
    model = Orcamento
    template_name = 'orcamento_list.html'
    context_object_name = 'orcamentos'

class OrcamentoDetailView(DetailView):
    model = Orcamento
    template_name = 'orcamento_detail.html'
    context_object_name = 'orcamento'

class OrcamentoCreateView(CreateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'orcamento_form.html'
    success_url = reverse_lazy('orcamento_list')

class OrcamentoUpdateView(UpdateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'orcamento_form.html'
    success_url = reverse_lazy('orcamento_list')

class OrcamentoDeleteView(DeleteView):
    model = Orcamento
    template_name = 'orcamento_confirm_delete.html'
    success_url = reverse_lazy('orcamento_list')

class OrcamentoExternoListView(ListView):
    model = OrcamentoExterno
    template_name = 'orcamentoexterno_list.html'
    context_object_name = 'orcamentos_externos'

class OrcamentoExternoDetailView(DetailView):
    model = OrcamentoExterno
    template_name = 'orcamentoexterno_detail.html'
    context_object_name = 'orcamento_externo'

class OrcamentoExternoCreateView(CreateView):
    model = OrcamentoExterno
    form_class = OrcamentoExternoForm
    template_name = 'orcamentoexterno_form.html'
    success_url = reverse_lazy('orcamentoexterno_list')

    def form_valid(self, form):
        orcamento_externo = form.save(commit=False)
        # Salva a instância do orçamento principal antes de associar o orçamento externo
        orcamento_externo.ano.save()
        orcamento_externo.save()
        return redirect(self.success_url)

class OrcamentoExternoUpdateView(UpdateView):
    model = OrcamentoExterno
    form_class = OrcamentoExternoForm
    template_name = 'orcamentoexterno_form.html'
    success_url = reverse_lazy('orcamentoexterno_list')

    def form_valid(self, form):
        orcamento_externo = form.save(commit=False)
        orcamento_externo.ano.save()
        orcamento_externo.save()
        return redirect(self.success_url)

class OrcamentoExternoDeleteView(DeleteView):
    model = OrcamentoExterno
    template_name = 'orcamentoexterno_confirm_delete.html'
    success_url = reverse_lazy('orcamentoexterno_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)