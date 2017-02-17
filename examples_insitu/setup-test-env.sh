#!/bin/bash
# unset  ONEDEP_BIOCURATION_USE_API_KEY
#  For local development platform -
export ONEDEP_BIOCURATION_USE_API_KEY="Y"
export ONEDEP_BIOCURATION_API_URL="https://rtt-ann.mydev"
#export ONEDEP_BIOCURATION_EXTRA_ARGS="--api_url https://rtt-ann.mydev --test_mode --debug"
export ONEDEP_BIOCURATION_EXTRA_ARGS="--api_url https://rtt-ann.mydev --debug "
#
# For Rutgers Development Server - "https://da-devel-1-ann.rcsb.rutgers.edu"
# export ONEDEP_BIOCURATION_EXTRA_ARGS="--api_url https://da-devel-1-ann.rcsb.rutgers.edu --test_mode "
# export ONEDEP_BIOCURATION_API_URL="https://da-devel-1-ann.rcsb.rutgers.edu"
# export ONEDEP_BIOCURATION_API_KEY_PATH="~/.onedep_biocuration_apikey.jwt"
#
# For Production environment
#export ONEDEP_BIOCURATION_EXTRA_ARGS="--api_url https://onedep-apiws-1.wwpdb.org --test_mode "
#
export ONEDEP_BIOCURATION_API_EMAIL="jdwestbrook@gmail.com"
export ONEDEP_API_MOCK_SERVICE="N"
export ONEDEP_API_MOCK_DURATION=10
#
