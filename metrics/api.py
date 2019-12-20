from metrics.models import ScholarProfile
from rest_framework import viewsets, permissions
from .serializers import ScholarProfileSerializer

# ScholarProfile Viewset

class ScholarProfileViewSet(viewsets.ModelViewSet):
	queryset = ScholarProfile.objects.all()
	permission_classes = [
	permissions.AllowAny
	]
	serializer_class = ScholarProfileSerializer