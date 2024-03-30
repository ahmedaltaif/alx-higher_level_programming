#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib
if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as respo :
        conntent = respo.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(conntent))
        print("\t- utf8 content: {}".format(body.decode("utf8")))
