#!/usr/bin/python3
"""Get information about employee ID
    argv[1]: employee id
"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    userId = argv[1]
    res = requests.get("{}users/{}".format(url, userId))
    name = res.json().get("username")

    tasks = requests.get(f"{url}todos", params={"userId": userId}).json()

    with open(f"{userId}.json", mode='w') as f:
        json.dump({userId: [{"task": t.get("title"),
                             "completed": t.get("completed"),
                             "username": name} for t in tasks]}, f)
