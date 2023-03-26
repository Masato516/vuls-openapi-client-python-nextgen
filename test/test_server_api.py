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
from openapiclient.api.server_api import ServerApi  # noqa: E501
from openapiclient.rest import ApiException


class TestServerApi(unittest.TestCase):
    """ServerApi unit test stubs"""

    def setUp(self):
        self.api = openapiclient.api.server_api.ServerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_server_create_pkg_paste_server(self):
        """Test case for server_create_pkg_paste_server

        createPkgPasteServer server  # noqa: E501
        """
        pass

    def test_server_delete_server(self):
        """Test case for server_delete_server

        deleteServer server  # noqa: E501
        """
        pass

    def test_server_get_server_detail(self):
        """Test case for server_get_server_detail

        getServerDetail server  # noqa: E501
        """
        pass

    def test_server_get_server_detail_by_uuid(self):
        """Test case for server_get_server_detail_by_uuid

        getServerDetailByUUID server  # noqa: E501
        """
        pass

    def test_server_get_server_list(self):
        """Test case for server_get_server_list

        getServerList server  # noqa: E501
        """
        pass

    def test_server_scan_server(self):
        """Test case for server_scan_server

        scanServer server  # noqa: E501
        """
        pass

    def test_server_update_pkg_paste_server(self):
        """Test case for server_update_pkg_paste_server

        updatePkgPasteServer server  # noqa: E501
        """
        pass

    def test_server_update_server(self):
        """Test case for server_update_server

        updateServer server  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
