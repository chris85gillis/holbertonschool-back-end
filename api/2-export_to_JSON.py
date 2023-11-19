#!/usr/bin/python3
"""Retrieve and export employee's tasks in JSON format"""

import requests
import sys
import json


def get_user_data(employee_id, base_url='https://jsonplaceholder.typicode.com/'):
    """Retrieve user data from the API"""
    user_url = f'{base_url}users/{employee_id}'
    response = requests.get(user_url)

    if response.status_code != 200:
        print(f"Failed to retrieve user data. Status code: {response.status_code}")
        sys.exit(1)

    return response.json()


def get_todos_data(employee_id, base_url='https://jsonplaceholder.typicode.com/'):
    """Retrieve todos data for a specific employee from the API"""
    todos_url = f'{base_url}todos?userId={employee_id}'
    response = requests.get(todos_url)

    if response.status_code != 200:
        print(f"Failed to retrieve todos data. Status code: {response.status_code}")
        sys.exit(1)

    return response.json()


def export_to_json(employee_id, tasks):
    """Export tasks to a JSON file"""
    filename = f'{employee_id}.json'
    with open(filename, 'w') as file:
        json.dump({str(employee_id): tasks}, file)


def print_progress_report(employee_name, num_completed_tasks, total_tasks, completed_tasks):
    """Print the progress report"""
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['task']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_data = get_user_data(employee_id)
    employee_name = user_data.get('name')

    todos_data = get_todos_data(employee_id)

    total_tasks = len(todos_data)
    completed_tasks = [
        {"task": task.get("title", "N/A"), "completed": task["completed"], "username": employee_name}
        for task in todos_data
    ]
    num_completed_tasks = len(completed_tasks)

    print_progress_report(employee_name, num_completed_tasks, total_tasks, completed_tasks)
    export_to_json(employee_id, completed_tasks)
