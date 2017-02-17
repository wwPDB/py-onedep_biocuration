# -*- coding: utf-8 -*-
"""
Register.py
^^^^^^^^^^

API for OneDep Biocuration Web Service Registration

:copyright: @wwPDB
:license: Apache 2.0, see LICENSE file for more details.


Updates:
    21-Sep-2016  jdw  adapted for the onedep tree package -
    13-Feb-2017  jdw  adapted for the onedep biocuration package -

"""
# from __future__ import print_function
from __future__ import unicode_literals
# from __future__ import division
#
__docformat__ = "restructuredtext en"
__author__ = "John Westbrook"
__email__ = "jwest@rcsb.rutgers.edu"
__license__ = "Apache 2.0"

import logging
import sys

from onedep_biocuration import __version__
from onedep_biocuration import __apiUrl__


from onedep_biocuration.utils.ApiBase import ApiBase

log = logging.getLogger(__name__)


class Register(ApiBase):

    def __init__(self, apiUrl=None):
        """
        OneDep webservice registration client API

        :param string apiUrl: (Optional) alternative API server URL.


        """
        apiUrl = apiUrl if apiUrl else __apiUrl__
        apiKey = None
        userAgent = 'OneDepBiocurationClient/%s Python/%s ' % (__version__, sys.version.split()[0])
        apiName = "contentws_register"
        #
        super(Register, self).__init__(apiKey=apiKey, userAgent=userAgent, apiName=apiName, apiUrl=apiUrl, verify=False)
        #

    def register(self, email):
        """ Request an API access token be sent to the input e-mail address

        :param string email: e-mail address

        :rtype: json service response converted to dictionary (with mininal keys: api_error_flag, api_status_text)

        """
        pD = {}
        pD = {'email': email}
        return self.get('accesstoken', **pD)
