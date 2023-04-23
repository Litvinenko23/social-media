from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from social_media.models import Post, Hashtag
from social_media.serializers import PostSerializer, HashtagSerializer


class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = ()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related("hashtags")
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)