#!/bin/bash
# takes in a URL, sends a POST request and displays the body of the response
curl -sd "subject=I will always be here for PLD&email=test@gmail.com" $1
