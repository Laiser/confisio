from django.shortcuts import render


# Criar funções para requisição!!

def home(request):
    return render(request,'confisioapp/home.html')

def atendimento(request):
    return render(request,'confisioapp/atendimento.html')

def paciente(request):
    return render(request,'confisioapp/paciente.html')