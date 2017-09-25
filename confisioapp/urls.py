from django.conf.urls import url
from . import views 

app_name = 'confisioapp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^atendimento/$', views.atendimento, name='atendimento'),
    url(r'^paciente/$', views.paciente, name='paciente'),
    url(r'^login/$', views.login, name='login'),
    url(r'^retorno/$', views.retorno, name='retorno'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^consulta/$', views.consulta, name='consulta'),

    #url(r'^', include(confisioapp.urls)),

]
