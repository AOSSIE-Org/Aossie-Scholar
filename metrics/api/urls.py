from rest_framework import routers
from metrics.api.views import ScholarViewSet, StarredScholarViewSet

router = routers.DefaultRouter()
router.register('scholar', ScholarViewSet)
router.register('starred', StarredScholarViewSet)
urlpatterns = router.urls
