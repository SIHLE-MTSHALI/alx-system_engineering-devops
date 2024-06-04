#!/usr/bin/python3
"""
This module contains the function recurse.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Python/requests'}
    params = {'after': after, 'limit': 100}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    if not data:
        return None
    after = data.get('after')
    children = data.get('children')
    if not children:
        return hot_list
    for child in children:
        hot_list.append(child.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
