#!/bin/bash
# Takes in a URL and sends a DELETE request to passed in URL
curl -s -X DELETE "$1"
