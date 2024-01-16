#!/usr/bin/python3
""" Function that queries the Reddit API and prints
    the top ten hot posts of a subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    """Recursively retrieves hot article titles for a given subreddit."""
    usr_agent = 'Mozilla/5.0'
    headers = {'User-Agent': usr_agent}
    params = {'limit': 100}  # Adjust limit as needed
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(f"Invalid subreddit or unable to fetch data. Status code: {response.status_code}")
            return None

        response.raise_for_status()

        data = response.json().get('data', {})
        hot_posts = data.get('children', [])

        if hot_posts:
            hot_list.extend(post['data']['title'] for post in hot_posts)

        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list)
        else:
            return hot_list if hot_list else None

    except requests.RequestException as e:
        print(f"Error during API request: {e}")
        return None
