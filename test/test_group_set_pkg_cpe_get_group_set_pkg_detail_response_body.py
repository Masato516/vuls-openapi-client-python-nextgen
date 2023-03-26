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
from openapiclient.models.group_set_pkg_cpe_get_group_set_pkg_detail_response_body import GroupSetPkgCpeGetGroupSetPkgDetailResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestGroupSetPkgCpeGetGroupSetPkgDetailResponseBody(unittest.TestCase):
    """GroupSetPkgCpeGetGroupSetPkgDetailResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GroupSetPkgCpeGetGroupSetPkgDetailResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupSetPkgCpeGetGroupSetPkgDetailResponseBody`
        """
        model = openapiclient.models.group_set_pkg_cpe_get_group_set_pkg_detail_response_body.GroupSetPkgCpeGetGroupSetPkgDetailResponseBody()  # noqa: E501
        if include_optional :
            return GroupSetPkgCpeGetGroupSetPkgDetailResponseBody(
                affected_procs = [{"name":"apache","pid":"12"},{"name":"apache","pid":"12"}], 
                created_at = '2018-07-14T08:13:28Z', 
                group = {"ID":1,"groupName":"CWE-416"}, 
                id = 1, 
                name = 'package01', 
                need_restart_procs = [{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"},{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"},{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"}], 
                new_release = 'new release', 
                new_version = '2.0', 
                package_statuses = {"bash":"resolved"}, 
                release = 'release', 
                repository = 'repository', 
                server = {"createdAt":"2018-07-14T08:13:28Z","defaultUserId":1,"defaultUserName":"vuls user","hostUuid":"141df30a-ecd0-39f4-a8f4-1ef216a4b5f2","id":1,"lastScannedAt":"2018-07-14T08:13:28Z","lastUploadedAt":"2018-07-14T08:13:28Z","needKernelRestart":true,"osFamily":"centos","osVersion":"6","serverName":"server01","serverUuid":"abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2","serverroleId":1,"serverroleName":"server_role01","tags":["Numquam excepturi.","Eos est consequuntur.","Repellendus voluptatum nihil autem ullam.","Corrupti ea voluptas."],"updatedAt":"2018-07-14T08:13:28Z"}, 
                tasks = [{"applyingPatchOn":"2018-07-14T08:13:28Z","createdAt":"2018-07-14T08:13:28Z","cveID":"CVE-2017-6799","id":1,"ignore":true,"ignoreUntil":"vector","mainUserID":1,"mainUserName":"main-user-name","priority":"high","serverID":1,"status":"new","subUserID":1,"subUserName":"sub-user-name","updatedAt":"2018-07-14T08:13:28Z"},{"applyingPatchOn":"2018-07-14T08:13:28Z","createdAt":"2018-07-14T08:13:28Z","cveID":"CVE-2017-6799","id":1,"ignore":true,"ignoreUntil":"vector","mainUserID":1,"mainUserName":"main-user-name","priority":"high","serverID":1,"status":"new","subUserID":1,"subUserName":"sub-user-name","updatedAt":"2018-07-14T08:13:28Z"},{"applyingPatchOn":"2018-07-14T08:13:28Z","createdAt":"2018-07-14T08:13:28Z","cveID":"CVE-2017-6799","id":1,"ignore":true,"ignoreUntil":"vector","mainUserID":1,"mainUserName":"main-user-name","priority":"high","serverID":1,"status":"new","subUserID":1,"subUserName":"sub-user-name","updatedAt":"2018-07-14T08:13:28Z"},{"applyingPatchOn":"2018-07-14T08:13:28Z","createdAt":"2018-07-14T08:13:28Z","cveID":"CVE-2017-6799","id":1,"ignore":true,"ignoreUntil":"vector","mainUserID":1,"mainUserName":"main-user-name","priority":"high","serverID":1,"status":"new","subUserID":1,"subUserName":"sub-user-name","updatedAt":"2018-07-14T08:13:28Z"}], 
                updated_at = '2018-07-14T08:13:28Z', 
                version = '1.0'
            )
        else :
            return GroupSetPkgCpeGetGroupSetPkgDetailResponseBody(
                created_at = '2018-07-14T08:13:28Z',
                name = 'package01',
                release = 'release',
                updated_at = '2018-07-14T08:13:28Z',
                version = '1.0',
        )
        """

    def testGroupSetPkgCpeGetGroupSetPkgDetailResponseBody(self):
        """Test GroupSetPkgCpeGetGroupSetPkgDetailResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
