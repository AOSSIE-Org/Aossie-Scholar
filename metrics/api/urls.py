from rest_framework import routers
from metrics.api.views import ScholarViewSet

router = routers.DefaultRouter()
router.register('', ScholarViewSet)
urlpatterns = router.urls
