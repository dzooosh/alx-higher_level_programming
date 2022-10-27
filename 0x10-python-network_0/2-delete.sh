#!/bin/bash
# sends a DELETE request to the URL passed and displays the body of res
curl -s $1 -X DELETE
