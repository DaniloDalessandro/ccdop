from django.urls import path

from auxilios import views
from .views import ( ColaboradorListView, ColaboradorCreateView, ColaboradorUpdateView, ColaboradorDeleteView)
from .views import ( CentroDeCustoGestorListView, CentroDeCustoGestorCreateView, CentroDeCustoGestorUpdateView, CentroDeCustoGestorDeleteView)
from .views import ( CentroDeCustoSolicitanteListView, CentroDeCustoSolicitanteCreateView, CentroDeCustoSolicitanteUpdateView, CentroDeCustoSolicitanteDeleteView)
from .views import ( DirecaoListView,DirecaoCreateView,DirecaoUpdateView,DirecaoDeleteView)
from .views import ( GerenciaListView,GerenciaCreateView,GerenciaUpdateView,GerenciaDeleteView)
from .views import CoordenacaoListView,CoordenacaoCreateView,CoordenacaoUpdateView,CoordenacaoDeleteView
from .views import ColaboradorListView, ColaboradorCreateView, ColaboradorUpdateView, ColaboradorDeleteView,ColaboradorDetailView
from .views import (
    OrcamentoListView, OrcamentoDetailView, OrcamentoCreateView, OrcamentoUpdateView, OrcamentoDeleteView,
    OrcamentoExternoListView, OrcamentoExternoDetailView, OrcamentoExternoCreateView, OrcamentoExternoUpdateView, OrcamentoExternoDeleteView,ContratoListView,
)

from .views import (
    LinhaOrcamentariaListView,
    LinhaOrcamentariaDetailView,
    LinhaOrcamentariaCreateView,
    LinhaOrcamentariaUpdateView,
    LinhaOrcamentariaDeleteView,    
)

from .views import (
    ContratoListView,
    ContratoCreateView,
    ContratoDetailView,
    ContratoUpdateView,
    ContratoDeleteView,
)

from .views import (
    RemanejamentoListView,
    RemanejamentoDetailView,
    RemanejamentoCreateView,
    RemanejamentoUpdateView,
    RemanejamentoDeleteView
)

from .views import AditivoListView, AditivoDetailView, AditivoCreateView, AditivoUpdateView, AditivoDeleteView
from .views import SetorManageView
from .views import ContratoCreateView, marcar_prestacao_como_paga

urlpatterns = [
    path('listarcolaboradores/', ColaboradorListView.as_view(), name='colaborador_list'),
    path('novocolaborador/', ColaboradorCreateView.as_view(), name='colaborador_create'),
    path('<int:pk>/editarcolaborador/', ColaboradorUpdateView.as_view(), name='colaborador_update'),
    path('<int:pk>/deletarcolaborador/', ColaboradorDeleteView.as_view(), name='colaborador_delete'),
    # ==============================================================================================
    path('centrogestor/', CentroDeCustoGestorListView.as_view(), name='centrodecustogestor_list'),
    path('novocentrodecustogestor/', CentroDeCustoGestorCreateView.as_view(), name='centrodecustogestor_create'),
    path('<int:pk>/editarcentrodecusto/', CentroDeCustoGestorUpdateView.as_view(), name='centrodecustogestor_update'),
    path('<int:pk>/deletarcentrodecusto/', CentroDeCustoGestorDeleteView.as_view(), name='centrodecustogestor_delete'),
    # ==============================================================================================
    path('centrosolicitante/', CentroDeCustoSolicitanteListView.as_view(), name='centrodecustosolicitante_list'),
    path('novosolicitante/', CentroDeCustoSolicitanteCreateView.as_view(), name='centrodecustosolicitante_create'),
    path('<int:pk>/editarsolicitante/', CentroDeCustoSolicitanteUpdateView.as_view(), name='centrodecustosolicitante_update'),
    path('<int:pk>/deletarsolicitante/', CentroDeCustoSolicitanteDeleteView.as_view(), name='centrodecustosolicitante_delete'),
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
    path('colaboradores/<int:pk>/', ColaboradorDetailView.as_view(), name='colaborador_detail'),
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

    # ==============================================================================================
    path('linhaorcamentaria/', LinhaOrcamentariaListView.as_view(), name='linhaorcamentaria_list'),
    path('linhaorcamentaria/nova/', LinhaOrcamentariaCreateView.as_view(), name='linhaorcamentaria_create'),
    path('linhaorcamentaria/<int:pk>/', LinhaOrcamentariaDetailView.as_view(), name='linhaorcamentaria_detail'),
    path('linhaorcamentaria/<int:pk>/editar/', LinhaOrcamentariaUpdateView.as_view(), name='linhaorcamentaria_update'),
    path('linhaorcamentaria/<int:pk>/deletar/', LinhaOrcamentariaDeleteView.as_view(), name='linhaorcamentaria_delete'),

    path('remanejamentos/', RemanejamentoListView.as_view(), name='remanejamento_list'),
    path('remanejamentos/<int:pk>/', RemanejamentoDetailView.as_view(), name='remanejamento_detail'),
    path('remanejamentos/novo/', RemanejamentoCreateView.as_view(), name='remanejamento_create'),
    path('remanejamentos/<int:pk>/editar/', RemanejamentoUpdateView.as_view(), name='remanejamento_update'),
    path('remanejamentos/<int:pk>/deletar/', RemanejamentoDeleteView.as_view(), name='remanejamento_delete'),

    path('aditivos/', AditivoListView.as_view(), name='aditivo_list'),
    path('aditivos/<int:pk>/', AditivoDetailView.as_view(), name='aditivo_detail'),
    path('aditivos/novo/', AditivoCreateView.as_view(), name='aditivo_create'),
    path('aditivos/<int:pk>/editar/', AditivoUpdateView.as_view(), name='aditivo_update'),
    path('aditivos/<int:pk>/excluir/', AditivoDeleteView.as_view(), name='aditivo_delete'),

    path('setores/manage/', SetorManageView.as_view(), name='setor_manage'),

    path('novo-contrato/', ContratoCreateView.as_view(), name='contrato_create'),
    path('list-contrato/', ContratoListView.as_view(), name='contrato-list'),
    path('<int:pk>/editar/', ContratoUpdateView.as_view(), name='contrato-update'),
    path('<int:pk>/deletar/', ContratoDeleteView.as_view(), name='contrato-delete'),
    path('<int:pk>/', ContratoDetailView.as_view(), name='contrato-detail'),
    path('prestacao/<int:pk>/pagar/', marcar_prestacao_como_paga, name='prestacao-pagar'),

]

