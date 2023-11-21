from celery import shared_task


@shared_task
def your_task_function():
    # Your task logic goes here
    print("Scheduled task executed!")
