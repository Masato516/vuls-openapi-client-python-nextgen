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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from openapiclient.models.library_pkg_child_response_body import LibraryPkgChildResponseBody
from openapiclient.models.server_child_response_body import ServerChildResponseBody

class LockfileListResponseBody(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    created_at: StrictStr = Field(..., alias="createdAt", description="created time of lockfile")
    file_content: StrictStr = Field(..., alias="fileContent", description="FileContent of lockfile")
    id: StrictInt = Field(..., description="ID of lockfile")
    library_pkgs: Optional[List[LibraryPkgChildResponseBody]] = Field(None, alias="libraryPkgs", description="LibraryPkgs of lockfile")
    path: StrictStr = Field(..., description="Path of lockfile")
    server: Optional[ServerChildResponseBody] = None
    updated_at: StrictStr = Field(..., alias="updatedAt", description="updated time of lockfile")
    __properties = ["createdAt", "fileContent", "id", "libraryPkgs", "path", "server", "updatedAt"]

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
    def from_json(cls, json_str: str) -> LockfileListResponseBody:
        """Create an instance of LockfileListResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in library_pkgs (list)
        _items = []
        if self.library_pkgs:
            for _item in self.library_pkgs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['libraryPkgs'] = _items
        # override the default output from pydantic by calling `to_dict()` of server
        if self.server:
            _dict['server'] = self.server.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LockfileListResponseBody:
        """Create an instance of LockfileListResponseBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return LockfileListResponseBody.parse_obj(obj)

        _obj = LockfileListResponseBody.parse_obj({
            "created_at": obj.get("createdAt"),
            "file_content": obj.get("fileContent"),
            "id": obj.get("id"),
            "library_pkgs": [LibraryPkgChildResponseBody.from_dict(_item) for _item in obj.get("libraryPkgs")] if obj.get("libraryPkgs") is not None else None,
            "path": obj.get("path"),
            "server": ServerChildResponseBody.from_dict(obj.get("server")) if obj.get("server") is not None else None,
            "updated_at": obj.get("updatedAt")
        })
        return _obj

