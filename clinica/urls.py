from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.listar_medico, name="listar_medicos"),
    path('consultas/<int:pk>', views.detalhes_consulta, name="detalhes_consulta"),
    path('consultas/nova/', views.criar_consulta, name="criar_consulta")
]