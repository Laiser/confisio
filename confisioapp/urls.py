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



    #url(r'^', include(confisioapp.urls)),

]
