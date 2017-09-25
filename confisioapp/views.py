from django.shortcuts import render
from .models import Paciente

# Criar funções para requisição!!

def home(request):
    return render(request,'confisioapp/home.html')

def atendimento(request):
    return render(request,'confisioapp/atendimento.html')

def paciente(request):
    return render(request,'confisioapp/paciente.html')

def login(request):
    return render(request,'confisioapp/login.html')

def retorno(request):
    return render(request,'confisioapp/retorno.html')

def cadastro_pacientes(request):
    return render(request,'confisioapp/cadastro_pacientes.html')

def consulta_pacientes(request):
    return render(request,'confisioapp/consulta_pacientes.html')

def lancamento_retorno(request):
    return render(request,'confisioapp/lancamento_retorno.html')

def consulta_retorno(request):
    return render(request,'confisioapp/consulta_retorno.html')

def lanca_atendimento(request):
    nome = request.POST.get("nome")
    avaliacao = request.POST.get("avaliacao")
    diasUso = request.POST.get("diasUso")
    dias4 = request.POST.get("dias4")
    mediaHoras = request.POST.get("mediaHoras")
    pressaoM = request.POST.get("pressaoM")
    iah = request.POST.get("iah")
    ih = request.POST.get("ih")
    iac = request.POST.get("iac")
    paciente = Paciente (
        nome = nome,
        avaliacao = avaliacao,
        diasUso = diasUso,
        dias4 = dias4,
        mediaHoras = mediaHoras,
        pressaoM = pressaoM,
        iah = iah,
        ih = ih,
        iac = iac
    )

    paciente.save()
    return redirect('confisio:home')
