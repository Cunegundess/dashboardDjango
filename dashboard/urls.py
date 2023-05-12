from django.urls import path
from . import views

urlpatterns = [
    path('teste/', views.teste),
    path('', views.dashboard, name = 'dashboard'),
]
