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
from openapiclient.models.task_add_task_comment_request_body import TaskAddTaskCommentRequestBody  # noqa: E501
from openapiclient.rest import ApiException

class TestTaskAddTaskCommentRequestBody(unittest.TestCase):
    """TaskAddTaskCommentRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskAddTaskCommentRequestBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskAddTaskCommentRequestBody`
        """
        model = openapiclient.models.task_add_task_comment_request_body.TaskAddTaskCommentRequestBody()  # noqa: E501
        if include_optional :
            return TaskAddTaskCommentRequestBody(
                comment_content = 'comment'
            )
        else :
            return TaskAddTaskCommentRequestBody(
                comment_content = 'comment',
        )
        """

    def testTaskAddTaskCommentRequestBody(self):
        """Test TaskAddTaskCommentRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
