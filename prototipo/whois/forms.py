from django import forms
from models import Enlaces

class Search(forms.Form):
    SearchLink = forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={
            'class': ' form-control',
            'placeholder': 'Escribe tu palabra...'
        }
    ))
