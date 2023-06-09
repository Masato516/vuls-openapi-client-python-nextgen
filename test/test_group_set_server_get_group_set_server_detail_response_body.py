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
from openapiclient.models.group_set_server_get_group_set_server_detail_response_body import GroupSetServerGetGroupSetServerDetailResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestGroupSetServerGetGroupSetServerDetailResponseBody(unittest.TestCase):
    """GroupSetServerGetGroupSetServerDetailResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GroupSetServerGetGroupSetServerDetailResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupSetServerGetGroupSetServerDetailResponseBody`
        """
        model = openapiclient.models.group_set_server_get_group_set_server_detail_response_body.GroupSetServerGetGroupSetServerDetailResponseBody()  # noqa: E501
        if include_optional :
            return GroupSetServerGetGroupSetServerDetailResponseBody(
                created_at = '2018-07-14T08:13:28Z', 
                default_user_id = 1, 
                default_user_name = 'vuls user', 
                group = {"ID":1,"groupName":"CWE-416"}, 
                host_uuid = '141df30a-ecd0-39f4-a8f4-1ef216a4b5f2', 
                id = 1, 
                last_scanned_at = '2018-07-14T08:13:28Z', 
                last_uploaded_at = '2018-07-14T08:13:28Z', 
                need_kernel_restart = True, 
                os_family = 'centos', 
                os_version = '6', 
                platform_instance_id = 'i-xxxxxxx', 
                platform_name = 'aws', 
                server_ipv4 = '192.168.0.2', 
                server_name = 'server01', 
                server_uuid = 'abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2', 
                serverrole_id = 1, 
                serverrole_name = 'server_role01', 
                tags = [{"id":1,"name":"tag"},{"id":1,"name":"tag"},{"id":1,"name":"tag"},{"id":1,"name":"tag"}], 
                tasks = [{"applyingPatchOn":"2018-07-14T08:13:28Z","createdAt":"2018-07-14T08:13:28Z","cveID":"CVE-2017-6799","id":1,"ignore":true,"ignoreUntil":"vector","mainUserID":1,"mainUserName":"main-user-name","priority":"high","serverID":1,"status":"new","subUserID":1,"subUserName":"sub-user-name","updatedAt":"2018-07-14T08:13:28Z"},{"applyingPatchOn":"2018-07-14T08:13:28Z","createdAt":"2018-07-14T08:13:28Z","cveID":"CVE-2017-6799","id":1,"ignore":true,"ignoreUntil":"vector","mainUserID":1,"mainUserName":"main-user-name","priority":"high","serverID":1,"status":"new","subUserID":1,"subUserName":"sub-user-name","updatedAt":"2018-07-14T08:13:28Z"},{"applyingPatchOn":"2018-07-14T08:13:28Z","createdAt":"2018-07-14T08:13:28Z","cveID":"CVE-2017-6799","id":1,"ignore":true,"ignoreUntil":"vector","mainUserID":1,"mainUserName":"main-user-name","priority":"high","serverID":1,"status":"new","subUserID":1,"subUserName":"sub-user-name","updatedAt":"2018-07-14T08:13:28Z"},{"applyingPatchOn":"2018-07-14T08:13:28Z","createdAt":"2018-07-14T08:13:28Z","cveID":"CVE-2017-6799","id":1,"ignore":true,"ignoreUntil":"vector","mainUserID":1,"mainUserName":"main-user-name","priority":"high","serverID":1,"status":"new","subUserID":1,"subUserName":"sub-user-name","updatedAt":"2018-07-14T08:13:28Z"}], 
                updated_at = '2018-07-14T08:13:28Z'
            )
        else :
            return GroupSetServerGetGroupSetServerDetailResponseBody(
                created_at = '2018-07-14T08:13:28Z',
                host_uuid = '141df30a-ecd0-39f4-a8f4-1ef216a4b5f2',
                id = 1,
                need_kernel_restart = True,
                os_family = 'centos',
                os_version = '6',
                platform_instance_id = 'i-xxxxxxx',
                platform_name = 'aws',
                server_ipv4 = '192.168.0.2',
                server_name = 'server01',
                server_uuid = 'abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2',
                serverrole_id = 1,
                serverrole_name = 'server_role01',
                updated_at = '2018-07-14T08:13:28Z',
        )
        """

    def testGroupSetServerGetGroupSetServerDetailResponseBody(self):
        """Test GroupSetServerGetGroupSetServerDetailResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
