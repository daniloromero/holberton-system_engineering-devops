#!/usr/bin/python3
""" returns information about employee TODO list progress"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    try:
        usr_id = argv[1]
        int_check = int(usr_id)
    except ValueError:
        print("Employee id must be an integer")

    usr_url = 'https://jsonplaceholder.typicode.com/users?id=' + usr_id
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + usr_id
    r_usr = requests.get(usr_url)
    r_todo = requests.get(todo_url)
    json_usr = r_usr.json()
    json_todo = r_todo.json()

    if json_usr and json_todo:
        USER_ID = usr_id
        USERNAME = json_usr[0].get('username')

        task_list = []
        for _ in json_todo:
            TASK_COMPLETED_STATUS = _.get('completed')
            TASK_TITLE = _.get('title')
            task_dic = {'task': TASK_TITLE,
                        'completed': TASK_COMPLETED_STATUS,
                        'username': USERNAME}
            task_list.append(task_dic)
        usr_dic = {USER_ID: task_list}

    with open(usr_id + '.json', 'w', newline='') as json_f:
        json.dump(usr_dic, json_f)
