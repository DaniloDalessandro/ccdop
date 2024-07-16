from django.urls import path
from .views import ColaboradorListView, ColaboradorCreateView, ColaboradorUpdateView, ColaboradorDeleteView,LinhaOrcamentariaCreateView

urlpatterns = [
    path('colaboradores/', ColaboradorListView.as_view(), name='colaborador-list'),
    path('cadastrar/', ColaboradorCreateView.as_view(), name='colaborador-create'),
    path('colaboradores/', ColaboradorListView.as_view(), name='colaborador-list'),
    path('editar/<int:pk>/', ColaboradorUpdateView.as_view(), name='colaborador-update'),
    path('deletar/<int:pk>/', ColaboradorDeleteView.as_view(), name='colaborador-delete'),
    path('linhaorcamentaria/nova/', LinhaOrcamentariaCreateView.as_view(), name='linhaorcamentaria-create'),
]


