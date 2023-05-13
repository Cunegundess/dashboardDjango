from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('viewempresa/<int:id>', views.viewEmpresa, name='viewEmpresa'),
    path('editarempresa/<int:id>', views.editEmpresa, name="editEmpresa"),
    path('deletarempresa/<int:id>', views.deleteEmpresa, name='deleteEmpresa'),
    path('novaempresa/', views.novaEmpresa, name='novaEmpresa'),
]
