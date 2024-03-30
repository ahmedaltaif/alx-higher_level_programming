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
    email = sys.argv[2]
    request = urllib.request.Request(url, data=email)
    with urllib.request.urlopen(request) as respo:
        body = respo.read()
        print(body.decode("utf8"))
