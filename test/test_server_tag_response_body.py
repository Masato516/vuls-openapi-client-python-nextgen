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
from openapiclient.models.server_tag_response_body import ServerTagResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestServerTagResponseBody(unittest.TestCase):
    """ServerTagResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ServerTagResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerTagResponseBody`
        """
        model = openapiclient.models.server_tag_response_body.ServerTagResponseBody()  # noqa: E501
        if include_optional :
            return ServerTagResponseBody(
                id = 1, 
                name = 'tag'
            )
        else :
            return ServerTagResponseBody(
                id = 1,
                name = 'tag',
        )
        """

    def testServerTagResponseBody(self):
        """Test ServerTagResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
