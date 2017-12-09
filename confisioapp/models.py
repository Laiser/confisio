from django.db import models
from django.utils import timezone



class Paciente(models.Model):
    nome = models.CharField(max_length= 200)
    endereco = models.CharField(max_length= 200)
    cpf = models.CharField(max_length = 15)
    email = models.CharField(max_length= 200)
    telefone = models.CharField(max_length = 15)
    data_nascimento = models.DateField()
    peso = models.FloatField()
    altura = models.FloatField()
    observacao = models.CharField(max_length = 500)
    imagem = models.ImageField(upload_to = "\img\chaifoto.jpg",blank=True)

    def __str__(self):
        return self.nome


class Atendimento(models.Model):
    id_paciente = models.ForeignKey(Paciente)
    periodo_avaliacao = models.IntegerField()
    dias_mais_quatro = models.IntegerField()
    media_horas = models.FloatField()
    pressao_media = models.FloatField()
    iah = models.FloatField()
    ia = models.FloatField()
    ih = models.FloatField()
    ia_central = models.FloatField()
    queixa = models.CharField(max_length = 500)
    conduta = models.CharField(max_length = 500)
    valor_consulta =models.FloatField()
    doenca = models.ManyToManyField('Doenca')
    equipamento = models.ManyToManyField('Equipamento') 

    def __str__(self):
        return self.queixa

class Doenca(models.Model):
    nome = models.CharField(max_length= 200)

    def __str__(self):
        return self.nome

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

class Equipamento(models.Model):
    nome = models.CharField(max_length= 200)

    def __str__(self):
        return self.nome

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

class Retorno(models.Model):
    id_paciente = models.ForeignKey(Paciente)
    data = models.DateField()
    hora = models.TimeField()
    description = models.CharField(max_length= 200, default="")
