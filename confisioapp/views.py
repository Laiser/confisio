from django.shortcuts import render


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

def cadastro(request):
    return render(request,'confisioapp/cadastro.html')

def consulta(request):
    return render(request,'confisioapp/consulta.html')
