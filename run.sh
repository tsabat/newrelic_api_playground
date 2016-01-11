#!/bin/bash

# $1 is applicaiton_id
# $2 is api_key

docker run -v "$(pwd)/scripts:/scripts" -it --rm=true newrelic-parser scripts/parse.py metric_data application_key api_key
