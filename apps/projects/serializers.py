from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id", "name", "slug", "category", "cover_image", "tech",
            "problem", "solution", "results", "live_url", "github_url",
            "is_featured", "order",
        ]
