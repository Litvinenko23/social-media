from rest_framework import serializers

from social_media.models import Post, Hashtag


class HashtagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hashtag
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("user",)


class PostListSerializer(PostSerializer):
    pass


class PostDetailSerializer(PostSerializer):
    pass


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "image", )
