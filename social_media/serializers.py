from rest_framework import serializers

from social_media.models import Post, Hashtag


class HashtagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hashtag
        fields = ("name",)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "image", "content", "created_at", "user", "hashtags", )
        read_only_fields = ("user",)


class PostListSerializer(PostSerializer):
    hashtags = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    user = serializers.CharField(source="user.email", read_only=True)


class PostDetailSerializer(PostSerializer):
    hashtags = HashtagSerializer(many=True, read_only=True)
    user = serializers.CharField(source="user.email", read_only=True)


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "image", )
