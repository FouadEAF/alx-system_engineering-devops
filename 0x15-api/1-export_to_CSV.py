#!/usr/bin/python3
""" Script that use JSONPlaceholder API to get information about employee
    and export data in CSV format
"""
import csv
import requests
import sys


def get_user_data(user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    return response.json()


def get_user_tasks(user_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)
    return response.json()


def export_to_csv(user_id, user_data, tasks_data):
    csv_output_file = '{}.csv'.format(user_id)

    with open(csv_output_file, 'w', newline='') as csv_file:
        fieldnames = ["task", "completed", "username"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks_data:
            writer.writerow({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_data.get("username")
            })

    print("Data exported to {}".format(csv_output_file))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    user_data = get_user_data(user_id)
    tasks_data = get_user_tasks(user_id)

    export_to_csv(user_id, user_data, tasks_data)
