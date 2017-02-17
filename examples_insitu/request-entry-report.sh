#!/bin/bash
#
# File:  request-entry-report.sh
# Date:  14-Feb-2017  Jdw
#
SLEEP=2
THISDIR="$( builtin cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TD=$(dirname ${THISDIR})
#
# Handle optional arguments from the environment and add a unique session file
TS=`/bin/date "+%Y%m%d%H%M%S"`_$$
if [  -n "${ONEDEP_BIOCURATION_EXTRA_ARGS}" ]
then
    X_ARGS="${ONEDEP_BIOCURATION_EXTRA_ARGS} --session_file ./.onedep_biocuration_session_${TS} "
else
    X_ARGS=" --session_file ./.onedep_biocuration_session_${TS} "
fi
#
# New session  -
#
${TD}/bin/onedep_request --new_session ${X_ARGS}
#
# Submit request to run service
#
${TD}/bin/onedep_request --entry_id D_1000000001 --entry_content_type "report-entry-example-test"  ${X_ARGS}
#
# Poll for completion status
#
STEP=0
while :
do
   STEP=$((STEP + 1))
   PAUSE=$((STEP * STEP * SLEEP))
   echo "[${STEP}] Pausing for ${PAUSE} seconds.   Press CTRL+C to stop..."
   sleep ${PAUSE}
   ST=$(${TD}/bin/onedep_request --test_complete ${X_ARGS})
   #
   if [ "${ST}" == "1" ]
   then
        break #Abandon the loop.
   fi
done
#
#  Optionally, check the completion status
${TD}/bin/onedep_request --status ${X_ARGS}
#
#  Get an index of output report files
${TD}/bin/onedep_request --index  ${X_ARGS}
#
#  Download report (by file type)
${TD}/bin/onedep_request --output_file D_1000000001-report-entry-example-test-${TS}.json  --output_type "report-entry-example-test" ${X_ARGS}
#
#  Get a summary of service activity -
# ${TD}/bin/onedep_request --activity ${X_ARGS}
#
