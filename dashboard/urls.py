from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('empresa/<int:id>', views.dadosEmpresa, name='dadosEmpresa')
]
