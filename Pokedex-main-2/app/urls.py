
from django.urls import path
from .views import webdex_home, webdex_procurar_nome, webdex_favoritos, webdex_retirar

urlpatterns = [
    path("",webdex_home,name="webdex-home"),
    path("favoritos/", webdex_favoritos, name="webdex-favoritos"),
    path("favoritos/tirar/<int:pk>", webdex_retirar, name="retira-pokemon"),
    path("pokemon/<str:pokemon>/",webdex_procurar_nome, name="webdex-pokemon-nome"),
]
