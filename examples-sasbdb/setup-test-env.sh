#!/bin/bash
#
unset ONEDEP_BIOCURATION_API_KEY_PATH
unset ONEDEP_BIOCURATION_API_URL
unset ONEDEP_BIOCURATION_TEST_ENTRY
unset ONEDEP_BIOCURATION_EXTRA_ARGS
unset ONEDEP_API_MOCK_SERVICE
unset ONEDEP_API_MOCK_DURATION

# For Rutgers Development Server - "https://da-devel-1-ann.rcsb.rutgers.edu"
export ONEDEP_BIOCURATION_API_URL="https://da-devel-1-ann.rcsb.rutgers.edu"
export ONEDEP_BIOCURATION_EXTRA_ARGS="--api_url ${ONEDEP_BIOCURATION_API_URL}"
export ONEDEP_BIOCURATION_API_URL="https://da-devel-1-ann.rcsb.rutgers.edu"
export ONEDEP_BIOCURATION_API_KEY_PATH="onedep_biocuration_apikey_sasbdb.jwt"
export ONEDEP_BIOCURATION_TEST_ENTRY_ID="D_800002"
#
#
export ONEDEP_API_MOCK_SERVICE="N"
export ONEDEP_API_MOCK_DURATION=10
#
