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
from openapiclient.models.group_set_cve_list_response_body import GroupSetCveListResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestGroupSetCveListResponseBody(unittest.TestCase):
    """GroupSetCveListResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GroupSetCveListResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupSetCveListResponseBody`
        """
        model = openapiclient.models.group_set_cve_list_response_body.GroupSetCveListResponseBody()  # noqa: E501
        if include_optional :
            return GroupSetCveListResponseBody(
                advisory_ids = ["advisoryID"], 
                created_at = '2018-07-14T08:13:28Z', 
                cve_id = 'CVE-2018-1234', 
                cwes = [{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"}], 
                groups = [{"ID":1,"groupName":"CWE-416"},{"ID":1,"groupName":"CWE-416"},{"ID":1,"groupName":"CWE-416"},{"ID":1,"groupName":"CWE-416"}], 
                has_exploit = True, 
                has_mitigation = True, 
                is_owasp_top_ten2017 = True, 
                max_v2 = 9.0, 
                max_v3 = 9.0, 
                score_v2s = {"nvd":9,"redhat":7}, 
                score_v3s = {"nvd":8,"redhat":9}, 
                title = 'title', 
                topic_count = 10, 
                topic_last_updated_at = '2018-07-14T08:13:28Z', 
                updated_at = '2018-07-14T08:13:28Z', 
                vector_v2s = {"jvn":"AV:L/AC:M/Au:N/C:C/I:N/A:N","nvd":"AV:L/AC:M/Au:N/C:C/I:N/A:N"}, 
                vector_v3s = {"jvn":"AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N","nvd":"AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N"}
            )
        else :
            return GroupSetCveListResponseBody(
                created_at = '2018-07-14T08:13:28Z',
                cve_id = 'CVE-2018-1234',
                cwes = [{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"}],
                groups = [{"ID":1,"groupName":"CWE-416"},{"ID":1,"groupName":"CWE-416"},{"ID":1,"groupName":"CWE-416"},{"ID":1,"groupName":"CWE-416"}],
                is_owasp_top_ten2017 = True,
                max_v2 = 9.0,
                max_v3 = 9.0,
                score_v2s = {"nvd":9,"redhat":7},
                score_v3s = {"nvd":8,"redhat":9},
                title = 'title',
                topic_count = 10,
                topic_last_updated_at = '2018-07-14T08:13:28Z',
                updated_at = '2018-07-14T08:13:28Z',
                vector_v2s = {"jvn":"AV:L/AC:M/Au:N/C:C/I:N/A:N","nvd":"AV:L/AC:M/Au:N/C:C/I:N/A:N"},
                vector_v3s = {"jvn":"AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N","nvd":"AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N"},
        )
        """

    def testGroupSetCveListResponseBody(self):
        """Test GroupSetCveListResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
