from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "is_featured", "order"]
    list_filter = ["is_featured", "category"]
    search_fields = ["name", "problem", "solution", "results"]
    list_editable = ["is_featured", "order"]
    prepopulated_fields = {"slug": ("name",)}
