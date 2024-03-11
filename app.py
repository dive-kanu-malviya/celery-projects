# app.py
from flask import Flask, request, jsonify
from task import process_message
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6380, db=0)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json['message']
    r.rpush('pending_tasks', message)
    process_message.delay(message)
    return 'Message received and queued for processing'

@app.route('/task_counts', methods=['GET'])
def get_task_counts():
    pending_tasks = r.llen('pending_tasks')
    completed_tasks = r.llen('completed_tasks')
    return jsonify({'pending': pending_tasks, 'completed': completed_tasks})

if __name__ == '__main__':
    app.run(debug=True)