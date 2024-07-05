#!/bin/bash
# Show all HTTP methods that the server at a specified URL will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
