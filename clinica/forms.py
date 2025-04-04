from django import forms
from .models import Medico, Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['nome_paciente', 'data', 'medico', 'status']

class PesquisaEspecialidade(forms.Form):
    especialidade = forms.CharField(required=False, max_length=100, label='Especialidade'),
    medico = forms.CharField(required=False, max_length=100, label='Médico')

    