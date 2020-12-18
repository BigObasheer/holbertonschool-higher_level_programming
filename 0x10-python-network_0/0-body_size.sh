#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size
curl -sI "$@" | grep Content-Length | cut -d" " -f2
