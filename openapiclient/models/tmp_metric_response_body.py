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

from pydantic import BaseModel, Field, StrictStr

class TmpMetricResponseBody(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    created_at: datetime = Field(..., alias="createdAt", description="created time")
    e: StrictStr = Field(..., description="E of tmpMetric")
    rc: StrictStr = Field(..., description="RC of tmpMetric")
    rl: StrictStr = Field(..., description="RL of tmpMetric")
    updated_at: datetime = Field(..., alias="updatedAt", description="updated time")
    __properties = ["createdAt", "e", "rc", "rl", "updatedAt"]

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
    def from_json(cls, json_str: str) -> TmpMetricResponseBody:
        """Create an instance of TmpMetricResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TmpMetricResponseBody:
        """Create an instance of TmpMetricResponseBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TmpMetricResponseBody.parse_obj(obj)

        _obj = TmpMetricResponseBody.parse_obj({
            "created_at": obj.get("createdAt"),
            "e": obj.get("e"),
            "rc": obj.get("rc"),
            "rl": obj.get("rl"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj
