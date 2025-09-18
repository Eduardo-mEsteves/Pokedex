from django import forms
<<<<<<< Updated upstream:pokedex/forms.py
from .models import Pokemon
=======
from .models import Pokemon 
>>>>>>> Stashed changes:app/forms.py

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
<<<<<<< Updated upstream:pokedex/forms.py
        fields = {'nome', 'tipo', 'numero', 'imagem'} 
           

=======
        fields = ['nome']
>>>>>>> Stashed changes:app/forms.py
