from django.contrib import admin
from .models import Atendimento,Doenca,Equipamento,Paciente,Retorno

admin.site.register(Atendimento)
admin.site.register(Doenca)
admin.site.register(Equipamento)
admin.site.register(Paciente)
admin.site.register(Retorno)