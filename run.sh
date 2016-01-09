#!/bin/bash

docker run -v "$(pwd)/stuff:/stuff" -it --rm=true python-json bash
