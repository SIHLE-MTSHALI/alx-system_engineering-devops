#!/usr/bin/python3
"""
Script that fetches TODO list progress of all employees from an API and
exports to JSON
"""
import json
import requests

if __name__ == "__main__":
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(url_users).json()
    todos = requests.get(url_todos).json()

    data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_todos = [todo for todo in todos if todo.get('userId') == user_id]
        tasks = [{"task": todo.get('title'), "completed": todo.get('completed'),
                  "username": username} for todo in user_todos]
        data[user_id] = tasks

    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(data, file)
