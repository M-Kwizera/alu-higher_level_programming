#!/bin/bash
# Display all methods a SERVER will accept
curl -siX OPTIONS "$1" | grep "Allow: " | cut -c 8-
