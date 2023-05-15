from django import forms
from .models import Empresas

class EmpresaForm(forms.ModelForm):
    # Define o formulário para o modelo Empresas

    class Meta:
        model = Empresas
        fields = ['name', 'Cnpj', 'active']

        widgets = {
            'active': forms.Select(attrs={'class': 'form-select', 'id': 'id_active'}),
            # Define o widget personalizado para o campo 'active' como um <select>
            # com classe CSS 'form-select' e ID 'id_active'
        }

        labels = {
            'name': 'Empresa',
            'Cnpj': 'CNPJ',
            'active': 'Ativo',
            # Define rótulos personalizados para os campos 'name', 'Cnpj' e 'active'
        }

        choices = [
            ('Ativo', 'Ativo'),
            ('Inativo', 'Inativo'),
        ]

        active = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_active'}))
        # Define um campo 'active' personalizado como um ChoiceField com as opções
        # "Ativo" e "Inativo". O widget Select é utilizado para exibir as opções
        # na interface do formulário.