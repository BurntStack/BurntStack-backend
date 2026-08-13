from django.db import models

from apps.core.models import TimeStampedModel


class Faq(TimeStampedModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=80, blank=True, default="General")
    is_active = models.BooleanField(default=True, db_index=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
