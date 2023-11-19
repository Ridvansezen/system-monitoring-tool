from rest_framework import serializers
from .models import SystemMonitoringData

class SystemMonitoringDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemMonitoringData
        fields = '__all__'