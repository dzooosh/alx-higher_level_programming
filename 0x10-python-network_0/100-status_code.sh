#!/bin/bash
# sends a request to a URL passed as an arg, displays only the status code of the response
curl -s -o /dev/null -I -w %"{http_code}" $1
