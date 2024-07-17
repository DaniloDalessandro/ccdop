from django.urls import path
from .views import (
    ColaboradorListView,
    ColaboradorCreateView,
    ColaboradorUpdateView,
    ColaboradorDeleteView
)

urlpatterns = [
    path('', ColaboradorListView.as_view(), name='colaborador_list'),
    path('novo/', ColaboradorCreateView.as_view(), name='colaborador_create'),
    path('<int:pk>/editar/', ColaboradorUpdateView.as_view(), name='colaborador_update'),
    path('<int:pk>/deletar/', ColaboradorDeleteView.as_view(), name='colaborador_delete'),
]

