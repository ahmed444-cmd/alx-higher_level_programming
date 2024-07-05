#!/bin/bash
# Retrieve the size(bytes) of the HTTP response header for a specified URL.
curl -s "$1" | wc -c
