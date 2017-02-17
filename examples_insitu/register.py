# -*- coding: utf-8 -*-
"""
register.py <email>
^^^^^^^^^^

Example of wwPDB OneDep API Registration service -

:copyright: @wwPDB
:license: Apache 2.0
"""
from __future__ import absolute_import, print_function
import os
import sys

try:
    from onedep_biocuration import __apiUrl__
except:
    here = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.dirname(here))

    from onedep_biocuration import __apiUrl__

from onedep_biocuration.api.Register import Register


def print_(s):
    sys.stdout.write(s)


def register(argv):
    """ Example of OneDep API Registration service.

        First input argument is the email address of the API key requester.

    """
    if len(argv) < 2:
        pn = argv[0]
        print_("Usage: %s <email>\n" % pn)
        raise SystemExit()
    #
    email = argv[1]
    apiUrl = os.getenv("ONEDEP_BIOCURATION_API_URL") if os.getenv("ONEDEP_BIOCURATION_API_URL") else __apiUrl__
    reg = Register(apiUrl=apiUrl)
    sD = reg.register(email=email)
    if 'onedep_error_flag' in sD and sD['onedep_error_flag']:
        print_("OneDep error: %s\n" % sD['onedep_status_text'])
        raise SystemExit()
    else:
        print_("A OneDep API access key will be sent to %s.\n  Copy the key in the email attachment to %s\n" % (email, os.path.expanduser("~/.onedep_biocuration_apikey.jwt")))


if __name__ == '__main__':
    register(sys.argv)
