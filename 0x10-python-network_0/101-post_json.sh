#!/bin/bash
# Send a JSON POST request to a specified URL, including a provided JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
