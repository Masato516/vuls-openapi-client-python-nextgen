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
from openapiclient.api.group_set_pkg_cpe_api import GroupSetPkgCpeApi  # noqa: E501
from openapiclient.rest import ApiException


class TestGroupSetPkgCpeApi(unittest.TestCase):
    """GroupSetPkgCpeApi unit test stubs"""

    def setUp(self):
        self.api = openapiclient.api.group_set_pkg_cpe_api.GroupSetPkgCpeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_group_set_pkg_cpe_get_group_set_cpe_detail(self):
        """Test case for group_set_pkg_cpe_get_group_set_cpe_detail

        getGroupSetCpeDetail groupSetPkgCpe  # noqa: E501
        """
        pass

    def test_group_set_pkg_cpe_get_group_set_pkg_cpe_list(self):
        """Test case for group_set_pkg_cpe_get_group_set_pkg_cpe_list

        getGroupSetPkgCpeList groupSetPkgCpe  # noqa: E501
        """
        pass

    def test_group_set_pkg_cpe_get_group_set_pkg_detail(self):
        """Test case for group_set_pkg_cpe_get_group_set_pkg_detail

        getGroupSetPkgDetail groupSetPkgCpe  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
