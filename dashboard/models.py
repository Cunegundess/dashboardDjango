from django.db import models
from django.core.validators import RegexValidator

# Criando um modelo Empresas.
class Empresas(models.Model):

    # Definindo uma tupla de escolhas para o campo 'active'
    STATUS = (
        ('Inativo', 'Inativo'),
        ('Ativo', 'Ativo'),
    )

    # Definindo os campos da tabela 'empresas'
    name = models.CharField(max_length=300)
    Cnpj = models.TextField()
    active = models.CharField(
        max_length=8,
        choices=STATUS,
        default='Inativo'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Definindo o nome da empresa como o titulo no Admin
    def __str__(self):
        return self.name
