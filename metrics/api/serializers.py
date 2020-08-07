from rest_framework import serializers
from metrics.models import ScholarData, StarredScholar

class ScholarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarData
        fields = '__all__'


class StarredScholarSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarredScholar
        fields = '__all__'
