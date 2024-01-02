#!/usr/bin/python3
""" Script that use JSONPlaceholder API to get information about employee
    and export data in JSON format
"""
import json
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


def export_to_json(user_id, user_data, tasks_data):
    user_tasks = []

    for task in tasks_data:
        user_tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_data.get("username")
        })

    output_data = {user_id: user_tasks}

    # Export data to JSON file
    output_file_name = '{}.json'.format(user_id)

    with open(output_file_name, 'w') as json_file:
        json.dump(output_data, json_file, indent=2)

    print("Data exported to {}".format(output_file_name))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    user_data = get_user_data(user_id)
    tasks_data = get_user_tasks(user_id)

    export_to_json(user_id, user_data, tasks_data)
