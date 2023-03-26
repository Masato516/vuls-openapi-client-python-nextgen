# coding: utf-8

"""
    Future Vuls Public API

    Future Vuls Public API  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from openapiclient.models.group_response_body import GroupResponseBody
from openapiclient.models.need_restart_proc_response_body import NeedRestartProcResponseBody

class GroupSetPkgCpeListResponseBody(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    application_name: Optional[StrictStr] = Field(None, alias="applicationName", description="ApplicationName of library package")
    cpe_fs: Optional[StrictStr] = Field(None, alias="cpeFS", description="Cpe FS of cpe")
    cpe_id: Optional[StrictInt] = Field(None, alias="cpeID", description="CpeID of cpe")
    cpe_uri: Optional[StrictStr] = Field(None, alias="cpeURI", description="Cpe URI of cpe")
    created_at: datetime = Field(..., alias="createdAt", description="crated time of package or cpe")
    github_pkg_id: Optional[StrictInt] = Field(None, alias="githubPkgID", description="githubPKGID of github pkg")
    group: GroupResponseBody = ...
    library_path: Optional[StrictStr] = Field(None, alias="libraryPath", description="LibraryPath of library package")
    library_pkg_id: Optional[StrictInt] = Field(None, alias="libraryPkgID", description="libraryPKGID of library pkg")
    name: StrictStr = Field(..., description="Name of package or cpe")
    need_restart_procs: Optional[List[NeedRestartProcResponseBody]] = Field(None, alias="needRestartProcs", description="NeedRestartProcess list of package")
    new_release: Optional[StrictStr] = Field(None, alias="newRelease", description="New Release of package")
    new_version: Optional[StrictStr] = Field(None, alias="newVersion", description="New Version of package")
    not_fixed_yet: Optional[StrictBool] = Field(None, alias="notFixedYet", description="Flag of Not fixed yet of package")
    oss_license: Optional[StrictStr] = Field(None, alias="ossLicense", description="ossLicense of library package")
    pkg_id: Optional[StrictInt] = Field(None, alias="pkgID", description="Package ID of package")
    release: Optional[StrictStr] = Field(None, description="Release of package")
    repository: Optional[StrictStr] = Field(None, description="Repository of package")
    server_id: StrictInt = Field(..., alias="serverID", description="ServerID of package or cpe")
    server_name: StrictStr = Field(..., alias="serverName", description="ServerName of package or cpe")
    server_uuid: StrictStr = Field(..., alias="serverUuid", description="ServerUUID of package or cpe")
    updated_at: datetime = Field(..., alias="updatedAt", description="updated time of package or cpe")
    version: StrictStr = Field(..., description="Version of package or cpe")
    wordpress_package_status: Optional[StrictStr] = Field(None, alias="wordpressPackageStatus", description="WordpressPackageStatus of wordpress package")
    wordpress_pkg_id: Optional[StrictInt] = Field(None, alias="wordpressPkgID", description="wordpressPKGID of wordpress pkg")
    __properties = ["applicationName", "cpeFS", "cpeID", "cpeURI", "createdAt", "githubPkgID", "group", "libraryPath", "libraryPkgID", "name", "needRestartProcs", "newRelease", "newVersion", "notFixedYet", "ossLicense", "pkgID", "release", "repository", "serverID", "serverName", "serverUuid", "updatedAt", "version", "wordpressPackageStatus", "wordpressPkgID"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GroupSetPkgCpeListResponseBody:
        """Create an instance of GroupSetPkgCpeListResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in need_restart_procs (list)
        _items = []
        if self.need_restart_procs:
            for _item in self.need_restart_procs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['needRestartProcs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupSetPkgCpeListResponseBody:
        """Create an instance of GroupSetPkgCpeListResponseBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GroupSetPkgCpeListResponseBody.parse_obj(obj)

        _obj = GroupSetPkgCpeListResponseBody.parse_obj({
            "application_name": obj.get("applicationName"),
            "cpe_fs": obj.get("cpeFS"),
            "cpe_id": obj.get("cpeID"),
            "cpe_uri": obj.get("cpeURI"),
            "created_at": obj.get("createdAt"),
            "github_pkg_id": obj.get("githubPkgID"),
            "group": GroupResponseBody.from_dict(obj.get("group")) if obj.get("group") is not None else None,
            "library_path": obj.get("libraryPath"),
            "library_pkg_id": obj.get("libraryPkgID"),
            "name": obj.get("name"),
            "need_restart_procs": [NeedRestartProcResponseBody.from_dict(_item) for _item in obj.get("needRestartProcs")] if obj.get("needRestartProcs") is not None else None,
            "new_release": obj.get("newRelease"),
            "new_version": obj.get("newVersion"),
            "not_fixed_yet": obj.get("notFixedYet"),
            "oss_license": obj.get("ossLicense"),
            "pkg_id": obj.get("pkgID"),
            "release": obj.get("release"),
            "repository": obj.get("repository"),
            "server_id": obj.get("serverID"),
            "server_name": obj.get("serverName"),
            "server_uuid": obj.get("serverUuid"),
            "updated_at": obj.get("updatedAt"),
            "version": obj.get("version"),
            "wordpress_package_status": obj.get("wordpressPackageStatus"),
            "wordpress_pkg_id": obj.get("wordpressPkgID")
        })
        return _obj

