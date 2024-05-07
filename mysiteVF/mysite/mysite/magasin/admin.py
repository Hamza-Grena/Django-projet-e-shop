from django.contrib import admin

from .models import Produit
from .models import Categorie
from .models import Fournisseur
from .models import ProduitNC
from .models import Commande

admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(Commande)