from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import redirect

def home(request):
    return render(request,'confisioapp/home.html')

def atendimento(request):
    lista_pacientes = Paciente.objects.order_by('nome')
    doencas = Doenca.objects.order_by('nome')
    equipamentos = Equipamento.objects.order_by('nome')
    contexto = {
        'lista_pacientes' : lista_pacientes,
        'doencas' : doencas,
        'equipamentos' : equipamentos,
    }
    return render(request,'confisioapp/atendimento.html', contexto)

def consulta_atendimento(request):
    lista_atendimentos = Atendimento.objects.all()
    lista_pacientes = Paciente.objects.all()    
    contexto = {
        'lista_atendimentos' : lista_atendimentos,
        'lista_pacientes' : lista_pacientes,
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
    if request.method == "POST":
        nome = request.POST.get("doenca")
        doenca = Doenca(
            nome= nome
        )
        doenca.save()
        return redirect('/')

    return render(request,'confisioapp/cadastro_doenca.html')

def cadastro_aparelho(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        equipamento = Equipamento(
            nome= nome
        )
        equipamento.save()
        return redirect('/')
        
    return render(request,'confisioapp/cadastro_aparelho.html')

def processa_cadastro_paciente(request):
    try:
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
    except Exception:
        error = True
        return render(request, 'confisioapp/cadastro_pacientes.html', {'error': error})
        
        


def edicao_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":    
        try:
            paciente.nome = request.POST.get("nome")
            paciente.endereco = request.POST.get("endereco")
            paciente.email = request.POST.get("email")
            paciente.cpf = request.POST.get("cpf")
            paciente.data_nascimento = request.POST.get("dataNascimento")
            paciente.telefone = request.POST.get("telefone")
            paciente.altura = request.POST.get("altura")
            paciente.peso = request.POST.get("peso")
            paciente.observacao = request.POST.get("observacao")
            paciente.save()
            return redirect('/consulta_pacientes/')
        except Exception:
            error = True
            contexto = {
                'paciente' : paciente,
                'error' : error,
            }
            return render(request, 'confisioapp/cadastro_pacientes.html', contexto)                    
    else:
        return render(request, 'confisioapp/cadastro_pacientes.html', {'paciente': paciente})


def edicao_atendimento(request, pk):
    atendimento = get_object_or_404(Atendimento, pk=pk)
    if request.method == "POST":
        atendimento.id_paciente = Paciente.objects.get(nome=request.POST.get("nome"))
        atendimento.periodo_avaliacao = request.POST.get("avaliacao")
        #atendimento.diasUso = request.POST.get("diasUso") NÃO EXISTE NO MODEL
        atendimento.dias_mais_quatro = request.POST.get("dias4")
        atendimento.media_horas = request.POST.get("mediaHoras")
        atendimento.pressao_media = request.POST.get("pressaoM")
        atendimento.iah = request.POST.get("iah")
        atendimento.ia = request.POST.get("ia")
        atendimento.ih = request.POST.get("ih")
        atendimento.ia_central = request.POST.get("iac")
        atendimento.queixa = request.POST.get("queixa")
        atendimento.conduta = request.POST.get("queixa")
        atendimento.valor_consulta = request.POST.get("valorConsulta")
        aux = atendimento.doenca.all()
        for x in aux:
            atendimento.doenca.remove(x)
        aux = atendimento.equipamento.all()
        for x in aux:
            atendimento.equipamento.remove(x)
        atendimento.doenca.add(Doenca.objects.get(nome=request.POST.get("doenca")))
        atendimento.equipamento.add(Equipamento.objects.get(nome=request.POST.get("aparelho")))
        atendimento.save()
        return redirect('/consulta_atendimento/')
    else:        
        paciente = None
        paciente = Paciente.objects.get(nome=atendimento.id_paciente)        
        doencas = Doenca.objects.order_by('nome')
        AuxDoenca = [(value, True) if str(value) == str(aux) else (value, False) for value in doencas for aux in atendimento.doenca.all()]
        equipamentos = Equipamento.objects.order_by('nome')
        AuxEquip = [(value, True) if str(value) == str(equip) else (value, False) for value in equipamentos for equip in atendimento.equipamento.all()]
        lista_pacientes = Paciente.objects.order_by('nome')        
        
        contexto = {
            'atendimento' : atendimento,
            'paciente' : paciente,
            'lista_pacientes' : lista_pacientes,
            'doencas' : doencas,
            'AuxEquip' : AuxEquip,
            'AuxDoenca' : AuxDoenca,             
        }
        return render(request, 'confisioapp/atendimento.html', contexto)
    

def consulta_pacientes(request):
    lista_pacientes = Paciente.objects.all()    
    contexto = {
        'lista_pacientes' : lista_pacientes,    
    }
    return render(request,'confisioapp/consulta_pacientes.html',contexto)

def lancamento_retorno(request):
    lista_pacientes = Paciente.objects.all().order_by('nome')
    return render(request,'confisioapp/lancamento_retorno.html', {'lista_pacientes': lista_pacientes})

def consulta_retorno(request):
    return render(request,'confisioapp/consulta_retorno.html')

def mensagem(request):
    return render(request,'confisioapp/mensagem.html')

def lanca_atendimento(request):
    try:
        nome = Paciente.objects.get(nome=request.POST.get("nome"))
        avaliacao = request.POST.get("avaliacao")
        #diasUso = request.POST.get("diasUso")   NÃO TEM NO MODEL
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
        doenca = Doenca.objects.get(nome=request.POST.get("doenca"))
        equipamento = Equipamento.objects.get(nome=request.POST.get("aparelho"))
        atendimento = Atendimento (
            id_paciente = nome,
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
        atendimento.doenca.add(doenca)
        atendimento.equipamento.add(equipamento)
        return redirect('/consulta_atendimento/')
    except Exception:    
        error = True
        lista_pacientes = Paciente.objects.order_by('nome')
        doencas = Doenca.objects.order_by('nome')
        equipamentos = Equipamento.objects.order_by('nome')
        contexto = {
            'lista_pacientes' : lista_pacientes,
            'doencas' : doencas,
            'equipamentos' : equipamentos,
            'error' : error,
        }
        return render(request, 'confisioapp/atendimento.html', contexto)