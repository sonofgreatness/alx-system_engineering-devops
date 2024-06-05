#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Define the URL of the subreddit
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set the headers to include a custom User-Agent
    headers = {"User-Agent": "get_number_of_subscribersv1.0"}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response and return the number of subscribers
        print("Ok")
        return response.json()["data"]["subscribers"]
    else:
        print("Not Ok")
        # If the subreddit is not valid, return 0
        return 0
