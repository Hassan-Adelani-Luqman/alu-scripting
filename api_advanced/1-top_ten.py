#!/usr/bin/python3
"""
A module that prints the titles of the top
10 hot posts from a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Fetches and prints the titles of the top ten hot posts from a subreddit.
    If the subreddit is invalid or there are no hot posts, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {}).get("children", [])
        if not data:
            print(None)
            return

        for post in data:
            print(post["data"]["title"])

    except requests.RequestException:
        print(None)
