#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    respond = requests.get(url)
    data = respond.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                data[i].get("sha"),
                data[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
