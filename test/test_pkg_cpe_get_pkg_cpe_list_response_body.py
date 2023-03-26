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
from openapiclient.models.pkg_cpe_get_pkg_cpe_list_response_body import PkgCpeGetPkgCpeListResponseBody  # noqa: E501
from openapiclient.rest import ApiException

class TestPkgCpeGetPkgCpeListResponseBody(unittest.TestCase):
    """PkgCpeGetPkgCpeListResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PkgCpeGetPkgCpeListResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PkgCpeGetPkgCpeListResponseBody`
        """
        model = openapiclient.models.pkg_cpe_get_pkg_cpe_list_response_body.PkgCpeGetPkgCpeListResponseBody()  # noqa: E501
        if include_optional :
            return PkgCpeGetPkgCpeListResponseBody(
                paging = {"limit":20,"offset":10,"page":1,"totalCount":200,"totalPage":10}, 
                pkg_cpes = [{"applicationName":"Application","cpeFS":"cpe:2.3:a:clamav:clamav:*:*:*:*:*:*:*:*","cpeID":1,"cpeURI":"cpe:/a:cisco:ios:15.2","createdAt":"2018-07-14T08:13:28Z","githubPkgID":1,"libraryPath":"/FutureVuls/go.sum","libraryPkgID":1,"name":"package01","needRestartProcs":[{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"},{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"},{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"}],"newRelease":"new release","newVersion":"2.0","notFixedYet":true,"ossLicense":"ossLicense","pkgID":1,"release":"14.amzn2","repository":"repository","serverID":1,"serverName":"server01","serverUuid":"abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2","updatedAt":"2018-07-14T08:13:28Z","version":"1.0","wordpressPackageStatus":"wordpressPackageStatus","wordpressPkgID":1},{"applicationName":"Application","cpeFS":"cpe:2.3:a:clamav:clamav:*:*:*:*:*:*:*:*","cpeID":1,"cpeURI":"cpe:/a:cisco:ios:15.2","createdAt":"2018-07-14T08:13:28Z","githubPkgID":1,"libraryPath":"/FutureVuls/go.sum","libraryPkgID":1,"name":"package01","needRestartProcs":[{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"},{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"},{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"}],"newRelease":"new release","newVersion":"2.0","notFixedYet":true,"ossLicense":"ossLicense","pkgID":1,"release":"14.amzn2","repository":"repository","serverID":1,"serverName":"server01","serverUuid":"abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2","updatedAt":"2018-07-14T08:13:28Z","version":"1.0","wordpressPackageStatus":"wordpressPackageStatus","wordpressPkgID":1},{"applicationName":"Application","cpeFS":"cpe:2.3:a:clamav:clamav:*:*:*:*:*:*:*:*","cpeID":1,"cpeURI":"cpe:/a:cisco:ios:15.2","createdAt":"2018-07-14T08:13:28Z","githubPkgID":1,"libraryPath":"/FutureVuls/go.sum","libraryPkgID":1,"name":"package01","needRestartProcs":[{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"},{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"},{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"}],"newRelease":"new release","newVersion":"2.0","notFixedYet":true,"ossLicense":"ossLicense","pkgID":1,"release":"14.amzn2","repository":"repository","serverID":1,"serverName":"server01","serverUuid":"abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2","updatedAt":"2018-07-14T08:13:28Z","version":"1.0","wordpressPackageStatus":"wordpressPackageStatus","wordpressPkgID":1},{"applicationName":"Application","cpeFS":"cpe:2.3:a:clamav:clamav:*:*:*:*:*:*:*:*","cpeID":1,"cpeURI":"cpe:/a:cisco:ios:15.2","createdAt":"2018-07-14T08:13:28Z","githubPkgID":1,"libraryPath":"/FutureVuls/go.sum","libraryPkgID":1,"name":"package01","needRestartProcs":[{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"},{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"},{"initSystem":"initSystem","path":"path","pid":"12","serviceName":"serviceName"}],"newRelease":"new release","newVersion":"2.0","notFixedYet":true,"ossLicense":"ossLicense","pkgID":1,"release":"14.amzn2","repository":"repository","serverID":1,"serverName":"server01","serverUuid":"abcdef12-ecd0-39f4-a8f4-1ef216a4b5f2","updatedAt":"2018-07-14T08:13:28Z","version":"1.0","wordpressPackageStatus":"wordpressPackageStatus","wordpressPkgID":1}]
            )
        else :
            return PkgCpeGetPkgCpeListResponseBody(
        )
        """

    def testPkgCpeGetPkgCpeListResponseBody(self):
        """Test PkgCpeGetPkgCpeListResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
