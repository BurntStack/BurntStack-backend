from rest_framework import mixins, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny

from .models import Application, JobOpening
from .serializers import ApplicationSerializer, JobOpeningSerializer


class JobOpeningViewSet(viewsets.ReadOnlyModelViewSet):
    """Public, read-only list of active job openings."""

    queryset = JobOpening.objects.filter(is_active=True)
    serializer_class = JobOpeningSerializer
    lookup_field = "slug"
    filterset_fields = ["department", "employment_type"]
    search_fields = ["title", "description", "location"]


class ApplicationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Public endpoint to submit a job application (supports résumé upload)."""

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]
