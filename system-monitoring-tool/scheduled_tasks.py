from celery import Celery
from celery.schedules import crontab

from main import SystemMonitor


app = Celery("scheduled_tasks", broker="redis://localhost:6379/0")


@app.task
def print_system_monitor():
    print(SystemMonitor.get_cpu_usage())
    print(SystemMonitor.get_ram_usage())
    print(SystemMonitor.get_hdd_usage())


app.conf.beat_schedule = {
    "print-system-monitor": {
        "task": "scheduled_tasks.print_system_monitor",
        "schedule": 10,
    },
}
