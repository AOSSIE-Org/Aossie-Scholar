from rest_framework import viewsets, permissions
from metrics.models import ScholarData, StarredScholar
from .serializers import ScholarSerializer, StarredScholarSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class ScholarViewSet(viewsets.ModelViewSet):
    queryset = ScholarData.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScholarSerializer
    filter_backends = [SearchFilter]
    search_fields = ['scholarName', 'workplace']
    filterset_fields = ['isStarred']

class StarredScholarViewSet(viewsets.ModelViewSet):
    queryset = StarredScholar.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StarredScholarSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'work']
