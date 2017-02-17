# -*- coding: utf-8 -*-
"""
content-summary-request.py <request_content_type> <output_file>
^^^^^^^^^^

Example of wwPDB OneDep Biocuration API summary content service -

:copyright: @wwPDB
:license: Apache 2.0
"""
from __future__ import absolute_import, print_function
import os
import sys
import time

# Configure logging -
if False:
    import logging
    logging.captureWarnings(True)
    logging.basicConfig(format='%(asctime)s [%(levelname)s]-%(module)s.%(funcName)s: %(message)s')
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

HERE = os.path.abspath(os.path.dirname(__file__))

try:
    from onedep_biocuration import __apiUrl__
except:
    sys.path.insert(0, os.path.dirname(HERE))
    from onedep_biocuration import __apiUrl__

from onedep_biocuration.api.ContentRequest import ContentRequest


def print_(s):
    sys.stdout.write(s)


def readApiKey(filePath):
    apiKey = None
    try:
        fn = os.path.expanduser(filePath)
        with open(fn, 'r') as fp:
            apiKey = fp.read()
    except:
        pass
    return apiKey


def displayStatus(sD, exitOnError=True):
    if 'onedep_error_flag' in sD and sD['onedep_error_flag']:
        print_("OneDep error: %s\n" % sD['onedep_status_text'])
        if exitOnError:
            raise SystemExit()
    else:
        if 'status' in sD:
            print_("OneDep status: %s\n" % sD['status'])


def displayIndex(sD):
    #
    print_("\nSession File Index:\n")
    try:
        if 'index' in sD and len(sD) > 0:
            print_("%50s : %-25s\n" % (" File name  ", "      Format     "))
            print_("%50s : %-25s\n" % ("------------", "-----------------"))
            for ky in sD['index']:
                fn, fmt = sD['index'][ky]
                print_("%50s : %-25s\n" % (fn, fmt))
        else:
            print_("No index content\n")
    except:
        print_("Error processing session index")


def requestSummaryContent(requestContentType, requestFormatType, resultFilePath):
    """ Example of OneDep API summary content request.

        :param string requestContentType : the request content type
        :param string requestFormatType :  the request format type
        :param string resultFilePaht :  result file path for the requested content

    """
    #
    print_("Example content request service for content type %s\n" % (requestContentType))
    #
    USEKEY = os.getenv("ONEDEP_BIOCURATION_USE_API_KEY") if os.getenv("ONEDEP_BIOCURATION_USE_API_KEY") else False
    # Flag for mock service for testing -
    mockService = True if os.getenv("ONEDEP_API_MOCK_SERVICE") == "Y" else False
    #
    # Check for alternative URL and KEY settings in the environment -
    #
    apiUrl = os.getenv("ONEDEP_BIOCURATION_API_URL") if os.getenv("ONEDEP_BIOCURATION_API_URL") else __apiUrl__
    if (USEKEY):
        keyFilePath = os.getenv("ONEDEP_BIOCURATION_API_KEY_PATH") if os.getenv("ONEDEP_BIOCURATION_API_KEY_PATH") else "~/.onedep_biocuration_apikey.jwt"
        apiKey = readApiKey(keyFilePath)
        cr = ContentRequest(apiKey=apiKey, apiUrl=apiUrl)
    else:
        cr = ContentRequest(apiUrl=apiUrl)
    #
    # Create a new service session -
    #
    print_("Creating new session for content request example\n")
    rD = cr.newSession()
    displayStatus(rD)
    #
    #
    print_("Request content type %s\n" % (requestContentType))
    #
    # Submit service request
    if mockService:
        pD = {}
        pD['worker_test_mode'] = True
        pD['worker_test_duration'] = int(os.getenv("ONEDEP_API_MOCK_DURATION"))
        print_("Using mock service setup %r\n" % pD)
        rD = cr.requestSummaryContent(requestContentType, requestFormatType, **pD)
    else:
        print_("Submitted content service request\n")
        rD = cr.requestSummaryContent(requestContentType, requestFormatType)
    displayStatus(rD)
    #
    #   Poll for service completion -
    #
    it = 0
    sl = 2
    while (True):
        #    Pause -
        it += 1
        pause = it * it * sl
        time.sleep(pause)
        rD = cr.getStatus()
        if rD['status'] in ['completed', 'failed']:
            break
        print_("[%4d] Pausing for %4d (seconds)\n" % (it, pause))
        #
    #
    print_("Storing content type %s  in result file %s\n" % (requestContentType, resultFilePath))
    rD = cr.getOutputByType(resultFilePath, requestContentType, formatType=requestFormatType)
    displayStatus(rD)
    #
    iD = cr.getIndex()
    displayIndex(iD)
    #
    print_("Completed\n")


if __name__ == '__main__':

    if len(sys.argv) < 4:
        # Use test case if no arguments are provided -
        requestContentType = "report-summary-example-test"
        requestFormatType = 'json'
        resultFileName = requestContentType + '.' + requestFormatType
    else:
        requestContentType = sys.argv[1]
        resultFileName = sys.arg[2]
        requestFormatType = 'json'
    #
    requestSummaryContent(requestContentType, requestFormatType, resultFileName)
