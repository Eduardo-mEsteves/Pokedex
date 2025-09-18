
from django.urls import path
from .views import webdex_home, webdex_procurar_nome

urlpatterns = [
    path("",webdex_home,name="webdex-home"),
    path("pokemon/<str:pokemon>/",webdex_procurar_nome, name="webdex-pokemon-nome"),
]
