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
from openapiclient.models.lockfile_get_lockfile_list_response_body import LockfileGetLockfileListResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestLockfileGetLockfileListResponseBody(unittest.TestCase):
    """LockfileGetLockfileListResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LockfileGetLockfileListResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LockfileGetLockfileListResponseBody`
        """
        model = openapiclient.models.lockfile_get_lockfile_list_response_body.LockfileGetLockfileListResponseBody()  # noqa: E501
        if include_optional :
            return LockfileGetLockfileListResponseBody(
                lockfiles = [{"createdAt":"2018-07-14T08:13:28Z","fileContent":"","id":1,"libraryPkgs":[{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"}],"path":"/FutureVuls/package.json","server":{"createdAt":"2018-07-14T08:13:28Z","defaultUserId":1,"defaultUserName":"vuls user","hostUuid":"141df30a-ecd0-39f4-a8f4-1ef216a4b5f2","id":1,"lastScannedAt":"2018-07-14T08:13:28Z","lastUploadedAt":"2018-07-14T08:13:28Z","needKernelRestart":true,"osFamily":"centos","osVersion":"6","serverName":"server01","serverUuid":"abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2","serverroleId":1,"serverroleName":"server_role01","tags":["Voluptatem quis nihil hic minima.","Quidem non aut incidunt."],"updatedAt":"2018-07-14T08:13:28Z"},"updatedAt":"2018-07-14T08:13:28Z"},{"createdAt":"2018-07-14T08:13:28Z","fileContent":"","id":1,"libraryPkgs":[{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"}],"path":"/FutureVuls/package.json","server":{"createdAt":"2018-07-14T08:13:28Z","defaultUserId":1,"defaultUserName":"vuls user","hostUuid":"141df30a-ecd0-39f4-a8f4-1ef216a4b5f2","id":1,"lastScannedAt":"2018-07-14T08:13:28Z","lastUploadedAt":"2018-07-14T08:13:28Z","needKernelRestart":true,"osFamily":"centos","osVersion":"6","serverName":"server01","serverUuid":"abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2","serverroleId":1,"serverroleName":"server_role01","tags":["Voluptatem quis nihil hic minima.","Quidem non aut incidunt."],"updatedAt":"2018-07-14T08:13:28Z"},"updatedAt":"2018-07-14T08:13:28Z"},{"createdAt":"2018-07-14T08:13:28Z","fileContent":"","id":1,"libraryPkgs":[{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"}],"path":"/FutureVuls/package.json","server":{"createdAt":"2018-07-14T08:13:28Z","defaultUserId":1,"defaultUserName":"vuls user","hostUuid":"141df30a-ecd0-39f4-a8f4-1ef216a4b5f2","id":1,"lastScannedAt":"2018-07-14T08:13:28Z","lastUploadedAt":"2018-07-14T08:13:28Z","needKernelRestart":true,"osFamily":"centos","osVersion":"6","serverName":"server01","serverUuid":"abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2","serverroleId":1,"serverroleName":"server_role01","tags":["Voluptatem quis nihil hic minima.","Quidem non aut incidunt."],"updatedAt":"2018-07-14T08:13:28Z"},"updatedAt":"2018-07-14T08:13:28Z"},{"createdAt":"2018-07-14T08:13:28Z","fileContent":"","id":1,"libraryPkgs":[{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"},{"createdAt":"2018-07-14T08:13:28Z","id":1,"name":"package01","updatedAt":"2018-07-14T08:13:28Z","version":"1.0"}],"path":"/FutureVuls/package.json","server":{"createdAt":"2018-07-14T08:13:28Z","defaultUserId":1,"defaultUserName":"vuls user","hostUuid":"141df30a-ecd0-39f4-a8f4-1ef216a4b5f2","id":1,"lastScannedAt":"2018-07-14T08:13:28Z","lastUploadedAt":"2018-07-14T08:13:28Z","needKernelRestart":true,"osFamily":"centos","osVersion":"6","serverName":"server01","serverUuid":"abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2","serverroleId":1,"serverroleName":"server_role01","tags":["Voluptatem quis nihil hic minima.","Quidem non aut incidunt."],"updatedAt":"2018-07-14T08:13:28Z"},"updatedAt":"2018-07-14T08:13:28Z"}], 
                paging = {"limit":20,"offset":10,"page":1,"totalCount":200,"totalPage":10}
            )
        else :
            return LockfileGetLockfileListResponseBody(
        )
        """

    def testLockfileGetLockfileListResponseBody(self):
        """Test LockfileGetLockfileListResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
