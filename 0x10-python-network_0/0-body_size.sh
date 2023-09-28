#!/usr/bin/env bash
# getting the response body size
curl -sI "${1}" | grep -iF Content-Length | cut -d ' ' -f2
