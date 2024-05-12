"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib import admin, auth
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from rest_framework import routers
from magasin.views import CategoryAPIView
from blog.views import BlogViewset
# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('blog', BlogViewset, basename='blog')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('magasin/',include('magasin.urls')),
    path('jeux/',include('jeux.urls')),
    path('', views.index, name='acceuil'),
    path('blog/',include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

