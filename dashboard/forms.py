from django import forms
from .models import Empresas

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresas
        fields = ['name', 'Cnpj', 'active']

        widgets = {
            'active': forms.Select(attrs={'class': 'form-select', 'id': 'id_active'}),
        }

        labels = {
            'name': 'Empresa',
            'Cnpj': 'CNPJ',
            'active': 'Ativo',
        }

        choices = [
            ('Ativo', 'Ativo'),
            ('Inativo', 'Inativo'),
        ]

        active = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_active'}))

    def clean_Cnpj(self):
        cnpj = self.cleaned_data.get('Cnpj')
        if cnpj:
            # Remove any non-digit characters from the CNPJ string
            cnpj = ''.join(filter(str.isdigit, cnpj))
            self.cleaned_data['Cnpj'] = cnpj
        return cnpj
