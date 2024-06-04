#!/usr/bin/python3
"""
This module contains the function count_words.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Python/requests'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get('data')
    if not data:
        return

    after = data.get('after')
    children = data.get('children')
    if not children:
        return

    for child in children:
        title = child.get('data').get('title').lower().split()
        for word in word_list:
            word_count[word.lower()] = word_count.get(word.lower(), 0) + title.count(word.lower())

    if after is not None:
        return count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print("{}: {}".format(word, count))
