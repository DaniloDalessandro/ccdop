from django.urls import path
from .views import ( ColaboradorListView, ColaboradorCreateView, ColaboradorUpdateView, ColaboradorDeleteView)
from .views import ( CentroDeCustoGestorListView, CentroDeCustoGestorCreateView, CentroDeCustoGestorUpdateView, CentroDeCustoGestorDeleteView)
from .views import ( CentroDeCustoSolicitanteListView, CentroDeCustoSolicitanteCreateView, CentroDeCustoSolicitanteUpdateView, CentroDeCustoSolicitanteDeleteView)
from .views import ( DirecaoListView,DirecaoCreateView,DirecaoUpdateView,DirecaoDeleteView)
from .views import ( GerenciaListView,GerenciaCreateView,GerenciaUpdateView,GerenciaDeleteView)
from .views import CoordenacaoListView,CoordenacaoCreateView,CoordenacaoUpdateView,CoordenacaoDeleteView
from .views import ColaboradorListView, ColaboradorCreateView, ColaboradorUpdateView, ColaboradorDeleteView
from .views import (
    OrcamentoListView, OrcamentoDetailView, OrcamentoCreateView, OrcamentoUpdateView, OrcamentoDeleteView,
    OrcamentoExternoListView, OrcamentoExternoDetailView, OrcamentoExternoCreateView, OrcamentoExternoUpdateView, OrcamentoExternoDeleteView
)



urlpatterns = [
    path('listarcolaboradores/', ColaboradorListView.as_view(), name='colaborador_list'),
    path('novocolaborador/', ColaboradorCreateView.as_view(), name='colaborador_create'),
    path('<int:pk>/editarcolaborador/', ColaboradorUpdateView.as_view(), name='colaborador_update'),
    path('<int:pk>/deletarcolaborador/', ColaboradorDeleteView.as_view(), name='colaborador_delete'),
    # ==============================================================================================
    path('listarcentrosdecusto/', CentroDeCustoGestorListView.as_view(), name='centrodecustogestor_list'),
    path('novocentrodecusto/', CentroDeCustoGestorCreateView.as_view(), name='centrodecustogestor_create'),
    path('<int:pk>/editarcentrodecusto/', CentroDeCustoGestorUpdateView.as_view(), name='centrodecustogestor_update'),
    path('<int:pk>/deletarcentrodecusto/', CentroDeCustoGestorDeleteView.as_view(), name='centrodecustogestor_delete'),
    # ==============================================================================================
    path('listarcentrossolicitantes/', CentroDeCustoSolicitanteListView.as_view(), name='centrodeustosolicitante_list'),
    path('novosolicitante/', CentroDeCustoSolicitanteCreateView.as_view(), name='centrodeustosolicitante_create'),
    path('<int:pk>/editarsolicitante/', CentroDeCustoSolicitanteUpdateView.as_view(), name='centrodeustosolicitante_update'),
    path('<int:pk>/deletarsolicitante/', CentroDeCustoSolicitanteDeleteView.as_view(), name='centrodeustosolicitante_delete'),
    # ==============================================================================================
    path('listardirecoes/', DirecaoListView.as_view(), name='direcao_list'),
    path('novadirecao/', DirecaoCreateView.as_view(), name='direcao_create'),
    path('<int:pk>/editardirecao/', DirecaoUpdateView.as_view(), name='direcao_update'),
    path('<int:pk>/deletardirecao/', DirecaoDeleteView.as_view(), name='direcao_delete'),
    # ==============================================================================================
    path('listargerencias/', GerenciaListView.as_view(), name='gerencia_list'),
    path('novagerencia/', GerenciaCreateView.as_view(), name='gerencia_create'),
    path('<int:pk>/editargerencia/', GerenciaUpdateView.as_view(), name='gerencia_update'),
    path('<int:pk>/deletargerencia/', GerenciaDeleteView.as_view(), name='gerencia_delete'),
    # ==============================================================================================
    path('listarcoordenacoes/', CoordenacaoListView.as_view(), name='coordenacao_list'),
    path('novacoordenacao/', CoordenacaoCreateView.as_view(), name='coordenacao_create'),
    path('<int:pk>/editarcoordenacao/', CoordenacaoUpdateView.as_view(), name='coordenacao_update'),
    path('<int:pk>/deletarcoordenacao/', CoordenacaoDeleteView.as_view(), name='coordenacao_delete'),
    # ==============================================================================================
    path('colaboradores/', ColaboradorListView.as_view(), name='colaborador_list'),
    path('colaboradores/novo/', ColaboradorCreateView.as_view(), name='colaborador_create'),
    path('colaboradores/<int:pk>/editar/', ColaboradorUpdateView.as_view(), name='colaborador_update'),
    path('colaboradores/<int:pk>/deletar/', ColaboradorDeleteView.as_view(), name='colaborador_delete'),
    # ==============================================================================================
  
    path('orcamentos/', OrcamentoListView.as_view(), name='orcamento_list'),
    path('orcamentos/<int:pk>/', OrcamentoDetailView.as_view(), name='orcamento_detail'),
    path('orcamentos/create/', OrcamentoCreateView.as_view(), name='orcamento_create'),
    path('orcamentos/<int:pk>/update/', OrcamentoUpdateView.as_view(), name='orcamento_update'),
    path('orcamentos/<int:pk>/delete/', OrcamentoDeleteView.as_view(), name='orcamento_delete'),

    # ==============================================================================================
    path('orcamentos_externos/', OrcamentoExternoListView.as_view(), name='orcamentoexterno_list'),
    path('orcamentos_externos/<int:pk>/', OrcamentoExternoDetailView.as_view(), name='orcamentoexterno_detail'),
    path('orcamentos_externos/create/', OrcamentoExternoCreateView.as_view(), name='orcamentoexterno_create'),
    path('orcamentos_externos/<int:pk>/update/', OrcamentoExternoUpdateView.as_view(), name='orcamentoexterno_update'),
    path('orcamentos_externos/<int:pk>/delete/', OrcamentoExternoDeleteView.as_view(), name='orcamentoexterno_delete'),

  

    

]

