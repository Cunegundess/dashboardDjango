from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Empresas

# Create your views here.
def dashboard(request):
    empresas = Empresas.objects.all()
    return render(request, 'dashboard/dashboard.html', {'empresas': empresas})

def dadosEmpresa(request, id):
    empresa = get_object_or_404(Empresas, pk=id)
    return render(request, 'dashboard/empresa.html', {'empresa': empresa})