from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import AuxilioColaborador,Orcamento
from .forms import AuxilioColaboradorForm
from django.db.models import Sum

class AuxilioColaboradorListView(ListView):
    model = AuxilioColaborador
    template_name = 'auxiliocolaborador_list.html'
    context_object_name = 'auxilios_colaboradores'

    def get_queryset(self):
        queryset = super().get_queryset()
        orcamento_id = self.request.GET.get('orcamento_id')
        
        if orcamento_id:
            queryset = queryset.filter(orcamento_id=orcamento_id)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calcular o valor total dos auxílios
        total_auxilios = self.get_queryset().aggregate(total=Sum('valor_total'))['total'] or 0
        context['valor_total_auxilios'] = total_auxilios

        # Passar os orçamentos para os filtros
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
