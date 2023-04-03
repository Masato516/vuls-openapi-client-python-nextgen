# coding: utf-8

"""
    Future Vuls Public API

    Future Vuls Public API  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from openapiclient.models.group_response_body import GroupResponseBody
from openapiclient.models.server_tag_response_body import ServerTagResponseBody

class ServerListResponseBody(BaseModel):
    """
    ServerListResponseBody
    """
    created_at: StrictStr = Field(..., alias="createdAt", description="crated time of server")
    default_user_id: Optional[StrictInt] = Field(None, alias="defaultUserId", description="default user ID of server")
    default_user_name: Optional[StrictStr] = Field(None, alias="defaultUserName", description="default user name of server")
    group: Optional[GroupResponseBody] = None
    host_uuid: StrictStr = Field(..., alias="hostUuid", description="UUID of server")
    id: StrictInt = Field(..., description="ID of server")
    last_scanned_at: Optional[StrictStr] = Field(None, alias="lastScannedAt", description="last scanned time of server")
    last_uploaded_at: Optional[StrictStr] = Field(None, alias="lastUploadedAt", description="last uploaded time of server")
    need_kernel_restart: StrictBool = Field(..., alias="needKernelRestart", description="Whether server needs kernel restart")
    os_family: StrictStr = Field(..., alias="osFamily", description="OS Name of server")
    os_version: StrictStr = Field(..., alias="osVersion", description="OS Version of server")
    platform_instance_id: StrictStr = Field(..., alias="platformInstanceId", description="platformInstanceId of server")
    platform_name: StrictStr = Field(..., alias="platformName", description="platformName of server")
    server_ipv4: StrictStr = Field(..., alias="serverIpv4", description="IPv4 of server")
    server_name: StrictStr = Field(..., alias="serverName", description="Name of server")
    server_uuid: StrictStr = Field(..., alias="serverUuid", description="UUID of server")
    serverrole_id: StrictInt = Field(..., alias="serverroleId", description="ID of server role")
    serverrole_name: StrictStr = Field(..., alias="serverroleName", description="Name of server role")
    success_scan_count: Optional[StrictInt] = Field(None, alias="successScanCount", description="successScanCount of server")
    tags: Optional[conlist(ServerTagResponseBody)] = Field(None, description="tags is list of server tag")
    updated_at: StrictStr = Field(..., alias="updatedAt", description="updated time of server")
    __properties = ["createdAt", "defaultUserId", "defaultUserName", "group", "hostUuid", "id", "lastScannedAt", "lastUploadedAt", "needKernelRestart", "osFamily", "osVersion", "platformInstanceId", "platformName", "serverIpv4", "serverName", "serverUuid", "serverroleId", "serverroleName", "successScanCount", "tags", "updatedAt"]

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
    def from_json(cls, json_str: str) -> ServerListResponseBody:
        """Create an instance of ServerListResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServerListResponseBody:
        """Create an instance of ServerListResponseBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ServerListResponseBody.parse_obj(obj)

        _obj = ServerListResponseBody.parse_obj({
            "created_at": obj.get("createdAt"),
            "default_user_id": obj.get("defaultUserId"),
            "default_user_name": obj.get("defaultUserName"),
            "group": GroupResponseBody.from_dict(obj.get("group")) if obj.get("group") is not None else None,
            "host_uuid": obj.get("hostUuid"),
            "id": obj.get("id"),
            "last_scanned_at": obj.get("lastScannedAt"),
            "last_uploaded_at": obj.get("lastUploadedAt"),
            "need_kernel_restart": obj.get("needKernelRestart"),
            "os_family": obj.get("osFamily"),
            "os_version": obj.get("osVersion"),
            "platform_instance_id": obj.get("platformInstanceId"),
            "platform_name": obj.get("platformName"),
            "server_ipv4": obj.get("serverIpv4"),
            "server_name": obj.get("serverName"),
            "server_uuid": obj.get("serverUuid"),
            "serverrole_id": obj.get("serverroleId"),
            "serverrole_name": obj.get("serverroleName"),
            "success_scan_count": obj.get("successScanCount"),
            "tags": [ServerTagResponseBody.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,
            "updated_at": obj.get("updatedAt")
        })
        return _obj

