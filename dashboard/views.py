from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Empresas
from .forms import EmpresaForm

@login_required
def dashboard(request):
    # Obtém todas as empresas ordenadas pela data de criação (mais recente primeiro)
    empresas_list = Empresas.objects.all().order_by('-created_at')
    
    # Paginação
    paginator = Paginator(empresas_list, 5)
    page = request.GET.get('page')
    empresas = paginator.get_page(page)
    
    # Renderiza o template 'dashboard.html' passando o objeto 'empresas'
    return render(request, 'dashboard/dashboard.html', {'empresas': empresas})

def viewEmpresa(request, id):
    # Obtém uma empresa específica com base no ID fornecido ou retorna 404 se não encontrada
    empresa = get_object_or_404(Empresas, pk=id)
    
    # Renderiza o template 'editarempresa.html' passando o objeto 'empresa'
    return render(request, 'dashboard/editarempresa.html', {'empresa': empresa})

def editEmpresa(request, id):
    # Obtém uma empresa específica com base no ID fornecido ou retorna 404 se não encontrada
    empresa = get_object_or_404(Empresas, pk=id)
    
    if request.method == "POST":
        # Se o método da requisição for POST, cria um formulário com os dados enviados
        form = EmpresaForm(request.POST, instance=empresa)
        
        if form.is_valid():
            # Se o formulário for válido, salva os dados da empresa no banco de dados
            form.save()
            return redirect('/')
    else:
        # Se o método da requisição for GET, cria um formulário com os dados da empresa existente
        form = EmpresaForm(instance=empresa)
    
    # Renderiza o template 'editarempresa.html' passando o formulário e a empresa
    return render(request, 'dashboard/editarempresa.html', {'form': form, 'empresa': empresa})

def novaEmpresa(request):
    if request.method == "POST":
        # Se o método da requisição for POST, cria um formulário com os dados enviados
        form = EmpresaForm(request.POST)
        
        if form.is_valid():
            # Se o formulário for válido, salva uma nova empresa no banco de dados
            empresa = form.save(commit=False)
            empresa.active = form.cleaned_data['active']
            empresa.save()
            return redirect('/')
        else:
            # Manipula dados inválidos do formulário aqui
            return HttpResponse("Invalid form data")
    else:
        # Se o método da requisição for GET, cria um formulário vazio
        form = EmpresaForm()
        return render(request, 'dashboard/novaempresa.html', {'form': form})

def deleteEmpresa(request, id):
    # Obtém uma empresa específica com base no ID fornecido ou retorna 404 se não encontrada
    empresa = get_object_or_404(Empresas, pk=id)
    
    # Exclui a empresa do banco de dados
    empresa.delete()
    
    return redirect('/')
