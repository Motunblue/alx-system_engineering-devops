#!/usr/bin/python3
"""query list of all hot posts on a Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], counter=0, after=""):
    """Returns list of titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "(Windows NT 10.0; Win64; x64)"}
    params = {
        "after": after,
        "count": counter,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    for children in results.get("children"):
        hot_list.append(children.get("data").get("title"))
    after = results.get("after")
    counter += results.get("dist")

    if after is not None:
        return recurse(subreddit, hot_list, counter, after)
    return hot_list
