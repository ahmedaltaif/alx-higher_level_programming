#!/usr/bin/python3
"""
    a Python script that takes in a URL, sends a request
    to the URL and displays the value of the X-Request-Id
    variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as respo:
        content = respo.read()
        print(dict(respo.headers).get("X-Request-Id"))
