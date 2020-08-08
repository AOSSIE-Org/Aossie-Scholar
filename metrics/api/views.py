from rest_framework import viewsets, permissions
from metrics.models import ScholarData, StarredScholar
from .serializers import ScholarSerializer, StarredScholarSerializer
from rest_framework.filters import SearchFilter

class ScholarViewSet(viewsets.ModelViewSet):
    queryset = ScholarData.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScholarSerializer
    filter_backends = [SearchFilter]
    search_fields = ['scholarName', 'workplace', 'isStarred']

class StarredScholarViewSet(viewsets.ModelViewSet):
    queryset = StarredScholar.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StarredScholarSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'work']
