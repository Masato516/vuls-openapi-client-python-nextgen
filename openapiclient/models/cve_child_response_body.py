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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictStr, conlist
from openapiclient.models.cwe_response_body import CweResponseBody

class CveChildResponseBody(BaseModel):
    """
    CveChildResponseBody
    """
    advisory_ids: conlist(StrictStr) = Field(..., alias="advisoryIDs", description="advisoryIDs of cve")
    cve_id: StrictStr = Field(..., alias="cveID", description="Cve ID string of cve")
    cwes: conlist(CweResponseBody) = Field(..., description="cwes of cve")
    exploit_level: Optional[StrictStr] = Field(None, alias="exploitLevel", description="exploitLevel")
    has_exploit: Optional[StrictBool] = Field(None, alias="hasExploit", description="hasExploit of cve")
    has_mitigation: Optional[StrictBool] = Field(None, alias="hasMitigation", description="hasMitigation of cve")
    is_owasp_top_ten2017: StrictBool = Field(..., alias="isOwaspTopTen2017", description="isOwaspTopTen2017 of cve")
    max_v2: StrictFloat = Field(..., alias="maxV2", description="maxV2 of cve")
    max_v3: StrictFloat = Field(..., alias="maxV3", description="maxV3 of cve")
    pkg_fixed_status: Optional[StrictStr] = Field(None, alias="pkgFixedStatus", description="pkgFixStatus")
    pkg_fixed_status_name: Optional[StrictStr] = Field(None, alias="pkgFixedStatusName", description="pkgFixStatusName")
    score_v2s: Dict[str, StrictFloat] = Field(..., alias="scoreV2s", description="cvss v2 scores of cve")
    score_v3s: Dict[str, StrictFloat] = Field(..., alias="scoreV3s", description="cvss v3 scores of cve")
    title: StrictStr = Field(..., description="Title of cve")
    vector_v2s: Dict[str, StrictStr] = Field(..., alias="vectorV2s", description="cvss v2 vectors of cve")
    vector_v3s: Dict[str, StrictStr] = Field(..., alias="vectorV3s", description="cvss v3 vectors of cve")
    __properties = ["advisoryIDs", "cveID", "cwes", "exploitLevel", "hasExploit", "hasMitigation", "isOwaspTopTen2017", "maxV2", "maxV3", "pkgFixedStatus", "pkgFixedStatusName", "scoreV2s", "scoreV3s", "title", "vectorV2s", "vectorV3s"]

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
    def from_json(cls, json_str: str) -> CveChildResponseBody:
        """Create an instance of CveChildResponseBody from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CveChildResponseBody:
        """Create an instance of CveChildResponseBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CveChildResponseBody.parse_obj(obj)

        _obj = CveChildResponseBody.parse_obj({
            "advisory_ids": obj.get("advisoryIDs"),
            "cve_id": obj.get("cveID"),
            "cwes": [CweResponseBody.from_dict(_item) for _item in obj.get("cwes")] if obj.get("cwes") is not None else None,
            "exploit_level": obj.get("exploitLevel"),
            "has_exploit": obj.get("hasExploit"),
            "has_mitigation": obj.get("hasMitigation"),
            "is_owasp_top_ten2017": obj.get("isOwaspTopTen2017"),
            "max_v2": obj.get("maxV2"),
            "max_v3": obj.get("maxV3"),
            "pkg_fixed_status": obj.get("pkgFixedStatus"),
            "pkg_fixed_status_name": obj.get("pkgFixedStatusName"),
            "score_v2s": obj.get("scoreV2s"),
            "score_v3s": obj.get("scoreV3s"),
            "title": obj.get("title"),
            "vector_v2s": obj.get("vectorV2s"),
            "vector_v3s": obj.get("vectorV3s")
        })
        return _obj

