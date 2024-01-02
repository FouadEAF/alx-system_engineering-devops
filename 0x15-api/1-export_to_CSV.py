#!/usr/bin/python3
""" Script that use JSONPlaceholder API to get information about employee
    and export data in CSV format
"""
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

    todos = '{}todos?userId={}'.format(url, idUser)  # Corrected the parameter name to 'userId'
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        l_task.append([idUser,
                       name,
                       task.get('completed'),
                       task.get('title')])

    filename = '{}.csv'.format(idUser)
    with open(filename, mode='w', newline='') as employee_file:  # Added 'newline=' argument
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)  # Changed to QUOTE_MINIMAL
        # Write header
        employee_writer.writerow(['UserID', 'Username', 'Completed', 'Title'])
        
        for task in l_task:
            employee_writer.writerow(task)
