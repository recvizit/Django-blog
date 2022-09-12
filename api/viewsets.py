from rest_framework import viewsets
from .serializer import PostSerializers
from blog.models import Post


class PostViewSet(viewsets.ModelViewSet):
    name = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializers
