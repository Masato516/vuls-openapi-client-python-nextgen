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
from openapiclient.models.task_list_response_body import TaskListResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestTaskListResponseBody(unittest.TestCase):
    """TaskListResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskListResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskListResponseBody`
        """
        model = openapiclient.models.task_list_response_body.TaskListResponseBody()  # noqa: E501
        if include_optional :
            return TaskListResponseBody(
                is_running_process = True, 
                advisory_ids = ["advisoryID"], 
                applying_patch_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                cloud_one_detect_only = True, 
                cloud_one_status = 'prevent', 
                created_at = '2018-07-14T08:13:28Z', 
                cve = {"advisoryIDs":["advisoryID"],"cveID":"CVE-2018-1234","cwes":[{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"}],"exploitLevel":"Ut distinctio suscipit labore.","hasExploit":true,"hasMitigation":true,"isOwaspTopTen2017":true,"maxV2":9,"maxV3":9,"pkgFixedStatus":"Ratione dolorem omnis quidem excepturi.","pkgFixedStatusName":"Accusantium asperiores quidem omnis voluptatem quia voluptas.","scoreV2s":{"nvd":9,"redhat":7},"scoreV3s":{"nvd":8,"redhat":9},"title":"title","vectorV2s":{"jvn":"AV:L/AC:M/Au:N/C:C/I:N/A:N","nvd":"AV:L/AC:M/Au:N/C:C/I:N/A:N"},"vectorV3s":{"jvn":"AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N","nvd":"AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N"}}, 
                cve_id = 'CVE-2017-6799', 
                deadline_on = 'Fri Jul 13 00:00:00 UTC 2018', 
                detection_methods = [{"name":"vuls","reliabilityScore":100},{"name":"vuls","reliabilityScore":100},{"name":"vuls","reliabilityScore":100},{"name":"vuls","reliabilityScore":100}], 
                detection_tools = [{"name":"changelog","patchAppliedAt":"2018-07-14T08:13:28Z"},{"name":"changelog","patchAppliedAt":"2018-07-14T08:13:28Z"},{"name":"changelog","patchAppliedAt":"2018-07-14T08:13:28Z"},{"name":"changelog","patchAppliedAt":"2018-07-14T08:13:28Z"}], 
                exploit_level = 'high', 
                group = {"ID":1,"groupName":"CWE-416"}, 
                has_danger = False, 
                has_exploit = True, 
                has_mitigation = True, 
                id = 1, 
                ignore = True, 
                ignore_expired_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                ignore_until = 'vector', 
                is_important = False, 
                listening_ports = ["192.0.0.1"], 
                main_user_id = 1, 
                main_user_name = 'main-user-name', 
                newed_at = '2018-07-14T08:13:28Z', 
                org_alert_tags = ["Alert For CVE-2017-6799"], 
                os_family = 'centos', 
                os_version = '6', 
                pkg_cpe_names = ["package1","package2"], 
                pkg_fixed_status = 'none', 
                pkg_fixed_status_names = 'affected', 
                priority = 'high', 
                server = {"createdAt":"2018-07-14T08:13:28Z","defaultUserId":1,"defaultUserName":"vuls user","hostUuid":"141df30a-ecd0-39f4-a8f4-1ef216a4b5f2","id":1,"lastScannedAt":"2018-07-14T08:13:28Z","lastUploadedAt":"2018-07-14T08:13:28Z","needKernelRestart":true,"osFamily":"centos","osVersion":"6","serverName":"server01","serverUuid":"abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2","serverroleId":1,"serverroleName":"server_role01","tags":["Numquam excepturi.","Eos est consequuntur.","Repellendus voluptatum nihil autem ullam.","Corrupti ea voluptas."],"updatedAt":"2018-07-14T08:13:28Z"}, 
                server_id = 1, 
                server_name = 'serverName', 
                server_tags = ["tag"], 
                server_uuid = 'abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2', 
                ssvc_priority = 'Itaque officia voluptatum iure.', 
                status = 'new', 
                sub_user_id = 1, 
                sub_user_name = 'sub-user-name', 
                updatable_pkg_cpe_names = ["package1","package2"], 
                updated_at = '2018-07-14T08:13:28Z', 
                vuln_info = {"alertLevel":"Aut est.","cwe":[{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"}],"hasAlert":true,"isOwaspTopTen2017":true,"title":"Voluptatem unde sit sit amet neque."}
            )
        else :
            return TaskListResponseBody(
                advisory_ids = ["advisoryID"],
                created_at = '2018-07-14T08:13:28Z',
                cve_id = 'CVE-2017-6799',
                detection_methods = [{"name":"vuls","reliabilityScore":100},{"name":"vuls","reliabilityScore":100},{"name":"vuls","reliabilityScore":100},{"name":"vuls","reliabilityScore":100}],
                detection_tools = [{"name":"changelog","patchAppliedAt":"2018-07-14T08:13:28Z"},{"name":"changelog","patchAppliedAt":"2018-07-14T08:13:28Z"},{"name":"changelog","patchAppliedAt":"2018-07-14T08:13:28Z"},{"name":"changelog","patchAppliedAt":"2018-07-14T08:13:28Z"}],
                has_danger = False,
                id = 1,
                ignore = True,
                is_important = False,
                listening_ports = ["192.0.0.1"],
                newed_at = '2018-07-14T08:13:28Z',
                os_family = 'centos',
                os_version = '6',
                priority = 'high',
                server_id = 1,
                server_name = 'serverName',
                server_uuid = 'abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2',
                status = 'new',
                updated_at = '2018-07-14T08:13:28Z',
        )
        """

    def testTaskListResponseBody(self):
        """Test TaskListResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
