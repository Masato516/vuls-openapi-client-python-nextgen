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
from pydantic import BaseModel, Field
from openapiclient.models.paging_response_body import PagingResponseBody
from openapiclient.models.server_list_response_body import ServerListResponseBody

class ServerGetServerListResponseBody(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    paging: Optional[PagingResponseBody] = None
    servers: Optional[List[ServerListResponseBody]] = Field(None, description="Servers list")
    __properties = ["paging", "servers"]

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
    def from_json(cls, json_str: str) -> ServerGetServerListResponseBody:
        """Create an instance of ServerGetServerListResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of paging
        if self.paging:
            _dict['paging'] = self.paging.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in servers (list)
        _items = []
        if self.servers:
            for _item in self.servers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['servers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServerGetServerListResponseBody:
        """Create an instance of ServerGetServerListResponseBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ServerGetServerListResponseBody.parse_obj(obj)

        _obj = ServerGetServerListResponseBody.parse_obj({
            "paging": PagingResponseBody.from_dict(obj.get("paging")) if obj.get("paging") is not None else None,
            "servers": [ServerListResponseBody.from_dict(_item) for _item in obj.get("servers")] if obj.get("servers") is not None else None
        })
        return _obj

