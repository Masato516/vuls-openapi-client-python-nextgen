# coding: utf-8

"""
    Future Vuls Public API

    Future Vuls Public API  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapiclient
from openapiclient.api.group_set_server_api import GroupSetServerApi  # noqa: E501
from openapiclient.rest import ApiException


class TestGroupSetServerApi(unittest.TestCase):
    """GroupSetServerApi unit test stubs"""

    def setUp(self):
        self.api = openapiclient.api.group_set_server_api.GroupSetServerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_group_set_server_get_group_set_server_detail(self):
        """Test case for group_set_server_get_group_set_server_detail

        getGroupSetServerDetail groupSetServer  # noqa: E501
        """
        pass

    def test_group_set_server_get_group_set_server_detail_by_uuid(self):
        """Test case for group_set_server_get_group_set_server_detail_by_uuid

        getGroupSetServerDetailByUUID groupSetServer  # noqa: E501
        """
        pass

    def test_group_set_server_get_group_set_server_list(self):
        """Test case for group_set_server_get_group_set_server_list

        getGroupSetServerList groupSetServer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
