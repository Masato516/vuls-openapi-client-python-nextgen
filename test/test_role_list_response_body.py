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
from openapiclient.models.role_list_response_body import RoleListResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestRoleListResponseBody(unittest.TestCase):
    """RoleListResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoleListResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleListResponseBody`
        """
        model = openapiclient.models.role_list_response_body.RoleListResponseBody()  # noqa: E501
        if include_optional :
            return RoleListResponseBody(
                all_task_count = 10, 
                created_at = '2018-07-14T08:13:28Z', 
                id = 1, 
                is_default = True, 
                name = 'server-role-name', 
                new_task_count = 10, 
                sec_metric = {"ar":"","cr":"","createdAt":"2018-07-14T08:13:28Z","ir":"","roleID":1,"roleName":"roleName","updatedAt":"2018-07-14T08:13:28Z"}, 
                server_count = 10, 
                updated_at = '2018-07-14T08:13:28Z'
            )
        else :
            return RoleListResponseBody(
                created_at = '2018-07-14T08:13:28Z',
                id = 1,
                is_default = True,
                name = 'server-role-name',
                updated_at = '2018-07-14T08:13:28Z',
        )
        """

    def testRoleListResponseBody(self):
        """Test RoleListResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
