#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request to the URL
 and displays the body of the response (decoded in utf-8).
"""
from urllib import request, error
import sys.argv

if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(request) as respo:
            print(respo.read().decode('UTF-8'))
    except error.HTTPError as erro:
        print("Error code:", erro.code)
