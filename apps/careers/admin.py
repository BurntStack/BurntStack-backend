from django.contrib import admin

from .models import Application, JobOpening


@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ["title", "department", "location", "employment_type", "is_active"]
    list_filter = ["is_active", "department", "employment_type"]
    search_fields = ["title", "description"]
    list_editable = ["is_active"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["name", "role", "email", "is_reviewed", "created_at"]
    list_filter = ["is_reviewed", "created_at"]
    search_fields = ["name", "email", "role"]
    list_editable = ["is_reviewed"]
    date_hierarchy = "created_at"
