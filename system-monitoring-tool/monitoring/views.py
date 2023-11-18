from datetime import datetime
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import SystemData
from main import SystemMonitor

import logging

logger = logging.getLogger(__name__)

def SystemDataView(request):
    cpu_data = SystemData.get_cpu_usage()
    ram_data = SystemData.get_ram_usage()
    ram_total = SystemData.get_total_ram()
    hdd_data = SystemData.get_hdd_usage()
    total_hdd = SystemData.get_total_hdd()

    new_data = SystemData.objects.create(
        cpu_usage=cpu_data["cpu_usage"],
        ram_percent=ram_data["percent"],
        hdd_percent=hdd_data["percent"],
        ram_total=ram_total,
        hdd_total=total_hdd,
    )


    logger.info(f"System data logged: {new_data}")


    latest_data = SystemData.objects.latest('timestamp')

    return render(request, 'index.html', {'latest_data': latest_data})