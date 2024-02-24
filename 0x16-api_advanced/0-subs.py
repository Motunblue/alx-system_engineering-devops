#!/usr/bin/python3
"""Query the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Requery reddit api for number of subscibers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/motun)"}
    response = requests.get(url, headers=headers, allow_redirect=False)
    if response.status_code == 404:
        return 0
    result = response.json()
    return result.get("data").get("subscribers")
