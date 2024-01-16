#!/usr/bin/python3
""" Function that queries the Reddit API and prints
    the top ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """ Queries Reddit API for top ten hot posts of a subreddit """

    # Set user agent in headers
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Set parameters for the API request
    params = {'limit': 10}

    # Construct the API URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    try:
        # Make the API request
        response = requests.get(url, headers=headers, params=params, timeout=5)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Extract the list of hot posts from the JSON response
        data = response.json().get('data', {})
        hot_posts = data.get('children', [])

        if not hot_posts:
            print(f"No hot posts found in subreddit '{subreddit}'.")
        else:
            for post in hot_posts:
                print(post['data']['title'])

    except requests.RequestException as e:
        print(f"Error during API request: {e}")
