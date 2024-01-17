#!/usr/bin/python3
"""Reddit subreddit API"""
import requests


def top_ten(subreddit):
    """prints the titles of first 10 hot posts listed for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "(Windows NT 10.0; Win64; x64)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(d.get("data").get("title")) for d in results.get("children")]
