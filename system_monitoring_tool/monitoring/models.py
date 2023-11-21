from django.db import models


class SystemMonitoringData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ram_usage = models.FloatField(default=0.0)
    cpu_usage = models.FloatField(default=0.0)
    hdd_usage = models.FloatField(default=0.0)
    network_requests = models.IntegerField()

    class Meta:
        ordering = ["-timestamp"]
