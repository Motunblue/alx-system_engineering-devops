#!/usr/bin/python3
"""Query the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Requery reddit api for number of subscibers"""
    url = "https://www.reddit.com/r/{}/about".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 404:
        return 0
    return response.json().get("data").get("subscribers")
