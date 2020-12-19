#!/bin/bash
# sript that sends a request to a URL and display status code
curl -s -o /dev/null -w "%{http_code}" "$1"
