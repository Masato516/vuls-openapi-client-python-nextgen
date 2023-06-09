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
from openapiclient.models.paging_response_body import PagingResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestPagingResponseBody(unittest.TestCase):
    """PagingResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagingResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PagingResponseBody`
        """
        model = openapiclient.models.paging_response_body.PagingResponseBody()  # noqa: E501
        if include_optional :
            return PagingResponseBody(
                limit = 20, 
                offset = 10, 
                page = 1, 
                total_count = 200, 
                total_page = 10
            )
        else :
            return PagingResponseBody(
                limit = 20,
                offset = 10,
                page = 1,
                total_count = 200,
                total_page = 10,
        )
        """

    def testPagingResponseBody(self):
        """Test PagingResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
