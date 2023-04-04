#!/bin/bash
# Take in a URL as an argument sned a get request and display the body of the response
curl -sHG 'X-HolbertonSchool-User-Id: 98' "$1" 
