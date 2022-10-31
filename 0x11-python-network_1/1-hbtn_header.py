#!/usr/bin/python3
"""
- Takes in a URL and sends a request to the URL
- displays the value of X-Request-Id variable in the header
    of the response
- using urllib and sys
"""


if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.getheader('X-Request-Id'))
