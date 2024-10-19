from celery import Celery
from celery.schedules import crontab

app = Celery('simpleapp')

app.conf.beat_schedule = {
    'send-weekly-posts': {
        'task': 'simpleapp.tasks.send_weekly_posts',
        'schedule': crontab(day_of_week=0, hour=0, minute=0),
    },
}
