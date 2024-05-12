from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, UserCreationForm
from django.contrib.auth.models import User
from .forms import ProduitForm
from .forms import CommandeForm
from .forms import FournisseurForm
from rest_framework import generics
from .models import Produit
from .models import Categorie
from .models import Commande
from .models import Fournisseur
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer,ProduitSerializer

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    if( request.method == "POST" ):
        form = ProduitForm(request.POST,request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = ProduitForm()
    products = Produit.objects.all()
    #context = {'products':products}
    #return render(request,'magasin/majProduits.html',{'form':form})
    return render(request, 'magasin/vitrine.html', {'list':products})#context est une variable python qui assure la communication avec le template

@login_required
def commande(request):
    if( request.method == "POST" ):
        form = CommandeForm(request.POST, request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = CommandeForm()
    commandes = Commande.objects.all()
    
    return render(request, 'magasin/commande.html', {'form':form, 'commandes':commandes})
@login_required
def nouveauFournisseur(request):
    if( request.method == "POST" ):
        form = FournisseurForm(request.POST, request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = FournisseurForm()
    listFour = Fournisseur.objects.all()
    return render(request, 'magasin/fournisseur.html', {'form':form, 'fournisseurs':listFour})
@login_required
def ajouterProduit(request):
    if( request.method == "POST" ):
        form = ProduitForm(request.POST,request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = ProduitForm()
    
    return render(request,'magasin/majProduits.html',{'form':form})

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
class ProduitDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProduitSerializer

    def get_queryset(self):
        return Produit.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj