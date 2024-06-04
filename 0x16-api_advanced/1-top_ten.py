#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            posts = data.get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
