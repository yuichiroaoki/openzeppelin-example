#!/bin/sh
# run slither
curl http://localhost:8000/human-summary/{filename}

# get whole json data
curl http://localhost:8000/data/sample/json

# get description
curl http://localhost:8000/data/sample/json?description=True

# get summary
curl http://localhost:8000/data/sample/json?other=number_findings
