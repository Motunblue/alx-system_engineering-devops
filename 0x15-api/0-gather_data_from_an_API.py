#!/usr/bin/python3
"""Get information about employee ID"""
from sys import argv
import requests


url = "https://jsonplaceholder.typicode.com/"

res = requests.get("{}users/{}".format(url, argv[1]))
name = res.json().get("name")

res = requests.get("{}todos/".format(url))
tasks = res.json()
task_count = 0
completed = 0
task_title = []
for task in tasks:
    if task.get("userId") == int(argv[1]):
        task_count += 1
        if task.get("completed") is True:
            completed += 1
            task_title.append(task.get("title"))

print("Employee {} is done with tasks({}/{}):\n\t".format(
    name, completed, task_count),
      "\n\t ".join(task_title))
