from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Consulta
from .forms import ConsultaForm

def listar_medico(request):
    medicos = Medico.objects.all()
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos})

def detalhes_consulta(request, pk):
    consulta = Consulta.objects.get(pk=pk)
    return render(request, 'clinica/base.html', {'consulta': consulta})

def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = ConsultaForm()
    return render(request, 'clinica/form_consulta.html', {'form': form})