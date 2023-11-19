#!/usr/bin/python3
"""import"""
import csv
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

    """Extract relevant data"""
    task_records = []
    for task in todos_data:
        task_record = {
            "USER_ID": employee_id,
            "USERNAME": employee_name,
            "TASK_COMPLETED_STATUS": task['completed'],
            "TASK_TITLE": task['title']
        }
        task_records.append(task_record)

    """Write to CSV"""
    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(task_records)

    with open(csv_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            print(row)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
