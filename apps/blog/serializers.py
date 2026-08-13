from rest_framework import serializers

from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class PostListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = [
            "id", "title", "slug", "excerpt", "category", "author",
            "cover_image", "tags", "reading_time", "is_featured", "published_at",
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id", "title", "slug", "excerpt", "content", "category", "author",
            "cover_image", "tags", "reading_time", "is_featured", "published_at",
            "created_at",
        ]
