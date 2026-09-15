"""Root URL configuration for the BurntStack API."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.core.views import api_root, health_check

api_patterns = [
    path("", api_root, name="api-root"),
    path("health/", health_check, name="health"),
    # JWT authentication
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Feature apps
    path("contact/", include("apps.contact.urls")),
    path("newsletter/", include("apps.newsletter.urls")),
    path("careers/", include("apps.careers.urls")),
    path("projects/", include("apps.projects.urls")),
    path("testimonials/", include("apps.testimonials.urls")),
    path("faqs/", include("apps.faqs.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Branded admin
admin.site.site_header = "BurntStack Administration"
admin.site.site_title = "BurntStack Admin"
admin.site.index_title = "Dashboard"
