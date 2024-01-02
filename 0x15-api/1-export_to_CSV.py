#!/usr/bin/python3
""" Script that use JSONPlaceholder API to get information about employee """
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    idUser = sys.argv[1]
    user = '{}users/{}'.format(url, idUser)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?idUser={}'.format(url, idUser)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        l_task.append([idUser,
                       name,
                       task.get('completed'),
                       task.get('title')])

    filename = '{}.csv'.format(idUser)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in l_task:
            employee_writer.writerow(task)
