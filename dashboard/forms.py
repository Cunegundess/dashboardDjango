from django import forms
from .models import Empresas

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresas
        fields = ('name', 'Cnpj')