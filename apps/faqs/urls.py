from rest_framework.routers import DefaultRouter

from .views import FaqViewSet

router = DefaultRouter()
router.register("", FaqViewSet, basename="faq")

urlpatterns = router.urls
