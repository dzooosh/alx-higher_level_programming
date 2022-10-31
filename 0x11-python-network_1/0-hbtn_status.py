#!/usr/bin/python3
""" fetches alx-intranet.hbtn.io/status site using
urllib request
"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        data = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- ut8 content: {}".format(data.decode('utf-8')))
