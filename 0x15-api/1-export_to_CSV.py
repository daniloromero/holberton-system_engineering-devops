#!/usr/bin/python3
""" returns information about employee TODO list progress"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    try:
        usr_id = argv[1]
        int_check = int(usr_id)
    except ValueError:
        print("Employee id must be and integer")

    usr_url = 'https://jsonplaceholder.typicode.com/users?id=' + usr_id
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + usr_id
    r_usr = requests.get(usr_url)
    r_todo = requests.get(todo_url)
    json_usr = r_usr.json()
    json_todo = r_todo.json()
    print(json_usr[0].get('username'))

    if json_usr and json_todo:
        USER_ID = usr_id
        USERNAME = json_usr[0].get('username')

    with open(usr_id + '.csv', 'w', newline='') as csv_f:
        spamwriter = csv.writer(csv_f, quoting=csv.QUOTE_ALL)

        for _ in json_todo:
            TASK_COMPLETED_STATUS = _.get('completed')
            TASK_TITLE = _.get('title')
            spamwriter.writerow([USER_ID, USERNAME,
                                TASK_COMPLETED_STATUS, TASK_TITLE])
