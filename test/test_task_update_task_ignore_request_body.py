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
from openapiclient.models.task_update_task_ignore_request_body import TaskUpdateTaskIgnoreRequestBody  # noqa: E501
from openapiclient.rest import ApiException

class TestTaskUpdateTaskIgnoreRequestBody(unittest.TestCase):
    """TaskUpdateTaskIgnoreRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskUpdateTaskIgnoreRequestBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskUpdateTaskIgnoreRequestBody`
        """
        model = openapiclient.models.task_update_task_ignore_request_body.TaskUpdateTaskIgnoreRequestBody()  # noqa: E501
        if include_optional :
            return TaskUpdateTaskIgnoreRequestBody(
                ignore_until = 'forever'
            )
        else :
            return TaskUpdateTaskIgnoreRequestBody(
                ignore_until = 'forever',
        )
        """

    def testTaskUpdateTaskIgnoreRequestBody(self):
        """Test TaskUpdateTaskIgnoreRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
