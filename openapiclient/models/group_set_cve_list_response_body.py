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

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from openapiclient.models.cwe_response_body import CweResponseBody
from openapiclient.models.group_response_body import GroupResponseBody

class GroupSetCveListResponseBody(BaseModel):
    """
    GroupSetCveListResponseBody
    """
    advisory_ids: Optional[conlist(StrictStr)] = Field(None, alias="advisoryIDs", description="advisoryIDs of cve")
    created_at: datetime = Field(..., alias="createdAt", description="created time")
    cve_id: StrictStr = Field(..., alias="cveID", description="Cve ID string of cve")
    cwes: conlist(CweResponseBody) = Field(..., description="cwes of cve")
    groups: conlist(GroupResponseBody) = Field(..., description="Groups including this cve")
    has_exploit: Optional[StrictBool] = Field(None, alias="hasExploit", description="hasExploit of cve")
    has_mitigation: Optional[StrictBool] = Field(None, alias="hasMitigation", description="hasMitigation of cve")
    is_owasp_top_ten2017: StrictBool = Field(..., alias="isOwaspTopTen2017", description="isOwaspTopTen2017 of cve")
    max_v2: StrictFloat = Field(..., alias="maxV2", description="maxV2 of cve")
    max_v3: StrictFloat = Field(..., alias="maxV3", description="maxV3 of cve")
    score_v2s: Dict[str, StrictFloat] = Field(..., alias="scoreV2s", description="cvss v2 scores of cve")
    score_v3s: Dict[str, StrictFloat] = Field(..., alias="scoreV3s", description="cvss v3 scores of cve")
    title: StrictStr = Field(..., description="Title of cve")
    topic_count: StrictInt = Field(..., alias="topicCount", description="topicCount of cve")
    topic_last_updated_at: StrictStr = Field(..., alias="topicLastUpdatedAt", description="topicLastUpdatedAt of cve (default value is \"\")")
    updated_at: datetime = Field(..., alias="updatedAt", description="updated time")
    vector_v2s: Dict[str, StrictStr] = Field(..., alias="vectorV2s", description="cvss v2 vectors of cve")
    vector_v3s: Dict[str, StrictStr] = Field(..., alias="vectorV3s", description="cvss v3 vectors of cve")
    __properties = ["advisoryIDs", "createdAt", "cveID", "cwes", "groups", "hasExploit", "hasMitigation", "isOwaspTopTen2017", "maxV2", "maxV3", "scoreV2s", "scoreV3s", "title", "topicCount", "topicLastUpdatedAt", "updatedAt", "vectorV2s", "vectorV3s"]

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
    def from_json(cls, json_str: str) -> GroupSetCveListResponseBody:
        """Create an instance of GroupSetCveListResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in cwes (list)
        _items = []
        if self.cwes:
            for _item in self.cwes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cwes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item in self.groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['groups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupSetCveListResponseBody:
        """Create an instance of GroupSetCveListResponseBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GroupSetCveListResponseBody.parse_obj(obj)

        _obj = GroupSetCveListResponseBody.parse_obj({
            "advisory_ids": obj.get("advisoryIDs"),
            "created_at": obj.get("createdAt"),
            "cve_id": obj.get("cveID"),
            "cwes": [CweResponseBody.from_dict(_item) for _item in obj.get("cwes")] if obj.get("cwes") is not None else None,
            "groups": [GroupResponseBody.from_dict(_item) for _item in obj.get("groups")] if obj.get("groups") is not None else None,
            "has_exploit": obj.get("hasExploit"),
            "has_mitigation": obj.get("hasMitigation"),
            "is_owasp_top_ten2017": obj.get("isOwaspTopTen2017"),
            "max_v2": obj.get("maxV2"),
            "max_v3": obj.get("maxV3"),
            "score_v2s": obj.get("scoreV2s"),
            "score_v3s": obj.get("scoreV3s"),
            "title": obj.get("title"),
            "topic_count": obj.get("topicCount"),
            "topic_last_updated_at": obj.get("topicLastUpdatedAt"),
            "updated_at": obj.get("updatedAt"),
            "vector_v2s": obj.get("vectorV2s"),
            "vector_v3s": obj.get("vectorV3s")
        })
        return _obj

