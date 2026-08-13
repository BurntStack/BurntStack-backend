from rest_framework import serializers

from .models import Application, JobOpening

RESUME_MAX_MB = 5
RESUME_ALLOWED = (".pdf", ".doc", ".docx")


class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields = [
            "id", "title", "slug", "department", "location",
            "employment_type", "description", "created_at",
        ]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "id", "job", "name", "email", "phone", "role",
            "portfolio_url", "cover_letter", "resume", "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_resume(self, value):
        if value is None:
            return value
        if value.size > RESUME_MAX_MB * 1024 * 1024:
            raise serializers.ValidationError(f"Résumé must be under {RESUME_MAX_MB}MB.")
        if not value.name.lower().endswith(RESUME_ALLOWED):
            raise serializers.ValidationError("Résumé must be a PDF or Word document.")
        return value
