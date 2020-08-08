from rest_framework import serializers
from metrics.models import ScholarData

class ScholarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarData
        fields = '__all__'
