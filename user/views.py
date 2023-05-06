from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from social_media.permissions import IsAdminOrIfAuthenticatedReadOnly
from .serializers import (
    UserSerializer,
    AuthTokenSerializer,
    SubscribeUserSerializer,
)


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = AuthTokenSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            Token.objects.filter(user=user).delete()
            return Response({"detail": "Logout successful."})
        else:
            return Response({"detail": "User not authenticated."}, status=400)


class SubscribeUserView(generics.CreateAPIView):
    serializer_class = SubscribeUserSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user_to_follow_id = serializer.validated_data["user_to_follow"]
        user_to_follow = get_user_model().objects.get(id=user_to_follow_id)
        self.request.user.following.add(user_to_follow)
        user_to_follow.followers.add(self.request.user)


class UnsubscribeUserView(generics.DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def perform_destroy(self, instance):
        user_to_unfollow = instance
        self.request.user.following.remove(user_to_unfollow)
        user_to_unfollow.followers.remove(self.request.user)


class UserFollowingListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.following.all()


class UserFollowersListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.followers.all()
