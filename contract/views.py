from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,CreateView, UpdateView, DeleteView,DetailView
from .models import Colaborador,CentroDeCustoGestor,CentroDeCustoSolicitante,Direcao,Gerencia,Coordenacao,Orcamento,OrcamentoExterno,LinhaOrcamentaria,Contrato,Remanejamento,Aditivo
from .forms import (ColaboradorForm,CentroDeCustoGestorForm,CentroDeCustoSolicitanteForm,DirecaoForm,
                    GerenciaForm,CoordenacaoForm,OrcamentoExternoForm,OrcamentoForm,LinhaOrcamentariaForm,ContratoForm,RemanejamentoForm,AditivoForm)
from django.urls import reverse_lazy
from .models import Contrato, Prestacao
from .forms import ContratoForm, PrestacaoForm
from django.utils import timezone
from django.views.generic import TemplateView
from .forms import DirecaoForm, GerenciaForm, CoordenacaoForm
from django.views.generic import TemplateView

#======================================================================================================================

class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'colaborador_list.html'
    context_object_name = 'colaboradores'

class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador/colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador/colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = 'colaborador/colaborador_confirm_delete.html'
    success_url = reverse_lazy('colaborador_list')

#======================================================================================================================

class CentroDeCustoGestorListView(ListView):
    model = CentroDeCustoGestor
    template_name = 'centros/centrodecustogestor_list.html'
    context_object_name = 'centros'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return CentroDeCustoGestor.objects.filter(nome__icontains=query)
        return CentroDeCustoGestor.objects.all()
    

class CentroDeCustoGestorCreateView(CreateView):
    model = CentroDeCustoGestor
    form_class = CentroDeCustoGestorForm
    template_name = 'centros/centrodecustogestor_form.html'
    success_url = reverse_lazy('centrodecustogestor_list')

class CentroDeCustoGestorUpdateView(UpdateView):
    model = CentroDeCustoGestor
    form_class = CentroDeCustoGestorForm
    template_name = 'centros/centrodecustogestor_form.html'
    success_url = reverse_lazy('centrodecustogestor_list')

class CentroDeCustoGestorDeleteView(DeleteView):
    model = CentroDeCustoGestor
    template_name = 'centros/centrodecustogestor_confirm_delete.html'
    success_url = reverse_lazy('centrodecustogestor_list')

#======================================================================================================================

class CentroDeCustoSolicitanteListView(ListView):
    model = CentroDeCustoSolicitante
    template_name = 'centros/centrodecustosolicitante_list.html'
    context_object_name = 'solicitantes'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return CentroDeCustoSolicitante.objects.filter(nome__icontains=query)
        return CentroDeCustoSolicitante.objects.all()

class CentroDeCustoSolicitanteCreateView(CreateView):
    model = CentroDeCustoSolicitante
    form_class = CentroDeCustoSolicitanteForm
    template_name = 'centros/centrodecustosolicitante_form.html'
    success_url = reverse_lazy('centrodecustosolicitante_list')

class CentroDeCustoSolicitanteUpdateView(UpdateView):
    model = CentroDeCustoSolicitante
    form_class = CentroDeCustoSolicitanteForm
    template_name = 'centros/centrodecustosolicitante_form.html'
    success_url = reverse_lazy('centrodecustosolicitante_list')

class CentroDeCustoSolicitanteDeleteView(DeleteView):
    model = CentroDeCustoSolicitante
    template_name = 'centros/centrodeustosolicitante_confirm_delete.html'
    success_url = reverse_lazy('centrodecustosolicitante_list')

#======================================================================================================================

class DirecaoListView(ListView):
    model = Direcao
    template_name = 'setores/direcao_list.html'
    context_object_name = 'direcoes'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Direcao.objects.filter(nome__icontains=query)
        return Direcao.objects.all()

class DirecaoCreateView(CreateView):
    model = Direcao
    form_class = DirecaoForm
    template_name = 'setores/direcao_form.html'
    success_url = reverse_lazy('direcao_list')

class DirecaoUpdateView(UpdateView):
    model = Direcao
    form_class = DirecaoForm
    template_name = 'setores/direcao_form.html'
    success_url = reverse_lazy('direcao_list')

class DirecaoDeleteView(DeleteView):
    model = Direcao
    template_name = 'setores/direcao_confirm_delete.html'
    success_url = reverse_lazy('direcao_list')

#======================================================================================================================

class GerenciaListView(ListView):
    model = Gerencia
    template_name = 'setores/gerencia_list.html'
    context_object_name = 'gerencias'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Gerencia.objects.filter(nome__icontains=query)
        return Gerencia.objects.all()

class GerenciaCreateView(CreateView):
    model = Gerencia
    form_class = GerenciaForm
    template_name = 'setores/gerencia_form.html'
    success_url = reverse_lazy('gerencia_list')

class GerenciaUpdateView(UpdateView):
    model = Gerencia
    form_class = GerenciaForm
    template_name = 'gerencia_form.html'
    success_url = reverse_lazy('gerencia_list')

class GerenciaDeleteView(DeleteView):
    model = Gerencia
    template_name = 'setores/gerencia_confirm_delete.html'
    success_url = reverse_lazy('gerencia_list')

#======================================================================================================================

class CoordenacaoListView(ListView):
    model = Coordenacao
    template_name = 'setores/coordenacao_list.html'
    context_object_name = 'coordenacoes'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Coordenacao.objects.filter(nome__icontains=query)
        return Coordenacao.objects.all()

class CoordenacaoCreateView(CreateView):
    model = Coordenacao
    form_class = CoordenacaoForm
    template_name = 'setores/coordenacao_form.html'
    success_url = reverse_lazy('coordenacao_list')

class CoordenacaoUpdateView(UpdateView):
    model = Coordenacao
    form_class = CoordenacaoForm
    template_name = 'setores/coordenacao_form.html'
    success_url = reverse_lazy('coordenacao_list')

class CoordenacaoDeleteView(DeleteView):
    model = Coordenacao
    template_name = 'setores/coordenacao_confirm_delete.html'
    success_url = reverse_lazy('coordenacao_list')

#======================================================================================================================

class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'colaborador/colaborador_list.html'
    context_object_name = 'colaboradores'

    def get_queryset(self):
        query = self.request.GET.get('search')

        if query:
            return Colaborador.objects.filter(nome_icontains=query)
        return Colaborador.objects.all()

class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador/colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'colaborador/colaborador_form.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = 'colaborador/colaborador_confirm_delete.html'
    success_url = reverse_lazy('colaborador_list')

class ColaboradorDetailView(DetailView):
    model = Colaborador
    template_name = 'colaborador/colaborador_detail.html'
    context_object_name = 'colaborador'

#======================================================================================================================

class OrcamentoListView(ListView):
    model = Orcamento
    template_name = 'orcamentos/orcamento_list.html'
    context_object_name = 'orcamentos'

class OrcamentoDetailView(DetailView):
    model = Orcamento
    template_name = 'orcamentos/orcamento_detail.html'
    context_object_name = 'orcamento'

class OrcamentoCreateView(CreateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'orcamentos/orcamento_form.html'
    success_url = reverse_lazy('orcamento_list')

class OrcamentoUpdateView(UpdateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'orcamentos/orcamento_form.html'
    success_url = reverse_lazy('orcamento_list')

class OrcamentoDeleteView(DeleteView):
    model = Orcamento
    template_name = 'orcamentos/orcamento_confirm_delete.html'
    success_url = reverse_lazy('orcamento_list')

#======================================================================================================================

class OrcamentoExternoListView(ListView):
    model = OrcamentoExterno
    template_name = 'orcamentos/orcamentoexterno_list.html'
    context_object_name = 'orcamentos_externos'

class OrcamentoExternoDetailView(DetailView):
    model = OrcamentoExterno
    template_name = 'orcamentos/orcamentoexterno_detail.html'
    context_object_name = 'orcamento_externo'

class OrcamentoExternoCreateView(CreateView):
    model = OrcamentoExterno
    form_class = OrcamentoExternoForm
    template_name = 'orcamentos/orcamentoexterno_form.html'
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
    template_name = 'orcamentos/orcamentoexterno_form.html'
    success_url = reverse_lazy('orcamentoexterno_list')

    def form_valid(self, form):
        orcamento_externo = form.save(commit=False)
        orcamento_externo.ano.save()
        orcamento_externo.save()
        return redirect(self.success_url)

class OrcamentoExternoDeleteView(DeleteView):
    model = OrcamentoExterno
    template_name = 'orcamentos/orcamentoexterno_confirm_delete.html'
    success_url = reverse_lazy('orcamentoexterno_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
    

#======================================================================================================================

class LinhaOrcamentariaListView(ListView):
    model = LinhaOrcamentaria
    template_name = 'linhas/linhaorcamentaria_list.html'
    context_object_name = 'linhaorcamentarias'
    paginate_by = 10

class LinhaOrcamentariaDetailView(DetailView):
    model = LinhaOrcamentaria
    template_name = 'linhas/linhaorcamentaria_detail.html'
    context_object_name = 'linhaorcamentaria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        linha = self.object
        context['valor_aprovisionado'] = linha.valor_aprovisionado
        context['valor_remanejado_total'] = linha.valor_remanejado_total
        context['saldo_orcamentario_pos_remanejamento'] = linha.saldo_orcamentario_pos_remanejamento
        context['tempo_para_contratacao'] = linha.tempo_para_contratacao
        return context

class LinhaOrcamentariaCreateView(CreateView):
    model = LinhaOrcamentaria
    form_class = LinhaOrcamentariaForm
    template_name = 'linhas/linhaorcamentaria_form.html'
    success_url = reverse_lazy('linhaorcamentaria_list')

class LinhaOrcamentariaUpdateView(UpdateView):
    model = LinhaOrcamentaria
    form_class = LinhaOrcamentariaForm
    template_name = 'linhas/linhaorcamentaria_form.html'
    success_url = reverse_lazy('linhaorcamentaria_list')

class LinhaOrcamentariaDeleteView(DeleteView):
    model = LinhaOrcamentaria
    template_name = 'linhas/linhaorcamentaria_confirm_delete.html'
    success_url = reverse_lazy('linhaorcamentaria_list')

#======================================================================================================================

class ContratoListView(ListView):
    model = Contrato
    template_name = 'contratos/contrato_list.html'
    context_object_name = 'contratos'

class ContratoCreateView(CreateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'contratos/contrato_form.html'
    success_url = reverse_lazy('contrato-list')

class ContratoUpdateView(UpdateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'contratos/contrato_form.html'
    success_url = reverse_lazy('contrato-list')

class ContratoDeleteView(DeleteView):
    model = Contrato
    template_name = 'contratos/contrato_confirm_delete.html'
    success_url = reverse_lazy('contrato-list')

class ContratoDetailView(DetailView):
    model = Contrato
    template_name = 'contratos/contrato_detail.html'
    context_object_name = 'contrato'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context

def marcar_prestacao_como_paga(request, pk):
    prestacao = get_object_or_404(Prestacao, pk=pk)
    prestacao.status_pagamento = True
    prestacao.save()
    return redirect('contratos/contrato-detail', pk=prestacao.contrato.pk)

#======================================================================================================================

class RemanejamentoListView(ListView):
    model = Remanejamento
    template_name = 'remanejamentos/remanejamento_list.html'
    context_object_name = 'remanejamentos'

class RemanejamentoDetailView(DetailView):
    model = Remanejamento
    template_name = 'remanejamentos/remanejamento_detail.html'
    context_object_name = 'remanejamento'

class RemanejamentoCreateView(CreateView):
    model = Remanejamento
    form_class = RemanejamentoForm
    template_name = 'remanejamentos/remanejamento_form.html'
    success_url = reverse_lazy('remanejamento_list')

    def form_valid(self, form):
        remanejamento = form.save(commit=False)
        remanejamento.clean()  # Validação antes de salvar
        return super().form_valid(form)

class RemanejamentoUpdateView(UpdateView):
    model = Remanejamento
    form_class = RemanejamentoForm
    template_name = 'remanejamentos/remanejamento_form.html'
    success_url = reverse_lazy('remanejamento_list')

    def form_valid(self, form):
        remanejamento = form.save(commit=False)
        remanejamento.clean()  # Validação antes de salvar
        return super().form_valid(form)

class RemanejamentoDeleteView(DeleteView):
    model = Remanejamento
    template_name = 'remanejamentos/remanejamento_confirm_delete.html'
    success_url = reverse_lazy('remanejamento_list')

#======================================================================================================================

class AditivoListView(ListView):
    model = Aditivo
    template_name = 'aditivos/aditivo_list.html'
    context_object_name = 'aditivos'

class AditivoDetailView(DetailView):
    model = Aditivo
    template_name = 'aditivos/aditivo_detail.html'
    context_object_name = 'aditivo'

class AditivoCreateView(CreateView):
    model = Aditivo
    form_class = AditivoForm
    template_name = 'aditivos/aditivo_form.html'
    success_url = reverse_lazy('aditivo_list')

class AditivoUpdateView(UpdateView):
    model = Aditivo
    form_class = AditivoForm
    template_name = 'aditivos/aditivo_form.html'
    success_url = reverse_lazy('aditivo_list')



class AditivoDeleteView(DeleteView):
    model = Aditivo
    template_name = 'aditivos/aditivo_confirm_delete.html'
    success_url = reverse_lazy('aditivo_list')

#======================================================================================================================

class SetorManageView(TemplateView):
    template_name = 'setores/setor_manage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direcoes'] = Direcao.objects.all()
        context['gerencias'] = Gerencia.objects.select_related('direcao').all()
        context['coordenacoes'] = Coordenacao.objects.select_related('gerencia').all()
        context['direcao_form'] = DirecaoForm(prefix='direcao')
        context['gerencia_form'] = GerenciaForm(prefix='gerencia')
        context['coordenacao_form'] = CoordenacaoForm(prefix='coordenacao')
        return context

    def post(self, request, *args, **kwargs):
        direcao_form = DirecaoForm(request.POST, prefix='direcao')
        gerencia_form = GerenciaForm(request.POST, prefix='gerencia')
        coordenacao_form = CoordenacaoForm(request.POST, prefix='coordenacao')

        if 'direcao' in request.POST and direcao_form.is_valid():
            direcao_form.save()
        elif 'gerencia' in request.POST and gerencia_form.is_valid():
            gerencia_form.save()
        elif 'coordenacao' in request.POST and coordenacao_form.is_valid():
            coordenacao_form.save()

        return redirect('setor_manage')




