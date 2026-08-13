from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Public newsletter subscription endpoint (create only)."""

    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [AllowAny]
