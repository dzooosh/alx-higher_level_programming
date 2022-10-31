#!/usr/bin/python3
"""
- takes in a URL, sends a request to the URL
- displays the value of the variable X-Request-Id in the response header
- using sys and requests package
"""


if __name__ == "__main__":
    import sys
    import requests

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
