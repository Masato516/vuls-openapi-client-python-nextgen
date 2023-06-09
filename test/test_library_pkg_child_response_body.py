# coding: utf-8

"""
    Future Vuls Public API

    Future Vuls Public API  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapiclient
from openapiclient.models.library_pkg_child_response_body import LibraryPkgChildResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestLibraryPkgChildResponseBody(unittest.TestCase):
    """LibraryPkgChildResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LibraryPkgChildResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LibraryPkgChildResponseBody`
        """
        model = openapiclient.models.library_pkg_child_response_body.LibraryPkgChildResponseBody()  # noqa: E501
        if include_optional :
            return LibraryPkgChildResponseBody(
                created_at = '2018-07-14T08:13:28Z', 
                id = 1, 
                name = 'package01', 
                updated_at = '2018-07-14T08:13:28Z', 
                version = '1.0'
            )
        else :
            return LibraryPkgChildResponseBody(
                created_at = '2018-07-14T08:13:28Z',
                id = 1,
                name = 'package01',
                updated_at = '2018-07-14T08:13:28Z',
                version = '1.0',
        )
        """

    def testLibraryPkgChildResponseBody(self):
        """Test LibraryPkgChildResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
