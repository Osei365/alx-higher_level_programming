#!/bin/bash
# send get request with additional header
curl -s -H "X-School-User-Id: 98" "${1}"
