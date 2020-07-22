from rest_framework import routers
from metrics.api import ScholarProfileViewSet

router = routers.DefaultRouter()
router.register('metrics', ScholarProfileViewSet, 'metrics')
