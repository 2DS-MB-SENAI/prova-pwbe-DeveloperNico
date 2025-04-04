from django.shortcuts import render, redirect
from .models import Medico, Consulta
from .forms import ConsultaForm, PesquisaEspecialidade

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

def pesquisa_especialidade(request):
    form = PesquisaEspecialidade(request.GET)
    medicos = Medico.objects.all()

    if form.is_valid():
        especialidade = form.cleaned_data.get('especialidade')
        medico = form.cleaned_data.get('medico')

        if especialidade:
            medicos = medicos.filter(especialidade=especialidade)
        if medico:
            medicos = medicos.filter(medico=medico)
    
    return render(request, 'clinica/pesquisa_especialidade.html', {'form': form, 'medicos': medicos})