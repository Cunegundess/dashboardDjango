from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Empresas
from .forms import EmpresaForm

# Create your views here.
def dashboard(request):
    empresas = Empresas.objects.all().order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {'empresas': empresas})

def viewEmpresa(request, id):
    empresa = get_object_or_404(Empresas, pk=id)
    return render(request, 'dashboard/editarempresa.html', {'empresa': empresa})

def editEmpresa(request, id):
    empresa = get_object_or_404(Empresas, pk=id)
    form = EmpresaForm(request.POST, instance=empresa)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'dashboard/editarempresa.html', {'form': form, 'empresa': empresa})


def novaEmpresa(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.active = form.cleaned_data['active'] # add this line
            empresa.save()
            return redirect('/')
        else:
            # handle invalid form data here
            return HttpResponse("Invalid form data")
    else:
        form = EmpresaForm()
        return render(request, 'dashboard/novaempresa.html', {'form': form})

    
def deleteEmpresa(request, id):
    empresa = get_object_or_404(Empresas, pk=id)
    empresa.delete()
    return redirect('/')