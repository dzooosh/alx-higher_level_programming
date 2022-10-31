#!/usr/bin/python3
"""
- takes a URL and email
- sends a POST request to the passed URL with the email as parameters
- displays the body of the response
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode()
    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
