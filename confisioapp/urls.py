from django.conf.urls import url
from . import views 

app_name = 'confisioapp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^atendimento/$', views.atendimento, name='atendimento'),
    url(r'^paciente/$', views.paciente, name='paciente'),
    url(r'^login/$', views.login, name='login'),
    url(r'^retorno/$', views.retorno, name='retorno'),
    url(r'^cadastro_pacientes/$', views.cadastro_pacientes, name='cadastro_pacientes'),
    url(r'^consulta_pacientes/$', views.consulta_pacientes, name='consulta_pacientes'),
    url(r'^consulta_retorno/$', views.consulta_retorno, name='consulta_retorno'),
    url(r'^lancamento_retorno/$', views.lancamento_retorno, name='lancamento_retorno'),
    url(r'^lanca_atendimento/$', views.lanca_atendimento, name='lanca_atendimento'),
    url(r'^consulta_atendimento/$', views.consulta_atendimento, name='consulta_atendimento'),
    url(r'^processa_cadastro_paciente/$', views.processa_cadastro_paciente, name='processa_cadastro_paciente'),
     url(r'^cadastro_doenca/$', views.cadastro_doenca, name='cadastro_doenca'),
    url(r'^cadastro_aparelho/$', views.cadastro_aparelho, name='cadastro_aparelho'),
    url(r'^mensagem/$', views.mensagem, name='mensagem'),
    url(r'^edicao_paciente/(?P<pk>[0-9]+)/$', views.edicao_paciente, name='edicao_paciente'),
    url(r'^edicao_atendimento/(?P<pk>[0-9]+)/$', views.edicao_atendimento, name='edicao_atendimento'),
    url(r'^criaEventoApi/$', views.criaEventoApi, name='criaEventoApi'),
    url(r'^trataData/$', views.trataData, name='trataData'),

    #url(r'^', include(confisioapp.urls)),

]
