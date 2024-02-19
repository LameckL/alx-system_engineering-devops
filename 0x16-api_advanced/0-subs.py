#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if not subreddit or not isinstance(subreddit, str):
        return 0
    try:
        response = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                                headers={'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'})
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    except requests.RequestException:
        return 0

