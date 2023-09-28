#!/bin/bash
# get the alowable methods
curl -sI "${1}" | grep -iF 'allow' | cut -d ' ' -f2-
