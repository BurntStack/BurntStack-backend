from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """Public, read-only access to portfolio projects."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"
    filterset_fields = ["category", "is_featured"]
    search_fields = ["name", "category", "problem", "solution"]
