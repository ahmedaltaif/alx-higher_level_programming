#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    request = requests.get("https://alx-intranet.hbtn.io/status")
    print ("Body response:")
    print ("\t- type: {}".format(type(request)))
    print ("\t- type: {}".format(request))
