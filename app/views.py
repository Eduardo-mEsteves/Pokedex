
from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import Pokemon
from random import randint
from .forms import PokemonForm

def webdex_home(request):
    if request.method == 'GET':
        tipo        = request.GET.get('tipo')
        pokemonNAME = request.GET.get('pokemonNAME')
        pokemonID   = request.GET.get('pokemonID')

        if tipo  == 'random':
            response  = requests.get(f"https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1010")
            if response.status_code == 200:
                data    = response.json()
                return redirect('webdex-pokemon-nome', pokemon=data["results"][randint(1,1010)]["name"])

        if pokemonNAME or pokemonID:
            if   tipo     == 'nome':
                response  = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonNAME}")
            elif tipo     == 'id':
                response  = requests.get(f"https://pokeapi.co/api/v2/pokemon-form/{pokemonID}")
            
            if response.status_code == 200:
                if tipo   == 'nome':
                    return redirect('webdex-pokemon-nome', pokemon=pokemonNAME)
                elif tipo == 'id':
                    data    = response.json()
                    return redirect('webdex-pokemon-nome', pokemon=data["pokemon"]["name"])
            else:
                return render(request, 'html/home.html', {'error': 'O nome ou id do pokemon está errado!'})

    return render(request, 'html/home.html')

def webdex_procurar_nome(request,pokemon):
    url       = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    data      = requests.get(url).json()

    tipo1     = data["types"][0]["type"]["name"]

    try:
        tipo2 = data["types"][1]["type"]["name"] # TIPO 2 SE TIVER
    except Exception:
        tipo2 = ''

    informacoes = {
        "id":        data["id"],
        "nome":      data["name"],
        "img":       data["sprites"]["front_default"],
        "peso":      float(data["weight"])/10,
        "tipo1":     tipo1,
        "tipo2":     tipo2,
        "hp":        data["stats"][0]["base_stat"],
        "forca":     data["stats"][1]["base_stat"],
        "defesa":    data["stats"][2]["base_stat"],
        "forca_esp": data["stats"][3]["base_stat"],
        "defesa_esp":data["stats"][4]["base_stat"],
        "velocidade":data["stats"][5]["base_stat"],
    }

    if request.method == 'POST':
        favoritar = Pokemon(
            pokemon_id = informacoes["id"],
            nome       = informacoes["nome"],
            img        = informacoes["img"],
            peso       = informacoes["peso"],
            tipo1      = informacoes["tipo1"],
            tipo2      = informacoes["tipo2"],
            hp         = informacoes["hp"],
            forca      = informacoes["forca"],
            defesa     = informacoes["defesa"],
            forca_esp  = informacoes["forca_esp"],
            defesa_esp = informacoes["defesa_esp"],
            velocidade = informacoes["velocidade"],
        )
        favoritar.save()
        return redirect("webdex-home")

    return render(request, 'html/pokemon.html', {"pokemon":informacoes})

def webdex_favoritos(request):
    pokemons_favoritos = Pokemon.objects.all()
    return render(request, 'html/favoritos.html', {'favoritos':pokemons_favoritos})

def webdex_retirar(request,pk):
    pokemon_deletar = Pokemon.objects.get(pk=pk).delete()
    return redirect("webdex-favoritos")

def webdex_editar(request, pk):
    pokemon_editar = Pokemon.objects.get(pk=pk)
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon_editar)
        if form.is_valid():
            pokemon_editado = form.save(commit=False)

            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_editado.nome}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                pokemon_editado.pokemon_id = data["id"]
                pokemon_editado.img = data["sprites"]["front_default"]
                pokemon_editado.peso = float(data["weight"])/10
                pokemon_editado.tipo1 = data["types"][0]["type"]["name"]
                try:
                    pokemon_editado.tipo2 = data["types"][1]["type"]["name"]
                except Exception:
                    pokemon_editado.tipo2 = ''
                pokemon_editado.hp = data["stats"][0]["base_stat"]
                pokemon_editado.forca = data["stats"][1]["base_stat"]
                pokemon_editado.defesa = data["stats"][2]["base_stat"]
                pokemon_editado.forca_esp = data["stats"][3]["base_stat"]
                pokemon_editado.defesa_esp = data["stats"][4]["base_stat"]
                pokemon_editado.velocidade = data["stats"][5]["base_stat"]
            else:
                form.add_error('nome', 'Nome de Pokémon inválido.')
                return render(request, 'html/editar.html', {'form': form, 'pokemon': pokemon_editar})
            form.save()
            return redirect('webdex-favoritos')
    else:
        form = PokemonForm(instance=pokemon_editar)

    return render(request, 'html/editar.html', {'form': form, 'pokemon': pokemon_editar})
