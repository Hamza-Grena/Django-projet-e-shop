from rest_framework.serializers import ModelSerializer
from .models import Post
class BlogSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug','author','updated_on','content','created_on','status','image']