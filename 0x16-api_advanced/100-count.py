#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests
from collections import Counter

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = Counter()

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get("data")
    after = data.get("after")

    for child in data.get("children"):
        title = child.get("data").get("title").lower()
        words = title.split()

        for word in word_list:
            if word.lower() in words:
                counts[word.lower()] += 1

    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")

# Example usage
count_words("programming", ["python", "java", "javascript"])
