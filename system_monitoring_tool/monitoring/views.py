from rest_framework import viewsets
from rest_framework.response import Response
from .models import SystemMonitoringData
from .serializers import SystemMonitoringDataSerializer
import psutil

class SystemMonitoringViewSet(viewsets.ModelViewSet):
    queryset = SystemMonitoringData.objects.all()
    serializer_class = SystemMonitoringDataSerializer

    def list(self, request):
        # RAM, CPU, HDD ölçümlerini al
        ram_usage = psutil.virtual_memory().percent
        cpu_usage = psutil.cpu_percent()
        hdd_usage = psutil.disk_usage('/').percent

        # Network isteklerini logla (burada dummy bir değer kullanıldı)
        network_requests = 10

        # Veritabanına kaydet
        SystemMonitoringData.objects.create(
            ram_usage=ram_usage,
            cpu_usage=cpu_usage,
            hdd_usage=hdd_usage,
            network_requests=network_requests,
        )

        # Son 10 kaydı çekip serialize et ve API yanıtını oluştur
        data = SystemMonitoringData.objects.order_by('-timestamp')[:10]
        serializer = SystemMonitoringDataSerializer(data, many=True)
        return Response(serializer.data)