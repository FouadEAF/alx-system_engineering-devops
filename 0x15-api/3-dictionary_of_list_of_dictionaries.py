#!/usr/bin/python3
""" Script that use JSONPlaceholder API to get information about employees
    and export data in JSON format
"""
import json
import requests
import sys


def export_all_to_json():
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    res = requests.get(user)
    json_o = res.json()
    d_task = {}
    for user in json_o:
        name = user.get('username')
        idUser = user.get('id')
        todos = '{}todos?userId={}'.format(url, idUser)
        res = requests.get(todos)
        tasks = res.json()
        l_task = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            l_task.append(dict_task)

        d_task[str(idUser)] = l_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(d_task, f)


if __name__ == "__main__":
    export_all_to_json()
