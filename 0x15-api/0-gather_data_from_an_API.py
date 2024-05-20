#!/usr/bin/python3
"""
Script that fetches employee TODO list progress from an API
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url_user = ("https://jsonplaceholder.typicode.com/users/"
                "{}".format(employee_id))
    url_todos = ("https://jsonplaceholder.typicode.com/users/"
                 "{}/todos".format(employee_id))

    user = requests.get(url_user).json()
    todos = requests.get(url_todos).json()

    employee_name = user.get('name')
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get('completed')]
    done_tasks_titles = [todo.get('title') for todo in done_tasks]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/"
          f"{total_tasks}):")
    for title in done_tasks_titles:
        print(f"\t {title}")
