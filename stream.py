# streamlit_app.py
import streamlit as st
import requests
import redis

r = redis.Redis(host='localhost', port=6380, db=0)

def send_message(message):
    url = 'http://localhost:5000/send_message'
    data = {'message': message}
    response = requests.post(url, json=data)
    return response.text

def get_task_counts():
    url = 'http://localhost:5000/task_counts'
    response = requests.get(url)
    return response.json()

def main():
    st.title('Message Queue')
    message = st.text_input('Enter a message')
    if st.button('Send'):
        response = send_message(message)
        st.write(response)

    task_counts = get_task_counts()
    pending_tasks = task_counts['pending']
    completed_tasks = task_counts['completed']
    st.write(f'Pending tasks: {pending_tasks}')
    st.write(f'Completed tasks: {completed_tasks}')

if __name__ == '__main__':
    main()