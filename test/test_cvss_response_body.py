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
from openapiclient.models.cvss_response_body import CvssResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestCvssResponseBody(unittest.TestCase):
    """CvssResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CvssResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CvssResponseBody`
        """
        model = openapiclient.models.cvss_response_body.CvssResponseBody()  # noqa: E501
        if include_optional :
            return CvssResponseBody(
                cve_id = '', 
                max_cvss_v2 = openapiclient.models.cvss_response_body_max_cvss_v2.CvssResponseBody_maxCvssV2(
                    type = '', 
                    value = openapiclient.models.value.value(), ), 
                max_cvss_v3 = openapiclient.models.cvss_response_body_max_cvss_v2.CvssResponseBody_maxCvssV2(
                    type = '', 
                    value = openapiclient.models.value.value(), ), 
                vuln_info = openapiclient.models.cvss_response_body_vuln_info.CvssResponseBody_vulnInfo(
                    alert_dict = openapiclient.models.alert_dict.alertDict(), 
                    ctis = [
                        ''
                        ], 
                    cve_contents = openapiclient.models.cve_contents.cveContents(), 
                    cve_id = '', 
                    exploits = [
                        None
                        ], 
                    mitigations = [
                        None
                        ], )
            )
        else :
            return CvssResponseBody(
        )
        """

    def testCvssResponseBody(self):
        """Test CvssResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()