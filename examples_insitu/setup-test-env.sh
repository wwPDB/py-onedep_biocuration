#!/bin/bash
#
unset ONEDEP_BIOCURATION_API_KEY_PATH
unset ONEDEP_BIOCURATION_API_URL
unset ONEDEP_BIOCURATION_TEST_ENTRY
unset ONEDEP_BIOCURATION_EXTRA_ARGS
unset ONEDEP_API_MOCK_SERVICE
unset ONEDEP_API_MOCK_DURATION
#
USE_LOCAL="Y"
if [ ${USE_LOCAL} == "Y" ]
then
    #  For local development platform -
    export ONEDEP_BIOCURATION_API_URL="https://rtt-ann.mydev"
    export ONEDEP_BIOCURATION_TEST_ENTRY_ID="D_1000000001"
    # export ONEDEP_BIOCURATION_EXTRA_ARGS="--api_url https://rtt-ann.mydev --test_mode --debug"
    export ONEDEP_BIOCURATION_API_KEY_PATH="~/.onedep_biocuration_apikey.jwt"
    export ONEDEP_BIOCURATION_EXTRA_ARGS="--api_url https://rtt-ann.mydev "
    #
else
    # For Rutgers Development Server - "https://da-devel-1-ann.rcsb.rutgers.edu"
    export ONEDEP_BIOCURATION_API_URL="https://da-devel-1-ann.rcsb.rutgers.edu"
    export ONEDEP_BIOCURATION_EXTRA_ARGS="--api_url ${ONEDEP_BIOCURATION_API_URL}"
    export ONEDEP_BIOCURATION_API_URL="https://da-devel-1-ann.rcsb.rutgers.edu"
    export ONEDEP_BIOCURATION_API_KEY_PATH="~/.onedep_biocuration_apikey_dev.jwt"
    export ONEDEP_BIOCURATION_TEST_ENTRY_ID="D_800004"
fi
#
#
export ONEDEP_API_MOCK_SERVICE="N"
export ONEDEP_API_MOCK_DURATION=10
#
