from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Produit
from .models import Commande
from .models import Fournisseur
#from crispy_forms.helper import FormHelper

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"
        #fields = ['libelle','description']
        
class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"
    
class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__"

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    
class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')