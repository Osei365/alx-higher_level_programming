#!/bin/bash
# displays status code alone
curl -s -o /dev/null --write-out "%{http_code}" "${1}"
