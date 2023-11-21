import psutil
from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from .models import SystemMonitoringData
from .serializers import SystemMonitoringDataSerializer


class SystemMonitoringViewSet(viewsets.ModelViewSet):
    def list(self, request):
        # RAM, CPU, HDD ölçümlerini al
        ram_usage = psutil.virtual_memory().percent
        cpu_usage = psutil.cpu_percent()
        hdd_usage = psutil.disk_usage("/").percent

        timestamp = timezone.now()
        formatted_timestamp = timestamp.strftime("%B %d, %Y %H:%M:%S")

        # Network isteklerini logla (burada dummy bir değer kullanıldı)
        network_requests = 15

        # Veritabanına kaydet
        SystemMonitoringData.objects.create(
            timestamp=timestamp,
            ram_usage=ram_usage,
            cpu_usage=cpu_usage,
            hdd_usage=hdd_usage,
            network_requests=network_requests,
        )

        # Son 10 kaydı çekip serialize et ve API yanıtını oluştur
        data = SystemMonitoringData.objects.order_by("-timestamp")[:10]
        serializer = SystemMonitoringDataSerializer(data, many=True)

        # Render işlevi ile template'e verileri iletiyoruz
        return render(
            request,
            "index.html",
            {"data": serializer.data, "formatted_timestamp": formatted_timestamp},
        )
