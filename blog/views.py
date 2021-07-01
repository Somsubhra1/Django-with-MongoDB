from blog.serializers import PostSerializer
from rest_framework import viewsets
from .models import Post
# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
