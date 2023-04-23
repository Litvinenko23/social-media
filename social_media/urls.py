from django.urls import path, include
from rest_framework import routers

from social_media.views import PostViewSet, HashtagViewSet


router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("hashtags", HashtagViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "social_media"
