#!/usr/bin/python3
"""
Script that fetches employee TODO list progress from an API and exports to JSON
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url_user = ("https://jsonplaceholder.typicode.com/users/"
                "{}".format(employee_id))
    url_todos = ("https://jsonplaceholder.typicode.com/users/"
                 "{}/todos".format(employee_id))

    user = requests.get(url_user).json()
    todos = requests.get(url_todos).json()

    username = user.get('username')
    tasks = [{"task": todo.get('title'), "completed": todo.get('completed'),
              "username": username} for todo in todos]
    data = {employee_id: tasks}

    filename = f"{employee_id}.json"
    with open(filename, mode='w') as file:
        json.dump(data, file)
