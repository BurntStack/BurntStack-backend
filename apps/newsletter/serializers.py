from rest_framework import serializers

from .models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ["id", "email", "created_at"]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        # Re-subscribing an existing (possibly inactive) email is idempotent.
        subscriber, _ = Subscriber.objects.update_or_create(
            email=validated_data["email"], defaults={"is_active": True}
        )
        return subscriber
