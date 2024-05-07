from django.shortcuts import render
from .models import Post
from .forms import PostForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ListePosts(ListView):
    model = Post
    template_name = 'post/liste_posts.html'
    context_object_name = 'posts'

class DetailPost(DetailView):
    model = Post
    template_name = 'post/detail_post.html'
    context_object_name = 'post'
@method_decorator(login_required, name='dispatch')
class CreerPost(CreateView):
    model = Post
    template_name = 'post/creer_post.html'
    form_class = PostForm  
    success_url = reverse_lazy('liste_posts') 
    def form_valid(self, form): 
        self.object = form.save()
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class ModifierPost(UpdateView):
    model = Post
    template_name = 'post/modifier_post.html'
    form_class = PostForm  
    success_url = reverse_lazy('liste_posts')  
@method_decorator(login_required, name='dispatch')
class SupprimerPost(DeleteView):
    model = Post
    template_name = 'post/supprimer_post.html'
    success_url = reverse_lazy('liste_posts')  

class BlogAPIView(APIView):
    def get(self, *args, **kwargs):
        Blogs = Post.objects.all()
        serializer = BlogSerializer(Blogs, many=True)
        return Response(serializer.data)

class BlogViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = BlogSerializer
    def get_queryset(self):
        queryset = Post.objects.filter()
        blog_Id = self.request.GET.get('author_id')
        if blog_Id:
            queryset = queryset.filter(blog_id=blog_Id)
        return queryset