#!/usr/bin/python3
"""Get information about employee ID
    argv[1]: employee id
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    res = requests.get("{}users/{}".format(url, argv[1]))
    name = res.json().get("username")

    tasks = requests.get(f"{url}todos", params={"userId": argv[1]}).json()

    with open(f"{argv[1]}.csv", mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [
            writer.writerow(
                [t.get("userId"), name, t.get("completed"), t.get("title")]
                ) for t in tasks
        ]
