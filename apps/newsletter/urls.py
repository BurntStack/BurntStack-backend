from rest_framework.routers import DefaultRouter

from .views import SubscriberViewSet

router = DefaultRouter()
router.register("", SubscriberViewSet, basename="newsletter")

urlpatterns = router.urls
