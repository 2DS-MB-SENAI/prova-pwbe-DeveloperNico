from django.db import models

class Medico(models.Model):
    nome_medico = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=50, choices=(
        ("Cardiologista", "Cardiologista"),
        ("Oftalmologista", "Oftalmologista"),
        ("Pediatra", "Pediatra")
    ))
    crm = models.CharField(max_length=8, unique=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome_medico
    
class Consulta(models.Model):
    nome_paciente = models.CharField(max_length=50)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=(
        ("Agendado", "Agendado"),
        ("Realizado", "Realizado"),
        ("Cancelado", "Cancelado")
    ))

    def __str__(self):
        return self.nome_paciente