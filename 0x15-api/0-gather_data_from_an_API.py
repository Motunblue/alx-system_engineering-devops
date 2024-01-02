#!/usr/bin/python3
"""Get information about employee ID
    argv[1]: employee id
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    res = requests.get("{}users/{}".format(url, argv[1]))
    name = res.json().get("name")

    tasks = requests.get(f"{url}todos", params={"userId": argv[1]}).json()
    task_count = len(tasks)
    task_title = [t.get("title") for t in tasks if t.get("completed") is True]
    completed = len(task_title)

    print("Employee {} is done with tasks({}/{}):\n\t".format(
        name, completed, task_count),
        "\n\t ".join(task_title))

