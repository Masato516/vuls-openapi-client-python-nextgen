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
from pydantic import BaseModel, Field, StrictStr
from openapiclient.models.cvss_response_body import CvssResponseBody
from openapiclient.models.cwe_response_body import CweResponseBody
from openapiclient.models.group_response_body import GroupResponseBody

class GroupSetCveGetGroupSetCveDetailResponseBody(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    created_at: datetime = Field(..., alias="createdAt", description="created time")
    cve_id: StrictStr = Field(..., alias="cveID", description="Cve ID string of cve")
    cvss: CvssResponseBody = ...
    cwes: List[CweResponseBody] = Field(..., description="cwes of cve")
    group: Optional[GroupResponseBody] = None
    updated_at: datetime = Field(..., alias="updatedAt", description="updated time")
    __properties = ["createdAt", "cveID", "cvss", "cwes", "group", "updatedAt"]

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
    def from_json(cls, json_str: str) -> GroupSetCveGetGroupSetCveDetailResponseBody:
        """Create an instance of GroupSetCveGetGroupSetCveDetailResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cvss
        if self.cvss:
            _dict['cvss'] = self.cvss.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in cwes (list)
        _items = []
        if self.cwes:
            for _item in self.cwes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cwes'] = _items
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupSetCveGetGroupSetCveDetailResponseBody:
        """Create an instance of GroupSetCveGetGroupSetCveDetailResponseBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GroupSetCveGetGroupSetCveDetailResponseBody.parse_obj(obj)

        _obj = GroupSetCveGetGroupSetCveDetailResponseBody.parse_obj({
            "created_at": obj.get("createdAt"),
            "cve_id": obj.get("cveID"),
            "cvss": CvssResponseBody.from_dict(obj.get("cvss")) if obj.get("cvss") is not None else None,
            "cwes": [CweResponseBody.from_dict(_item) for _item in obj.get("cwes")] if obj.get("cwes") is not None else None,
            "group": GroupResponseBody.from_dict(obj.get("group")) if obj.get("group") is not None else None,
            "updated_at": obj.get("updatedAt")
        })
        return _obj

