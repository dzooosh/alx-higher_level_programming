#!/usr/bin/python3
"""
- takes in a URL, sends request to the URL and
- displays the body of the response
- using urllib and sys packages
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: ", end="")
        print(e.code)
