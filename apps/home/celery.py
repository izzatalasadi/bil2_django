from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

app = Celery('myapp', broker='pyamqp://guest@localhost//')

@app.task
def run_crawler():
    from .run_crawler import run_crawler
    run_crawler()
    
    

app.conf.beat_schedule = {
    'run-crawler-every-10-minutes': {
        'task': 'run_crawler',
        'schedule': timedelta(minutes=1),
    },
}
