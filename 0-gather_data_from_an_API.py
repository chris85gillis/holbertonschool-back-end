#!/usr/bin/python3
"""import"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """constructing URLs for user and todos data"""
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{employee_id}'
    todos_url = f'{base_url}todos?userId={employee_id}'

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks(", end="")
    print(f"{num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
