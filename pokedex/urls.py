from django.urls import path
from . import views
from .views import testando


urlpatterns = [
    path('', views.testando, name='testando'),  
]