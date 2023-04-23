from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from social_media.models import Post, Hashtag
from social_media.permissions import IsAdminOrIfAuthenticatedReadOnly
from social_media.serializers import PostSerializer, HashtagSerializer, PostImageSerializer, PostListSerializer, \
    PostDetailSerializer


class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly, )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_queryset(self):
        queryset = self.queryset

        if self.action == "retrieve":
            queryset = queryset

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer

        if self.action == "retrieve":
            return PostDetailSerializer

        if self.action == "upload_image":
            return PostImageSerializer

        return PostSerializer

    @action(methods=["POST"], detail=True, url_path="upload_image")
    def upload_image(self, request, pk=None):
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def own_posts(self, request):
        posts = Post.objects.filter(user=request.user)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def following_posts(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(user__in=following_users)
        serializer = self.get_serializer(posts, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search_posts_by_hashtag(self, request, hashtag):
        hashtag_obj, _ = Hashtag.objects.get_or_create(name=hashtag)
        posts = Post.objects.filter(hashtags=hashtag_obj)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
