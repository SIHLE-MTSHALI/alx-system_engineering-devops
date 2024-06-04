#!/usr/bin/python3
"""Fetches the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    else:
        return 0
