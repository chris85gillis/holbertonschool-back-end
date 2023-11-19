#!/usr/bin/python3
"""import"""
import csv
import requests
import sys


def get_employee_todo_progress(USER_ID):
    """constructing URLs for user and todos data"""
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{USER_ID}'
    todos_url = f'{base_url}todos?userId={USER_ID}'

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    """Extract relevant data"""
    task_records = []
    for task in todos_data:
        task_record = {
            "USER_ID": USER_ID,
            "USERNAME": employee_name,
            "TASK_COMPLETED_STATUS": task['completed'],
            "TASK_TITLE": task['title']
        }
        task_records.append(task_record)

    return task_records

def write_to_csv(task_records, csv_file_name):
    with open(csv_file_name, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writerows(task_records)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <USER_ID>")
        sys.exit(1)

    USER_ID = int(sys.argv[1])
    task_records = get_employee_todo_progress(USER_ID)

    # Specify a CSV file name (e.g., using the employee's username or a combination)
    csv_file_name = f"{USER_ID}.csv"
    write_to_csv(task_records, csv_file_name)
