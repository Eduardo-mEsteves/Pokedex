from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pokemon
from .forms import PokemonForm
import requests

# Create your views here.
def testando(request):
    return render(request, 'testando.html')