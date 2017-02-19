#!/bin/bash
#
# File:  request-entry-report.sh
# Date:  14-Feb-2017  Jdw
#
#
TS=`/bin/date "+%Y%m%d%H%M%S"`_$$
ONEDEP_BIOCURATION_API_KEY_PATH="onedep_biocuration_apikey_emdb.jwt"
CONTENT_TYPE="report-entry-example-emdb"
ONEDEP_BIOCURATION_TEST_ENTRY_ID="D_800004"
X_ARGS=" --session_file ./.onedep_biocuration_session_${TS} --api_key_file  ${ONEDEP_BIOCURATION_API_KEY_PATH} "
#
# New session  -
#
onedep_request --new_session ${X_ARGS}
#
# Submit request to run service
#
onedep_request --entry_id ${ONEDEP_BIOCURATION_TEST_ENTRY_ID} --entry_content_type ${CONTENT_TYPE}  ${X_ARGS}
#
# Poll for completion status
#
STEP=0
SLEEP=1
while :
do
   STEP=$((STEP + 1))
   PAUSE=$((STEP * STEP * SLEEP))
   echo "[${STEP}] Pausing for ${PAUSE} seconds.   Press CTRL+C to stop..."
   sleep ${PAUSE}
   ST=$(onedep_request --test_complete ${X_ARGS})
   #
   if [ "${ST}" == "1" ]
   then
        break #Abandon the loop.
   fi
done
#
#  Optionally, check the completion status
onedep_request --status ${X_ARGS}
#
#  Optionally, get an index of output report files
onedep_request --index  ${X_ARGS}
#
#  Download report (by file type)
onedep_request --output_file ${ONEDEP_BIOCURATION_TEST_ENTRY_ID}-${CONTENT_TYPE}-${TS}.json  --output_type ${CONTENT_TYPE} ${X_ARGS}
#
#
