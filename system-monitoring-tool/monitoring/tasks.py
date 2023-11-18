from celery import shared_task
from datetime import datetime
from main import SystemMonitor
from .models import SystemData

@shared_task
def update_system_data():
    cpu_data = SystemData.get_cpu_usage()
    ram_data = SystemData.get_ram_usage()
    hdd_data = SystemData.get_hdd_usage()

    total_ram = SystemData.get_total_ram()
    total_hdd = SystemData.get_total_hdd()

    new_data = SystemData.objects.create(
        cpu_usage=cpu_data["cpu_usage"],
        ram_percent=ram_data["percent"],
        hdd_percent=hdd_data["percent"],
        ram_total=total_ram,
        hdd_total=total_hdd,
    )

    print(f"System data updated: {new_data}")