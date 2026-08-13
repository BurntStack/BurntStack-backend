from django.db import models
from django.utils.text import slugify

from apps.core.models import TimeStampedModel


class JobOpening(TimeStampedModel):
    class EmploymentType(models.TextChoices):
        FULL_TIME = "Full-time", "Full-time"
        PART_TIME = "Part-time", "Part-time"
        CONTRACT = "Contract", "Contract"
        INTERNSHIP = "Internship", "Internship"

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    department = models.CharField(max_length=80)
    location = models.CharField(max_length=120)
    employment_type = models.CharField(
        max_length=20, choices=EmploymentType.choices, default=EmploymentType.FULL_TIME
    )
    description = models.TextField()
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta(TimeStampedModel.Meta):
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Application(TimeStampedModel):
    job = models.ForeignKey(
        JobOpening, on_delete=models.SET_NULL, null=True, blank=True, related_name="applications"
    )
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    role = models.CharField(max_length=150)
    portfolio_url = models.URLField(blank=True)
    cover_letter = models.TextField(blank=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    is_reviewed = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return f"{self.name} — {self.role}"
