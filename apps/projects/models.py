from django.db import models
from django.utils.text import slugify

from apps.core.models import TimeStampedModel


class Project(TimeStampedModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    category = models.CharField(max_length=80)
    cover_image = models.ImageField(upload_to="projects/", blank=True, null=True)
    tech = models.JSONField(default=list, blank=True, help_text="List of technologies")
    problem = models.TextField()
    solution = models.TextField()
    results = models.TextField()
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
