#!/bin/bash
# sript that sends a request to a URL and display status code
curl -s -o "$1" /dev/null -w '%{http_code}'
