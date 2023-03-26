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
from openapiclient.models.group_set_cve_get_group_set_cve_detail_response_body import GroupSetCveGetGroupSetCveDetailResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestGroupSetCveGetGroupSetCveDetailResponseBody(unittest.TestCase):
    """GroupSetCveGetGroupSetCveDetailResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GroupSetCveGetGroupSetCveDetailResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupSetCveGetGroupSetCveDetailResponseBody`
        """
        model = openapiclient.models.group_set_cve_get_group_set_cve_detail_response_body.GroupSetCveGetGroupSetCveDetailResponseBody()  # noqa: E501
        if include_optional :
            return GroupSetCveGetGroupSetCveDetailResponseBody(
                created_at = '2018-07-14T08:13:28Z', 
                cve_id = 'CVE-2018-1234', 
                cvss = {"cveID":"CVE-2021-22880","maxCvssV2":{"type":"nvd","value":{"calculatedBySeverity":false,"score":5,"severity":"MEDIUM","type":"2","vector":"AV:N/AC:L/Au:N/C:N/I:N/A:P"}},"maxCvssV3":{"type":"trivy","value":{"calculatedBySeverity":true,"score":8.9,"severity":"HIGH","type":"3","vector":""}},"vulnInfo":{"alertDict":{"cisa":null,"jpcert":null,"uscert":null},"ctis":["T1499","CAPEC-147","CAPEC-492","CAPEC-227"],"cveContents":{"debian":[{"cveID":"CVE-2021-22880","cvss2Score":0,"cvss2Severity":"not yet assigned","cvss2Vector":"","cvss3Score":0,"cvss3Severity":"not yet assigned","cvss3Vector":"","lastModified":"0001-01-01T00:00:00Z","optional":{"attack range":"local"},"published":"0001-01-01T00:00:00Z","sourceLink":"https://security-tracker.debian.org/tracker/CVE-2021-22880","summary":"The PostgreSQL adapter in Active Record before 6.1.2.1, 6.0.3.5, 5.2.4.5 suffers from a regular expression denial of service (REDoS) vulnerability. Carefully crafted input can cause the input validation in the `money` type of the PostgreSQL adapter in Active Record to spend too much time in a regular expression, resulting in the potential for a DoS attack. This only impacts Rails applications that are using PostgreSQL along with money type columns that take user input.","title":"","type":"debian"}],"jvn":[{"cveID":"CVE-2021-22880","cvss2Score":5,"cvss2Severity":"Medium","cvss2Vector":"AV:N/AC:L/Au:N/C:N/I:N/A:P","cvss3Score":7.5,"cvss3Severity":"High","cvss3Vector":"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H","lastModified":"2021-11-04T15:05:00+09:00","published":"2021-11-04T15:05:00+09:00","references":[{"link":"https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22880","source":"CVE"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2021-22880","source":"NVD"},{"link":"https://hackerone.com/reports/1023899","source":"関連文書"},{"link":"https://cwe.mitre.org/data/definitions/400.html"}],"sourceLink":"https://jvndb.jvn.jp/ja/contents/2021/JVNDB-2021-003755.html","summary":"Active Record には、リソースの枯渇に関する脆弱性が存在します。\n","title":"Active Record におけるリソースの枯渇に関する脆弱性","type":"jvn"}],"nvd":[{"cveID":"CVE-2021-22880","cvss2Score":5,"cvss2Severity":"MEDIUM","cvss2Vector":"AV:N/AC:L/Au:N/C:N/I:N/A:P","cvss3Score":7.5,"cvss3Severity":"HIGH","cvss3Vector":"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H","cweIDs":["CWE-400"],"lastModified":"2022-01-04T16:38:00Z","published":"2021-02-11T18:15:00Z","references":[{"link":"https://hackerone.com/reports/1023899","source":"MISC","tags":["Exploit","Patch","Third Party Advisory"]},{"link":"https://discuss.rubyonrails.org/t/cve-2021-22880-possible-dos-vulnerability-in-active-record-postgresql-adapter/77129","source":"MISC","tags":["Mitigation","Patch","Vendor Advisory"]},{"link":"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/XQ3NS4IBYE2I3MVMGAHFZBZBIZGHXHT3/","source":"FEDORA","tags":["Mailing List","Third Party Advisory"]},{"link":"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/MO5OJ3F4ZL3UXVLJO6ECANRVZBNRS2IH/","source":"FEDORA","tags":["Mailing List","Third Party Advisory"]},{"link":"https://www.debian.org/security/2021/dsa-4929","source":"DEBIAN","tags":["Third Party Advisory"]},{"link":"https://security.netapp.com/advisory/ntap-20210805-0009/","source":"CONFIRM","tags":["Third Party Advisory"]}],"sourceLink":"https://nvd.nist.gov/vuln/detail/CVE-2021-22880","summary":"~~~~~~~~~~~~~~~~~~~~~~~~~~~~","title":"","type":"nvd"}],"redhat":[{"cveID":"CVE-2021-22880","cvss2Score":0,"cvss2Severity":"","cvss2Vector":"","cvss3Score":7.5,"cvss3Severity":"Moderate","cvss3Vector":"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H","cweIDs":["CWE-400"],"lastModified":"0001-01-01T00:00:00Z","published":"2021-02-11T00:00:00Z","references":[{"link":"https://discuss.rubyonrails.org/t/cve-2021-22880-possible-dos-vulnerability-in-active-record-postgresql-adapter/77129"}],"sourceLink":"https://access.redhat.com/security/cve/CVE-2021-22880","summary":"The PostgreSQL adapter in Active Record before 6.1.2.1, 6.0.3.5, 5.2.4.5 suffers from a regular expression denial of service (REDoS) vulnerability. Carefully crafted input can cause the input validation in the `money` type of the PostgreSQL adapter in Active Record to spend too much time in a regular expression, resulting in the potential for a DoS attack. This only impacts Rails applications that are using PostgreSQL along with money type columns that take user input.\nThe PostgreSQL adapter in Active Record suffers from a regular expression denial of service (REDoS) vulnerability. Carefully crafted input can cause the input validation in the `money` type of the PostgreSQL adapter in Active Record to spend too much time in a regular expression, resulting in the potential for a DoS attack. This only impacts Rails applications that are using PostgreSQL along with money type columns that take user input.","title":"CVE-2021-22880 rubygem-activerecord: crafted input may cause a regular expression DoS","type":"redhat"}],"trivy":[{"cveID":"CVE-2021-22880","cvss2Score":0,"cvss2Severity":"","cvss2Vector":"","cvss3Score":0,"cvss3Severity":"HIGH","cvss3Vector":"","lastModified":"0001-01-01T00:00:00Z","published":"0001-01-01T00:00:00Z","references":[{"link":"https://access.redhat.com/security/cve/CVE-2021-22880","source":"trivy"},{"link":"https://discuss.rubyonrails.org/t/cve-2021-22880-possible-dos-vulnerability-in-active-record-postgresql-adapter/77129","source":"trivy"},{"link":"https://github.com/advisories/GHSA-8hc4-xxm3-5ppp","source":"trivy"},{"link":"https://groups.google.com/g/rubyonrails-security/c/ZzUqCh9vyhI","source":"trivy"},{"link":"https://hackerone.com/reports/1023899","source":"trivy"},{"link":"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/MO5OJ3F4ZL3UXVLJO6ECANRVZBNRS2IH/","source":"trivy"},{"link":"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/XQ3NS4IBYE2I3MVMGAHFZBZBIZGHXHT3/","source":"trivy"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2021-22880","source":"trivy"},{"link":"https://rubygems.org/gems/activerecord","source":"trivy"},{"link":"https://security.netapp.com/advisory/ntap-20210805-0009/","source":"trivy"},{"link":"https://www.debian.org/security/2021/dsa-4929","source":"trivy"}],"sourceLink":"","summary":"The PostgreSQL adapter in Active Record before 6.1.2.1, 6.0.3.5, 5.2.4.5 suffers from a regular expression denial of service (REDoS) vulnerability. Carefully crafted input can cause the input validation in the `money` type of the PostgreSQL adapter in Active Record to spend too much time in a regular expression, resulting in the potential for a DoS attack. This only impacts Rails applications that are using PostgreSQL along with money type columns that take user input.","title":"rubygem-activerecord: crafted input may cause a regular expression DoS","type":"trivy"}],"ubuntu":[{"cveID":"CVE-2021-22880","cvss2Score":0,"cvss2Severity":"low","cvss2Vector":"","cvss3Score":0,"cvss3Severity":"low","cvss3Vector":"","lastModified":"0001-01-01T00:00:00Z","published":"2021-02-11T18:15:00Z","references":[{"link":"https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22880","source":"CVE"},{"link":"https://discuss.rubyonrails.org/t/cve-2021-22880-possible-dos-vulnerability-in-active-record-postgresql-adapter/77129"},{"link":"https://hackerone.com/reports/1023899"}],"sourceLink":"https://ubuntu.com/security/CVE-2021-22880","summary":"~~~~~~~~~~~~~~","title":"","type":"ubuntu"}]},"cveID":"CVE-2021-22880","exploits":[{"description":"","exploitType":"nvd","id":"","url":"https://hackerone.com/reports/1023899"}],"mitigations":[{"cveContentType":"nvd","url":"https://discuss.rubyonrails.org/~~~~"}]}}, 
                cwes = [{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"}], 
                group = {"ID":1,"groupName":"CWE-416"}, 
                updated_at = '2018-07-14T08:13:28Z'
            )
        else :
            return GroupSetCveGetGroupSetCveDetailResponseBody(
                created_at = '2018-07-14T08:13:28Z',
                cve_id = 'CVE-2018-1234',
                cvss = {"cveID":"CVE-2021-22880","maxCvssV2":{"type":"nvd","value":{"calculatedBySeverity":false,"score":5,"severity":"MEDIUM","type":"2","vector":"AV:N/AC:L/Au:N/C:N/I:N/A:P"}},"maxCvssV3":{"type":"trivy","value":{"calculatedBySeverity":true,"score":8.9,"severity":"HIGH","type":"3","vector":""}},"vulnInfo":{"alertDict":{"cisa":null,"jpcert":null,"uscert":null},"ctis":["T1499","CAPEC-147","CAPEC-492","CAPEC-227"],"cveContents":{"debian":[{"cveID":"CVE-2021-22880","cvss2Score":0,"cvss2Severity":"not yet assigned","cvss2Vector":"","cvss3Score":0,"cvss3Severity":"not yet assigned","cvss3Vector":"","lastModified":"0001-01-01T00:00:00Z","optional":{"attack range":"local"},"published":"0001-01-01T00:00:00Z","sourceLink":"https://security-tracker.debian.org/tracker/CVE-2021-22880","summary":"The PostgreSQL adapter in Active Record before 6.1.2.1, 6.0.3.5, 5.2.4.5 suffers from a regular expression denial of service (REDoS) vulnerability. Carefully crafted input can cause the input validation in the `money` type of the PostgreSQL adapter in Active Record to spend too much time in a regular expression, resulting in the potential for a DoS attack. This only impacts Rails applications that are using PostgreSQL along with money type columns that take user input.","title":"","type":"debian"}],"jvn":[{"cveID":"CVE-2021-22880","cvss2Score":5,"cvss2Severity":"Medium","cvss2Vector":"AV:N/AC:L/Au:N/C:N/I:N/A:P","cvss3Score":7.5,"cvss3Severity":"High","cvss3Vector":"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H","lastModified":"2021-11-04T15:05:00+09:00","published":"2021-11-04T15:05:00+09:00","references":[{"link":"https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22880","source":"CVE"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2021-22880","source":"NVD"},{"link":"https://hackerone.com/reports/1023899","source":"関連文書"},{"link":"https://cwe.mitre.org/data/definitions/400.html"}],"sourceLink":"https://jvndb.jvn.jp/ja/contents/2021/JVNDB-2021-003755.html","summary":"Active Record には、リソースの枯渇に関する脆弱性が存在します。\n","title":"Active Record におけるリソースの枯渇に関する脆弱性","type":"jvn"}],"nvd":[{"cveID":"CVE-2021-22880","cvss2Score":5,"cvss2Severity":"MEDIUM","cvss2Vector":"AV:N/AC:L/Au:N/C:N/I:N/A:P","cvss3Score":7.5,"cvss3Severity":"HIGH","cvss3Vector":"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H","cweIDs":["CWE-400"],"lastModified":"2022-01-04T16:38:00Z","published":"2021-02-11T18:15:00Z","references":[{"link":"https://hackerone.com/reports/1023899","source":"MISC","tags":["Exploit","Patch","Third Party Advisory"]},{"link":"https://discuss.rubyonrails.org/t/cve-2021-22880-possible-dos-vulnerability-in-active-record-postgresql-adapter/77129","source":"MISC","tags":["Mitigation","Patch","Vendor Advisory"]},{"link":"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/XQ3NS4IBYE2I3MVMGAHFZBZBIZGHXHT3/","source":"FEDORA","tags":["Mailing List","Third Party Advisory"]},{"link":"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/MO5OJ3F4ZL3UXVLJO6ECANRVZBNRS2IH/","source":"FEDORA","tags":["Mailing List","Third Party Advisory"]},{"link":"https://www.debian.org/security/2021/dsa-4929","source":"DEBIAN","tags":["Third Party Advisory"]},{"link":"https://security.netapp.com/advisory/ntap-20210805-0009/","source":"CONFIRM","tags":["Third Party Advisory"]}],"sourceLink":"https://nvd.nist.gov/vuln/detail/CVE-2021-22880","summary":"~~~~~~~~~~~~~~~~~~~~~~~~~~~~","title":"","type":"nvd"}],"redhat":[{"cveID":"CVE-2021-22880","cvss2Score":0,"cvss2Severity":"","cvss2Vector":"","cvss3Score":7.5,"cvss3Severity":"Moderate","cvss3Vector":"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H","cweIDs":["CWE-400"],"lastModified":"0001-01-01T00:00:00Z","published":"2021-02-11T00:00:00Z","references":[{"link":"https://discuss.rubyonrails.org/t/cve-2021-22880-possible-dos-vulnerability-in-active-record-postgresql-adapter/77129"}],"sourceLink":"https://access.redhat.com/security/cve/CVE-2021-22880","summary":"The PostgreSQL adapter in Active Record before 6.1.2.1, 6.0.3.5, 5.2.4.5 suffers from a regular expression denial of service (REDoS) vulnerability. Carefully crafted input can cause the input validation in the `money` type of the PostgreSQL adapter in Active Record to spend too much time in a regular expression, resulting in the potential for a DoS attack. This only impacts Rails applications that are using PostgreSQL along with money type columns that take user input.\nThe PostgreSQL adapter in Active Record suffers from a regular expression denial of service (REDoS) vulnerability. Carefully crafted input can cause the input validation in the `money` type of the PostgreSQL adapter in Active Record to spend too much time in a regular expression, resulting in the potential for a DoS attack. This only impacts Rails applications that are using PostgreSQL along with money type columns that take user input.","title":"CVE-2021-22880 rubygem-activerecord: crafted input may cause a regular expression DoS","type":"redhat"}],"trivy":[{"cveID":"CVE-2021-22880","cvss2Score":0,"cvss2Severity":"","cvss2Vector":"","cvss3Score":0,"cvss3Severity":"HIGH","cvss3Vector":"","lastModified":"0001-01-01T00:00:00Z","published":"0001-01-01T00:00:00Z","references":[{"link":"https://access.redhat.com/security/cve/CVE-2021-22880","source":"trivy"},{"link":"https://discuss.rubyonrails.org/t/cve-2021-22880-possible-dos-vulnerability-in-active-record-postgresql-adapter/77129","source":"trivy"},{"link":"https://github.com/advisories/GHSA-8hc4-xxm3-5ppp","source":"trivy"},{"link":"https://groups.google.com/g/rubyonrails-security/c/ZzUqCh9vyhI","source":"trivy"},{"link":"https://hackerone.com/reports/1023899","source":"trivy"},{"link":"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/MO5OJ3F4ZL3UXVLJO6ECANRVZBNRS2IH/","source":"trivy"},{"link":"https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/XQ3NS4IBYE2I3MVMGAHFZBZBIZGHXHT3/","source":"trivy"},{"link":"https://nvd.nist.gov/vuln/detail/CVE-2021-22880","source":"trivy"},{"link":"https://rubygems.org/gems/activerecord","source":"trivy"},{"link":"https://security.netapp.com/advisory/ntap-20210805-0009/","source":"trivy"},{"link":"https://www.debian.org/security/2021/dsa-4929","source":"trivy"}],"sourceLink":"","summary":"The PostgreSQL adapter in Active Record before 6.1.2.1, 6.0.3.5, 5.2.4.5 suffers from a regular expression denial of service (REDoS) vulnerability. Carefully crafted input can cause the input validation in the `money` type of the PostgreSQL adapter in Active Record to spend too much time in a regular expression, resulting in the potential for a DoS attack. This only impacts Rails applications that are using PostgreSQL along with money type columns that take user input.","title":"rubygem-activerecord: crafted input may cause a regular expression DoS","type":"trivy"}],"ubuntu":[{"cveID":"CVE-2021-22880","cvss2Score":0,"cvss2Severity":"low","cvss2Vector":"","cvss3Score":0,"cvss3Severity":"low","cvss3Vector":"","lastModified":"0001-01-01T00:00:00Z","published":"2021-02-11T18:15:00Z","references":[{"link":"https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22880","source":"CVE"},{"link":"https://discuss.rubyonrails.org/t/cve-2021-22880-possible-dos-vulnerability-in-active-record-postgresql-adapter/77129"},{"link":"https://hackerone.com/reports/1023899"}],"sourceLink":"https://ubuntu.com/security/CVE-2021-22880","summary":"~~~~~~~~~~~~~~","title":"","type":"ubuntu"}]},"cveID":"CVE-2021-22880","exploits":[{"description":"","exploitType":"nvd","id":"","url":"https://hackerone.com/reports/1023899"}],"mitigations":[{"cveContentType":"nvd","url":"https://discuss.rubyonrails.org/~~~~"}]}},
                cwes = [{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"},{"cweID":"CWE-416","english":"english summary","japanese":"japanese summary","owaspTopTen2017":"10"}],
                updated_at = '2018-07-14T08:13:28Z',
        )
        """

    def testGroupSetCveGetGroupSetCveDetailResponseBody(self):
        """Test GroupSetCveGetGroupSetCveDetailResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()