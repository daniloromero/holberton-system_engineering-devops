#!/usr/bin/python3
""" returns information about employee TODO list progress"""
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
        EMPLOYEE_NAME = json_usr[0].get('name')
        TOTAL_NUMBER_OF_TASKS = len(json_todo)
        NUMBER_OF_DONE_TASKS = sum(map(lambda x:
                                   x.get('completed'), json_todo))

    print('Employee {} is done with tasks({}/{}):'.
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for _ in json_todo:
        TASK_TITLE = _.get('title')
        if _.get('completed'):
            print('\t {}'.format(TASK_TITLE))
