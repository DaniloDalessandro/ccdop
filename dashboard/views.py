from django.shortcuts import render
from django.views.generic import TemplateView
from contract.models import Colaborador

class DashboardView(TemplateView):
    template_name = 'dashboard_home.html'

def colaborador_chart(request):
    colaboradores = Colaborador.objects.all()

    # Coletar dados das direções
    direcoes = [colab.direcao.nome for colab in colaboradores if colab.direcao]
    direcoes_count = {direcao: direcoes.count(direcao) for direcao in set(direcoes)}

    # Passar os dados para o template
    context = {
        'labels': list(direcoes_count.keys()),  # Nomes das direções
        'data': list(direcoes_count.values())   # Quantidade de colaboradores por direção
    }
    return render(request, 'dashboard_home.html', context)