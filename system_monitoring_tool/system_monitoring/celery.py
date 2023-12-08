from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system_monitoring.settings")

app = Celery("system_monitoring")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "udpate-system-data": {
        "task": "monitoring.tasks.update_system_data",
        "schedule": timedelta(seconds=5),  
    },

}
