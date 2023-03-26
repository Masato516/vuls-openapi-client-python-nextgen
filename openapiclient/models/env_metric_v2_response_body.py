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

from pydantic import BaseModel, Field, StrictInt, StrictStr

class EnvMetricV2ResponseBody(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    cdp: StrictStr = Field(..., description="CDP of envMetricV2")
    created_at: datetime = Field(..., alias="createdAt", description="created time")
    cve_id: StrictStr = Field(..., alias="cveID", description="CveID of envMetricV2")
    role_id: StrictInt = Field(..., alias="roleID", description="ServerRoleID of envMetricV2")
    role_name: StrictStr = Field(..., alias="roleName", description="ServerRoleName of envMetricV2")
    td: StrictStr = Field(..., description="TD of envMetricV2")
    updated_at: datetime = Field(..., alias="updatedAt", description="updated time")
    __properties = ["cdp", "createdAt", "cveID", "roleID", "roleName", "td", "updatedAt"]

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
    def from_json(cls, json_str: str) -> EnvMetricV2ResponseBody:
        """Create an instance of EnvMetricV2ResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnvMetricV2ResponseBody:
        """Create an instance of EnvMetricV2ResponseBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EnvMetricV2ResponseBody.parse_obj(obj)

        _obj = EnvMetricV2ResponseBody.parse_obj({
            "cdp": obj.get("cdp"),
            "created_at": obj.get("createdAt"),
            "cve_id": obj.get("cveID"),
            "role_id": obj.get("roleID"),
            "role_name": obj.get("roleName"),
            "td": obj.get("td"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

