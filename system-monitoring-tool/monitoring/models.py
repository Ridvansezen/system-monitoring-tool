from django.db import models
from mongoengine import Document, fields
import psutil
from datetime import datetime

class SystemData(models.Model):
    cpu_usage = models.FloatField(default=0.0)  
    ram_percent = models.FloatField(default=0.0)
    hdd_percent = models.FloatField(default=0.0)
    ram_total = models.FloatField(default=0.0)
    hdd_total = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(default=datetime.now)

    @staticmethod
    def get_cpu_usage():
        cpu_usage = psutil.cpu_percent(interval=1)
        return {"cpu_usage": cpu_usage}

    @staticmethod
    def get_ram_usage():
        ram = psutil.virtual_memory()
        return {
            "available": ram.available,
            "percent": ram.percent,
            "used": ram.used,
        }
    

    @staticmethod
    def get_total_ram():
        ram = psutil.virtual_memory()
        return ram.total


    @staticmethod
    def get_hdd_usage():
        hdd = psutil.disk_usage("/")
        return {
            "used": hdd.used,
            "free": hdd.free,
            "percent": hdd.percent,
        }
    
    @staticmethod
    def get_total_hdd():
        hdd = psutil.disk_usage("/")
        return hdd.total
