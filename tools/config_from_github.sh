#!/bin/bash

set -e
set -o pipefail

USER=users/dnephin
PER_PAGE=300
URL=https://api.github.com/$USER/repos?per_page=$PER_PAGE

curl -s $URL | jq -r '.[].full_name' | ./tools/build_config.py
