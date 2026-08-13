from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.throttling import ScopedRateThrottle

from .models import ContactMessage
from .serializers import ContactMessageSerializer
from .tasks import send_contact_notification


class ContactMessageViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Public endpoint that accepts contact-form submissions (create only)."""

    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "contact"

    def perform_create(self, serializer):
        instance = serializer.save()
        # Fire-and-forget notification (synchronous if Celery runs eagerly).
        send_contact_notification.delay(instance.id)
