#!/bin/bash
#Bash scripts for sending POST requests to specified URLs.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
