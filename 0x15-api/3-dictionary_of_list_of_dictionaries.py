#!/usr/bin/python3
"""Get information about employee ID
    argv[1]: employee id
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get("{}users".format(url)).json()

    dict = {}
    for user in users:
        name = user.get("username")
        id = user.get("id")
        tasks = requests.get(f"{url}todos", params={"userId": id}).json()
        dict[id] = [{"username": name, "task": t.get("title"),
                     "completed": t.get("completed")} for t in tasks]

    with open(f"todo_all_employees.json", mode='w') as f:
        json.dump(dict, f)
