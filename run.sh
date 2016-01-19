#!/bin/bash

# $1 is api_key
# $2 is applicaiton_id
# $3 is metric_name

docker run -v "$(pwd)/scripts:/scripts" -it --rm=true newrelic-parser scripts/parse.py metric_data $1 $2 $3
