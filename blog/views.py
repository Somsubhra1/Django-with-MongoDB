from blog.serializers import BlogSerializer
from rest_framework import viewsets
from .models import Blog
# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
