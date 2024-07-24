from django.urls import path
from .views import (
    AuxilioColaboradorListView,
    AuxilioColaboradorDetailView,
    AuxilioColaboradorCreateView,
    AuxilioColaboradorUpdateView,
    AuxilioColaboradorDeleteView
)

urlpatterns = [
    path('', AuxilioColaboradorListView.as_view(), name='auxiliocolaborador_list'),
    path('<int:pk>/', AuxilioColaboradorDetailView.as_view(), name='auxiliocolaborador_detail'),
    path('create/', AuxilioColaboradorCreateView.as_view(), name='auxiliocolaborador_create'),
    path('<int:pk>/update/', AuxilioColaboradorUpdateView.as_view(), name='auxiliocolaborador_update'),
    path('<int:pk>/delete/', AuxilioColaboradorDeleteView.as_view(), name='auxiliocolaborador_delete'),
]
