from rest_framework import viewsets

from .models import Category, Post
from .serializers import CategorySerializer, PostDetailSerializer, PostListSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Public, read-only list of blog categories."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """Public, read-only access to published blog posts."""

    queryset = Post.objects.filter(is_published=True).select_related("category")
    lookup_field = "slug"
    filterset_fields = ["category__slug", "is_featured"]
    search_fields = ["title", "excerpt", "content", "author"]
    ordering_fields = ["published_at", "reading_time"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        return PostListSerializer
