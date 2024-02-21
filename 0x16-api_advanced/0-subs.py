#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    subreddit: A string representing the subreddit name.
    
    Returns:
        The number of subscribers if the subreddit is valid, otherwise 0.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    try:
        response = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                                headers={'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'})
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    except (requests.RequestException, ValueError):
        return 0
