#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as respo:
        conntent = respo.read()
        print("Body response:")
        print("\t- type: {}".format(type(conntent)))
        print("\t- content: {}".format(conntent))
        print("\t- utf8 content: {}".format(conntent.decode("utf8")))
