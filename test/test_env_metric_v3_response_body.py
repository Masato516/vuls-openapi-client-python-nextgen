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
from openapiclient.models.env_metric_v3_response_body import EnvMetricV3ResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestEnvMetricV3ResponseBody(unittest.TestCase):
    """EnvMetricV3ResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EnvMetricV3ResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnvMetricV3ResponseBody`
        """
        model = openapiclient.models.env_metric_v3_response_body.EnvMetricV3ResponseBody()  # noqa: E501
        if include_optional :
            return EnvMetricV3ResponseBody(
                created_at = '2018-07-14T08:13:28Z', 
                cve_id = 'CVE-2018-1234', 
                ma = '', 
                mac = '', 
                mav = '', 
                mc = '', 
                mpr = '', 
                ms = '', 
                mui = '', 
                role_id = 1, 
                role_name = 'roleName', 
                updated_at = '2018-07-14T08:13:28Z'
            )
        else :
            return EnvMetricV3ResponseBody(
                created_at = '2018-07-14T08:13:28Z',
                cve_id = 'CVE-2018-1234',
                ma = '',
                mac = '',
                mav = '',
                mc = '',
                mpr = '',
                ms = '',
                mui = '',
                role_id = 1,
                role_name = 'roleName',
                updated_at = '2018-07-14T08:13:28Z',
        )
        """

    def testEnvMetricV3ResponseBody(self):
        """Test EnvMetricV3ResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
