from django.urls import path, include
from rest_framework import routers

from social_media.views import PostViewSet, HashtagViewSet


router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("hashtags", HashtagViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("posts/own_posts/", PostViewSet.as_view({"get": "own_posts"}), name="post-own-posts"),
    path("posts/following_posts/", PostViewSet.as_view({"get": "following_posts"}), name="post-following-posts"),
    path("posts/search_posts_by_hashtag/<str:hashtag>/", PostViewSet.as_view({"get": "search_posts_by_hashtag"}), name="post-search-posts-by-hashtag"),
]

app_name = "social_media"
