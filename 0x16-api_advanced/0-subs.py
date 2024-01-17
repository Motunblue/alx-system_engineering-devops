#!/usr/bin/python3
"""Query the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Requery reddit api for number of subscibers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)
    if response.status_code == 404:
        return 0
    result = response.json()
    return result.get("data").get("subscribers")
