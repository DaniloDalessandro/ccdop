from django.urls import path
from . import views
from .views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(),name='dashboard'),

    path('colaboradores/chart/', views.colaborador_chart, name='colaborador_chart'),
]