from rest_framework import viewsets
from .models import SystemMonitoringData
from .serializers import SystemMonitoringDataSerializer
from django.shortcuts import render
from django.utils import timezone
from .tasks import update_system_data
from.service import save_system_data


class SystemMonitoringViewSet(viewsets.ModelViewSet):

    def list(self, request):
        update_system_data()
        data = SystemMonitoringData.objects.order_by('-timestamp')[:10]
        serializer = SystemMonitoringDataSerializer(data, many=True)
        formatted_timestamp = timezone.now().strftime("%B %d, %Y %H:%M:%S")
        latest_data = data.first()

        json_data = {
            'cpuUsage': 70.0,
            'ramUsage': 50.0,
            'hddUsage': 80.0,
        }

        context = {
            'json_data': json_data,
            'data': serializer.data,
            'formatted_timestamp': formatted_timestamp,
            'latest_data': latest_data,
        }

        return render(request, 'index.html', context)
        
    