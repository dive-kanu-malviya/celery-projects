# tasks.py
import time
from celery import Celery
import redis

app = Celery('tasks', broker='redis://localhost:6379/0')
r = redis.Redis(host='localhost', port=6380, db=0)

@app.task
def process_message(message):
    time.sleep(5)  # Simulate a time-consuming task
    r.rpush('completed_tasks', message)
    r.lrem('pending_tasks', 0, message)