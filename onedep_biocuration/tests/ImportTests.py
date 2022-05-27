##
# File: ImportTests.py
# Date:  08-Dec-2020  E. Peisach
#
# Updates:
##
"""Test cases for onedep API"""

__docformat__ = "restructuredtext en"
__author__ = "Ezra Peisach"
__email__ = "peisach@rcsb.rutgers.edu"
__license__ = "Creative Commons Attribution 3.0 Unported"
__version__ = "V0.01"

import unittest

from onedep_biocuration.api.ContentRequest import ContentRequest
import onedep_biocuration.cli.biocuration_cli  # noqa: F401 pylint: disable=unused-import
from onedep_biocuration import __apiUrl__, __version__
from onedep_biocuration.utils.ApiBase import ApiBase


class ImportTests(unittest.TestCase):
    def setUp(self):
        pass

    def testInstantiate(self):
        """Tests simple instantiation"""
        _c = ContentRequest()  # noqa: F841
        _a = ApiBase()  # noqa: F841
        print("ApiUrl %s" % __apiUrl__)
        print("Version %s" % __version__)
