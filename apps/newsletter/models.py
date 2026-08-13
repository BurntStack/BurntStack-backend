from django.db import models

from apps.core.models import TimeStampedModel


class Subscriber(TimeStampedModel):
    """A newsletter subscriber."""

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return self.email
