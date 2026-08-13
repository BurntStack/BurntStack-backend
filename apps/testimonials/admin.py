from django.contrib import admin

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["name", "company", "rating", "is_active", "order"]
    list_filter = ["is_active", "rating"]
    search_fields = ["name", "company", "review"]
    list_editable = ["is_active", "order"]
