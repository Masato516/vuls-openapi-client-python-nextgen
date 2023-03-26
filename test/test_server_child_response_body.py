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
from openapiclient.models.server_child_response_body import ServerChildResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestServerChildResponseBody(unittest.TestCase):
    """ServerChildResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ServerChildResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerChildResponseBody`
        """
        model = openapiclient.models.server_child_response_body.ServerChildResponseBody()  # noqa: E501
        if include_optional :
            return ServerChildResponseBody(
                created_at = '2018-07-14T08:13:28Z', 
                default_user_id = 1, 
                default_user_name = 'vuls user', 
                host_uuid = '141df30a-ecd0-39f4-a8f4-1ef216a4b5f2', 
                id = 1, 
                last_scanned_at = '2018-07-14T08:13:28Z', 
                last_uploaded_at = '2018-07-14T08:13:28Z', 
                need_kernel_restart = True, 
                os_family = 'centos', 
                os_version = '6', 
                server_name = 'server01', 
                server_uuid = 'abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2', 
                serverrole_id = 1, 
                serverrole_name = 'server_role01', 
                tags = ["Rerum expedita.","Et blanditiis molestiae corporis."], 
                updated_at = '2018-07-14T08:13:28Z'
            )
        else :
            return ServerChildResponseBody(
                created_at = '2018-07-14T08:13:28Z',
                host_uuid = '141df30a-ecd0-39f4-a8f4-1ef216a4b5f2',
                id = 1,
                need_kernel_restart = True,
                os_family = 'centos',
                os_version = '6',
                server_name = 'server01',
                server_uuid = 'abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2',
                serverrole_id = 1,
                serverrole_name = 'server_role01',
                updated_at = '2018-07-14T08:13:28Z',
        )
        """

    def testServerChildResponseBody(self):
        """Test ServerChildResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
