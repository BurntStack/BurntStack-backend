from rest_framework import viewsets

from .models import Faq
from .serializers import FaqSerializer


class FaqViewSet(viewsets.ReadOnlyModelViewSet):
    """Public, read-only access to active FAQs."""

    queryset = Faq.objects.filter(is_active=True)
    serializer_class = FaqSerializer
    pagination_class = None
    filterset_fields = ["category"]
