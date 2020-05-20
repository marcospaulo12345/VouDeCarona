"""VouDeCarona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from carona import views
from django.conf.urls.static import static
from django.conf import settings
from carona.models import Carona


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('procurar/', views.procurar, name='procurar'),
    path('procurar/submit', views.submit_con_carona, name = 'submitProcuar'),
    path('ofertarCarona/', views.ofertarCarona, name='ofertarCarona'),
    path('ofertarCarona/submit', views.ofertarCarona, name='ofertarCaronaSubmit'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/submit', views.submit_cadastro, name='submit_cadastro'),
    path('cadastroCarro/', views.cadastroCarro, name='cadastroCarro'),
    path('login/', views.submit_login, name='login'),
    path('login/submit', views.submit_login, name='submit_login'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/submit/<int:id_usuario>', views.alteraDadosUsuario, name='alteraDadosUsuario'),
    path('perfilPublico/<int:user_id>', views.perfilPublico, name='perfilPublico'),
    path('detalhesCarona/<int:idi>', views.detalhesCarona, name='detalhesCarona'),
    path('alteraSenha/', views.alterarSenha, name='alteraSenha'),
    path('alteraFoto/<int:id_user>', views.alteraFoto, name='alteraFoto'),
    path('', views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
