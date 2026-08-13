from rest_framework.routers import DefaultRouter

from .views import ApplicationViewSet, JobOpeningViewSet

router = DefaultRouter()
router.register("applications", ApplicationViewSet, basename="application")
router.register("", JobOpeningViewSet, basename="job")

urlpatterns = router.urls
