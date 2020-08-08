from rest_framework import viewsets, permissions
from metrics.models import ScholarData
from .serializers import ScholarSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class ScholarViewSet(viewsets.ModelViewSet):
    queryset = ScholarData.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScholarSerializer
    filter_backends = [SearchFilter]
    search_fields = ['scholarName', 'workplace', 'isStarred']
