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
from openapiclient.api.health_api import HealthApi  # noqa: E501
from openapiclient.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = openapiclient.api.health_api.HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_health(self):
        """Test case for health_health

        health health  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
