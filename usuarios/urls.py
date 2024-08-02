from django.urls import path, include
from .views import UsuarioRegisterView

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('register/', UsuarioRegisterView.as_view(), name='register'),
]
