#!/usr/bin/python3
""" fetches alx-intranet.hbtn.io/status site using
urllib request
"""

if __name__ == "__main__":
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        utf8 = data.decode("UTF-8")
        print("\t- ut8 content: {}".format(utf8))
