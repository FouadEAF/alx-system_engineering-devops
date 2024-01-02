#!/usr/bin/python3
""" Script that use JSONPlaceholder API to get information about employees
    and export data in JSON format
"""
import json
import requests


def export_all_to_json():
    url = 'https://jsonplaceholder.typicode.com/'
    all_users_url = f'{url}users'

    all_users_data = requests.get(all_users_url).json()

    all_data = {}

    for user_data in all_users_data:
        user_id = user_data['id']
        username = user_data['username']

        todos_url = f'{url}todos?userId={user_id}'
        tasks_data = requests.get(todos_url).json()

        user_tasks = []

        for task in tasks_data:
            user_tasks.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        all_data[user_id] = user_tasks

    # Export data to JSON file
    output_file_name = 'todo_all_employees.json'

    with open(output_file_name, 'w') as json_file:
        json.dump(all_data, json_file, indent=2)

    print("Data for all employees exported to {}".format(output_file_name))


if __name__ == "__main__":
    export_all_to_json()
