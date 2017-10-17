from django.shortcuts import render
from .models import Paciente,Atendimento
from django.shortcuts import redirect

# Criar funções para requisição!!

def home(request):
    return render(request,'confisioapp/home.html')

def atendimento(request):
    lista_pacientes = Paciente.objects.order_by('nome')
    return render(request,'confisioapp/atendimento.html', {'lista_pacientes': lista_pacientes})

def consulta_atendimento(request):
    lista_atendimentos = Atendimento.objects.all()
    contexto = {
        'lista_atendimentos' : lista_atendimentos,
    }
    return render(request,'confisioapp/consulta_atendimento.html',contexto)

def paciente(request):
    return render(request,'confisioapp/paciente.html')

def login(request):
    return render(request,'confisioapp/login.html')

def retorno(request):
    return render(request,'confisioapp/retorno.html')

def cadastro_pacientes(request):
    return render(request,'confisioapp/cadastro_pacientes.html')

def cadastro_doenca(request):
    return render(request,'confisioapp/cadastro_doenca.html')

def cadastro_aparelho(request):
    return render(request,'confisioapp/cadastro_aparelho.html')

def processa_cadastro_paciente(request):
    nome = request.POST.get("nome")
    endereco = request.POST.get("endereco")
    email = request.POST.get("email")
    cpf = request.POST.get("cpf")
    dataNasci = request.POST.get("dataNascimento")
    telefone = request.POST.get("telefone")
    altura = request.POST.get("altura")
    peso = request.POST.get("peso")
    observacao = request.POST.get("observacao")

    paciente = Paciente(

        nome = nome,
        cpf = cpf,
        email = email,
        telefone = telefone,
        data_nascimento = dataNasci,
        peso = peso,
        altura = altura,
        observacao = observacao,
        endereco = endereco

    )

    paciente.save()
    return redirect('/consulta_pacientes/')
    

def consulta_pacientes(request):
    lista_pacientes = Paciente.objects.all()
    contexto = {
        'lista_pacientes' : lista_pacientes,
    }
    return render(request,'confisioapp/consulta_pacientes.html',contexto)

def lancamento_retorno(request):
    return render(request,'confisioapp/lancamento_retorno.html', {'paciente': paciente})

def consulta_retorno(request):
    return render(request,'confisioapp/consulta_retorno.html')

def mensagem(request):
    return render(request,'confisioapp/mensagem.html')

def lanca_atendimento(request):
    nome = request.POST.get("nome")
    avaliacao = request.POST.get("avaliacao")
    diasUso = request.POST.get("diasUso")
    dias4 = request.POST.get("dias4")
    mediaHoras = request.POST.get("mediaHoras")
    pressaoM = request.POST.get("pressaoM")
    iah = request.POST.get("iah")
    ia = request.POST.get("ia")
    ih = request.POST.get("ih")
    iac = request.POST.get("iac")
    queixa = request.POST.get("queixa")
    conduta = request.POST.get("queixa")
    valor = request.POST.get("valorConsulta")

    atendimento = Atendimento (
        
        periodo_avaliacao = avaliacao,
        dias_mais_quatro = dias4,
        media_horas = mediaHoras,
        pressao_media = pressaoM,
        iah = iah,
        ia = ia,
        ih = ih,
        ia_central = iac,
        queixa = queixa,
        conduta = conduta,
        valor_consulta = valor

    )

    atendimento.save()
    return redirect('/consulta_atendimento/')
