from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import AuxilioColaborador,Orcamento
from .forms import AuxilioColaboradorForm
from django.db.models import Sum
from datetime import date
from auxilios import models

class AuxilioColaboradorListView(ListView):
    model = AuxilioColaborador
    template_name = 'auxiliocolaborador_list.html'
    context_object_name = 'auxilios_colaboradores'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        orcamento_id = self.request.GET.get('orcamento_id')

        # Filtro por orcamento_id, se fornecido
        if orcamento_id:
            queryset = queryset.filter(orcamento_id=orcamento_id)
        
        # Atualiza o campo status baseado nas datas mes_inicio e mes_fim
        hoje = date.today()
        for auxilio in queryset:
            if hoje < auxilio.mes_inicio:
                auxilio.status = 'aguardando'
            elif auxilio.mes_inicio <= hoje <= auxilio.mes_fim:
                auxilio.status = 'ativo'
            else:
                auxilio.status = 'finalizado'
            auxilio.save(update_fields=['status'])
        
        return queryset.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_auxilios = self.get_queryset().aggregate(total=Sum('valor_total'))['total'] or 0
        context['valor_total_auxilios'] = total_auxilios
        context['orcamentos'] = Orcamento.objects.all()
        return context
class AuxilioColaboradorDetailView(DetailView):
    model = AuxilioColaborador
    template_name = 'auxiliocolaborador_detail.html'
    context_object_name = 'auxilio_colaborador'

class AuxilioColaboradorCreateView(CreateView):
    model = AuxilioColaborador
    form_class = AuxilioColaboradorForm
    template_name = 'auxiliocolaborador_form.html'
    success_url = reverse_lazy('auxiliocolaborador_list')

class AuxilioColaboradorUpdateView(UpdateView):
    model = AuxilioColaborador
    form_class = AuxilioColaboradorForm
    template_name = 'auxiliocolaborador_form.html'
    success_url = reverse_lazy('auxiliocolaborador_list')

class AuxilioColaboradorDeleteView(DeleteView):
    model = AuxilioColaborador
    template_name = 'auxiliocolaborador_confirm_delete.html'
    success_url = reverse_lazy('auxiliocolaborador_list')
