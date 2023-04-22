from rest_framework import viewsets

from social_media.models import Post
from social_media.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
