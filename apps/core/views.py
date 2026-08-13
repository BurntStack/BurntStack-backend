from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    """Lightweight liveness probe for load balancers / uptime monitors."""
    return Response({"status": "ok", "time": timezone.now().isoformat()})


@api_view(["GET"])
@permission_classes([AllowAny])
def api_root(request, format=None):
    """Browsable index of the available API endpoints."""
    return Response(
        {
            "health": reverse("health", request=request, format=format),
            "auth": {
                "token": reverse("token_obtain_pair", request=request, format=format),
                "refresh": reverse("token_refresh", request=request, format=format),
                "verify": reverse("token_verify", request=request, format=format),
            },
            "contact": reverse("contact-list", request=request, format=format),
            "newsletter": reverse("newsletter-list", request=request, format=format),
            "blog": reverse("post-list", request=request, format=format),
            "careers": reverse("job-list", request=request, format=format),
            "projects": reverse("project-list", request=request, format=format),
            "testimonials": reverse("testimonial-list", request=request, format=format),
            "faqs": reverse("faq-list", request=request, format=format),
        }
    )
