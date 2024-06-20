from django.urls import path
from .views import ColaboradorListView,ColaboradorCreateView

urlpatterns = [
    path('colaboradores/', ColaboradorListView.as_view(), name='colaborador-list'),
    path('cadastrar/', ColaboradorCreateView.as_view(), name='colaborador-create'),
]


