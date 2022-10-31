#!/usr/bin/python3
"""
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response
"""


if __name__ == "__main__":
    import requests
    import sys

    email = sys.argv[2]
    data = {'email': email}
    url = sys.argv[1]
    r = requests.post(url, data=data)
    print(r.text)
