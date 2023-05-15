from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Empresas
from .forms import EmpresaForm

# Create your views here.
@login_required
def dashboard(request):
    empresas_list = Empresas.objects.all().order_by('-created_at')
    paginator = Paginator(empresas_list, 5)
    page = request.GET.get('page')
    empresas = paginator.get_page(page)
    return render(request, 'dashboard/dashboard.html', {'empresas': empresas})

@login_required
def viewEmpresa(request, id):
    empresa = get_object_or_404(Empresas, pk=id)
    form = EmpresaForm(request.POST, instance=empresa)
    return render(request, 'dashboard/editarempresa.html', {'empresa': empresa, 'form': form})

@login_required
def editEmpresa(request, id):
    empresa = get_object_or_404(Empresas, pk=id)
    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'dashboard/editarempresa.html', {'form': form, 'empresa': empresa})

@login_required
def novaEmpresa(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.active = form.cleaned_data['active']
            empresa.save()
            return redirect('/')
        else:
            # handle invalid form data here
            return HttpResponse("Invalid form data")
    else:
        form = EmpresaForm()
        return render(request, 'dashboard/novaempresa.html', {'form': form})

@login_required
def deleteEmpresa(request, id):
    empresa = get_object_or_404(Empresas, pk=id)
    empresa.delete()
    return redirect('/')