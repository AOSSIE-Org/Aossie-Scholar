from rest_framework import serializers
from metrics.models import ScholarProfile

class ScholarProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = ScholarProfile
		fields = '__all__'