from django.urls import path
from . import views

urlpatterns = [
    # URL da página inicial do dashboard
    path('', views.dashboard, name='dashboard'),
    
    # URL para visualizar uma empresa específica
    # O parâmetro <int:id> indica que o ID da empresa será passado na URL
    path('viewempresa/<int:id>', views.viewEmpresa, name='viewEmpresa'),
    
    # URL para editar uma empresa específica
    # O parâmetro <int:id> indica que o ID da empresa será passado na URL
    path('editarempresa/<int:id>', views.editEmpresa, name='editEmpresa'),
    
    # URL para excluir uma empresa específica
    # O parâmetro <int:id> indica que o ID da empresa será passado na URL
    path('deletarempresa/<int:id>', views.deleteEmpresa, name='deleteEmpresa'),
    
    # URL para criar uma nova empresa
    path('novaempresa/', views.novaEmpresa, name='novaEmpresa'),
]
