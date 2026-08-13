from django.db import models

from apps.core.models import TimeStampedModel


class ContactMessage(TimeStampedModel):
    """A message submitted through the public contact form."""

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    is_handled = models.BooleanField(default=False, db_index=True)

    class Meta(TimeStampedModel.Meta):
        verbose_name = "Contact message"

    def __str__(self):
        return f"{self.name} <{self.email}>"
