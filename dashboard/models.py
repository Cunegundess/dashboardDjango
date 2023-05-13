from django.db import models

# Create your models here.
class Empresas(models.Model):

    STATUS = (
        ('Não', 'Inativo'),
        ('Sim', 'Ativo'),
    )

    name = models.CharField(max_length=300)
    Cnpj = models.TextField()
    active = models.CharField(
        max_length=8,
        choices=  STATUS, 
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name