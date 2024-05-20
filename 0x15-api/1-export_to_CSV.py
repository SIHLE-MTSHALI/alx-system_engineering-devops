#!/usr/bin/python3
"""
Script that fetches employee TODO list progress from an API and exports to CSV
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url_user = ("https://jsonplaceholder.typicode.com/users/"
                "{}".format(employee_id))
    url_todos = ("https://jsonplaceholder.typicode.com/users/"
                 "{}/todos".format(employee_id))

    user = requests.get(url_user).json()
    todos = requests.get(url_todos).json()

    username = user.get('username')
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, username, todo.get('completed'),
                             todo.get('title')])
