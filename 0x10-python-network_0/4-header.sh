#!/bin/bash
# takes in a URL as an arg, sends a GET request with a custom header and displays the body of the res
curl -H "X-School-User-Id: 98;" $1 -X GET
