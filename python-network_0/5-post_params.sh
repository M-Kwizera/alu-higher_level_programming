#!/bin/bash
# Takes in a URL sends a POST request to passed in URL displays the body of the response
curl -sHX -d "email=test@gmail.com&subject=I will always be here for PLD" POST "$1"
