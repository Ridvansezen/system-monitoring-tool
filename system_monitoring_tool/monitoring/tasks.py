from celery import shared_task
from django.utils import timezone
from monitoring.models import SystemMonitoringData
import psutil
from celery import Celery
from pymongo import MongoClient

app = Celery("system_monitoring")
client = MongoClient('mongodb://localhost:27017')
db = client['system_monitoring_tool']
collection = db['monitoring']

@shared_task
def update_system_data():

        timestamp = timezone.now()
        ram_usage = psutil.virtual_memory().percent
        cpu_usage = psutil.cpu_percent()
        hdd_usage = psutil.disk_usage('/').percent
        network_requests = 15  # Dummy değeri, isteğe bağlı

        system_data = SystemMonitoringData.objects.create(
            timestamp=timestamp,
            ram_usage=ram_usage,
            cpu_usage=cpu_usage,
            hdd_usage=hdd_usage,
            network_requests=network_requests,
        )

