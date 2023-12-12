from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system_monitoring_tool.settings")

app = Celery("system_monitoring_tool")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "your-task-name": {
        "task": "monitoring.tasks.your_task_function",
        "schedule": timedelta(seconds=5),  # Adjust the schedule as needed
    },
    # Add more tasks as needed
}
