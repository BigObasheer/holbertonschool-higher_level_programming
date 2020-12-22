#!/bin/bash
# Server to respond with a message containing You got me
curl -sL 0.0.0.0:5000/catch_me -X PUT -F 'user_id=98' -H 'Origin: HolbertonSchool'
