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



from pydantic import BaseModel, Field, StrictInt, StrictStr

class LockfileAddLockfileRequestBody(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    file_content: StrictStr = Field(..., alias="fileContent", description="fileContent of the lockfile (or Base64 string of fileContent)")
    path: StrictStr = Field(..., description="Path of lockfile")
    server_id: StrictInt = Field(..., alias="serverID", description="ServerID")
    __properties = ["fileContent", "path", "serverID"]

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
    def from_json(cls, json_str: str) -> LockfileAddLockfileRequestBody:
        """Create an instance of LockfileAddLockfileRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LockfileAddLockfileRequestBody:
        """Create an instance of LockfileAddLockfileRequestBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return LockfileAddLockfileRequestBody.parse_obj(obj)

        _obj = LockfileAddLockfileRequestBody.parse_obj({
            "file_content": obj.get("fileContent"),
            "path": obj.get("path"),
            "server_id": obj.get("serverID")
        })
        return _obj

