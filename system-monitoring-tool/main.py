import psutil


class SystemMonitor:
    @staticmethod
    def get_cpu_usage():
        cpu_usage = psutil.cpu_percent(interval=1)

        return {
            "cpu_usage": cpu_usage,
        }

    @staticmethod
    def get_ram_usage():
        ram = psutil.virtual_memory()

        return {
            "total": ram.total,
            "available": ram.available,
            "percent": ram.percent,
            "used": ram.used,
        }

    @staticmethod
    def get_hdd_usage():
        hdd = psutil.disk_usage("/")

        return {
            "total": hdd.total,
            "used": hdd.used,
            "free": hdd.free,
            "percent": hdd.percent,
        }
