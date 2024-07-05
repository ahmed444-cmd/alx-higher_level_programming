#!/bin/bash
# Make a GET request to a specified URL while including a header variable.
curl -sH "X-School-User-Id: 98" "${1}"
