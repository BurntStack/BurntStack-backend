from django.contrib import admin

from .models import Faq


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ["question", "category", "is_active", "order"]
    list_filter = ["is_active", "category"]
    search_fields = ["question", "answer"]
    list_editable = ["is_active", "order"]
