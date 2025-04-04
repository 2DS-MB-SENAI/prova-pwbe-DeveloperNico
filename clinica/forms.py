from django import forms
from .models import Medico, Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['nome_paciente', 'data', 'medico', 'status']