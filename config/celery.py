import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "run_movie_rating_avg_every_30": {
        "task": "task_update_movie_ratings",
        "schedule": 60 * 30,  # 30 min,
    },
    "daily_rating_dataset_export": {
        "task": "export_rating_dataset",
        "schedule": crontab(hour=1, minute=30),
    },
}
