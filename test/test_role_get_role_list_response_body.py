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
from openapiclient.models.role_get_role_list_response_body import RoleGetRoleListResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestRoleGetRoleListResponseBody(unittest.TestCase):
    """RoleGetRoleListResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoleGetRoleListResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleGetRoleListResponseBody`
        """
        model = openapiclient.models.role_get_role_list_response_body.RoleGetRoleListResponseBody()  # noqa: E501
        if include_optional :
            return RoleGetRoleListResponseBody(
                paging = {"limit":20,"offset":10,"page":1,"totalCount":200,"totalPage":10}, 
                roles = [{"allTaskCount":10,"createdAt":"2018-07-14T08:13:28Z","id":1,"isDefault":true,"name":"server-role-name","newTaskCount":10,"secMetric":{"ar":"","cr":"","createdAt":"2018-07-14T08:13:28Z","ir":"","roleID":1,"roleName":"roleName","updatedAt":"2018-07-14T08:13:28Z"},"serverCount":10,"updatedAt":"2018-07-14T08:13:28Z"},{"allTaskCount":10,"createdAt":"2018-07-14T08:13:28Z","id":1,"isDefault":true,"name":"server-role-name","newTaskCount":10,"secMetric":{"ar":"","cr":"","createdAt":"2018-07-14T08:13:28Z","ir":"","roleID":1,"roleName":"roleName","updatedAt":"2018-07-14T08:13:28Z"},"serverCount":10,"updatedAt":"2018-07-14T08:13:28Z"}]
            )
        else :
            return RoleGetRoleListResponseBody(
        )
        """

    def testRoleGetRoleListResponseBody(self):
        """Test RoleGetRoleListResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()