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
from openapiclient.models.lockfile_update_lockfile_request_body import LockfileUpdateLockfileRequestBody  # noqa: E501
from openapiclient.rest import ApiException

class TestLockfileUpdateLockfileRequestBody(unittest.TestCase):
    """LockfileUpdateLockfileRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LockfileUpdateLockfileRequestBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LockfileUpdateLockfileRequestBody`
        """
        model = openapiclient.models.lockfile_update_lockfile_request_body.LockfileUpdateLockfileRequestBody()  # noqa: E501
        if include_optional :
            return LockfileUpdateLockfileRequestBody(
                file_content = '', 
                path = '/FutureVuls/package.json'
            )
        else :
            return LockfileUpdateLockfileRequestBody(
        )
        """

    def testLockfileUpdateLockfileRequestBody(self):
        """Test LockfileUpdateLockfileRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
