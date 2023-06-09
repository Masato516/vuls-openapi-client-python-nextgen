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

from datetime import date, datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from openapiclient.models.cvss_response_body import CvssResponseBody
from openapiclient.models.detection_method_response_body import DetectionMethodResponseBody
from openapiclient.models.detection_tool_response_body import DetectionToolResponseBody
from openapiclient.models.group_response_body import GroupResponseBody
from openapiclient.models.pkg_cpe_child_response_body import PkgCpeChildResponseBody
from openapiclient.models.server_child_response_body import ServerChildResponseBody
from openapiclient.models.task_comment_response_body import TaskCommentResponseBody

class TaskAddTaskCommentResponseBody(BaseModel):
    """
    TaskAddTaskCommentResponseBody
    """
    advisory_ids: Optional[conlist(StrictStr)] = Field(None, alias="advisoryIDs", description="advisoryIDs of cve")
    advisory_primary_src_urls: Optional[Dict[str, StrictStr]] = Field(None, alias="advisoryPrimarySrcURLs", description="advisory primary src")
    applying_patch_on: Optional[date] = Field(None, alias="applyingPatchOn", description="ApplyingPatchOn of task")
    cloud_one_status: Optional[StrictStr] = Field(None, alias="cloudOneStatus", description="cloudone status")
    cloud_one_status_only: Optional[StrictBool] = Field(None, alias="cloudOneStatusOnly", description="only detected by cloudone status")
    comments: Optional[conlist(TaskCommentResponseBody)] = Field(None, description="Comment of task")
    created_at: datetime = Field(..., alias="createdAt", description="created time of task")
    cve_id: StrictStr = Field(..., alias="cveID", description="CVE ID of task")
    cvss: CvssResponseBody = ...
    deadline_on: Optional[date] = Field(None, alias="deadlineOn", description="DeadlineOn of task")
    detection_methods: Optional[conlist(DetectionMethodResponseBody)] = Field(None, alias="detectionMethods", description="DetectionMethod of task")
    detection_tools: Optional[conlist(DetectionToolResponseBody)] = Field(None, alias="detectionTools", description="DetectionTools of task")
    group: Optional[GroupResponseBody] = None
    has_exploit: Optional[StrictBool] = Field(None, alias="hasExploit", description="hasExploit of cve")
    has_mitigation: Optional[StrictBool] = Field(None, alias="hasMitigation", description="hasMitigation of cve")
    id: StrictInt = Field(..., description="ID of task")
    ignore: StrictBool = Field(..., description="Ignore of task")
    ignore_expired_at: Optional[datetime] = Field(None, alias="ignoreExpiredAt", description="the date of ignore expiration")
    ignore_until: Optional[StrictStr] = Field(None, alias="ignoreUntil", description="Ignore until of task")
    is_deadline_on_autochanged: Optional[StrictBool] = Field(None, alias="isDeadlineOnAutochanged", description="DeadlineOn of task")
    is_important: StrictBool = Field(..., alias="isImportant", description="the task is important")
    main_user_id: Optional[StrictInt] = Field(None, alias="mainUserID", description="MainUserID of task")
    main_user_name: Optional[StrictStr] = Field(None, alias="mainUserName", description="MainUserName of task")
    newed_at: datetime = Field(..., alias="newedAt", description="the time when task status became 'new'")
    org_alert_tags: Optional[conlist(StrictStr)] = Field(None, alias="orgAlertTags", description="SpecialAlertTags of task")
    package_statuses: Optional[Dict[str, StrictStr]] = Field(None, alias="packageStatuses", description="packageStatus of task")
    pkg_cpes: Optional[conlist(PkgCpeChildResponseBody)] = Field(None, alias="pkgCpes", description="Pcakge And Cpe list of task")
    primary_src_urls: Optional[Dict[str, conlist(StrictStr)]] = Field(None, alias="primarySrcURLs", description="primary src urls")
    priority: StrictStr = Field(..., description="Priority of task")
    server: ServerChildResponseBody = ...
    ssvc_decision_human_impact: Optional[StrictStr] = Field(None, alias="ssvcDecisionHumanImpact", description="ssvc decisionPoint: human impact")
    ssvc_decision_point_exploitation: Optional[StrictStr] = Field(None, alias="ssvcDecisionPointExploitation", description="ssvc decisionPoint: exploitation")
    ssvc_decision_point_exposure: Optional[StrictStr] = Field(None, alias="ssvcDecisionPointExposure", description="ssvc decisionPoint: exposure")
    ssvc_decision_point_utility: Optional[StrictStr] = Field(None, alias="ssvcDecisionPointUtility", description="ssvc decisionPoint: utility")
    ssvc_decision_point_utility_automatable: Optional[StrictStr] = Field(None, alias="ssvcDecisionPointUtilityAutomatable", description="ssvc decisionPoint: utility.automatable")
    ssvc_decision_point_utility_density: Optional[StrictStr] = Field(None, alias="ssvcDecisionPointUtilityDensity", description="ssvc decisionPoint: utility.density")
    ssvc_priority: Optional[StrictStr] = Field(None, alias="ssvcPriority", description="ssvc priority")
    status: StrictStr = Field(..., description="Status of task")
    sub_user_id: Optional[StrictInt] = Field(None, alias="subUserID", description="SubUserID of task")
    sub_user_name: Optional[StrictStr] = Field(None, alias="subUserName", description="SubUserName of task")
    updated_at: datetime = Field(..., alias="updatedAt", description="updated time of task")
    __properties = ["advisoryIDs", "advisoryPrimarySrcURLs", "applyingPatchOn", "cloudOneStatus", "cloudOneStatusOnly", "comments", "createdAt", "cveID", "cvss", "deadlineOn", "detectionMethods", "detectionTools", "group", "hasExploit", "hasMitigation", "id", "ignore", "ignoreExpiredAt", "ignoreUntil", "isDeadlineOnAutochanged", "isImportant", "mainUserID", "mainUserName", "newedAt", "orgAlertTags", "packageStatuses", "pkgCpes", "primarySrcURLs", "priority", "server", "ssvcDecisionHumanImpact", "ssvcDecisionPointExploitation", "ssvcDecisionPointExposure", "ssvcDecisionPointUtility", "ssvcDecisionPointUtilityAutomatable", "ssvcDecisionPointUtilityDensity", "ssvcPriority", "status", "subUserID", "subUserName", "updatedAt"]

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
    def from_json(cls, json_str: str) -> TaskAddTaskCommentResponseBody:
        """Create an instance of TaskAddTaskCommentResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in comments (list)
        _items = []
        if self.comments:
            for _item in self.comments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['comments'] = _items
        # override the default output from pydantic by calling `to_dict()` of cvss
        if self.cvss:
            _dict['cvss'] = self.cvss.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in detection_methods (list)
        _items = []
        if self.detection_methods:
            for _item in self.detection_methods:
                if _item:
                    _items.append(_item.to_dict())
            _dict['detectionMethods'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in detection_tools (list)
        _items = []
        if self.detection_tools:
            for _item in self.detection_tools:
                if _item:
                    _items.append(_item.to_dict())
            _dict['detectionTools'] = _items
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pkg_cpes (list)
        _items = []
        if self.pkg_cpes:
            for _item in self.pkg_cpes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pkgCpes'] = _items
        # override the default output from pydantic by calling `to_dict()` of server
        if self.server:
            _dict['server'] = self.server.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskAddTaskCommentResponseBody:
        """Create an instance of TaskAddTaskCommentResponseBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TaskAddTaskCommentResponseBody.parse_obj(obj)

        _obj = TaskAddTaskCommentResponseBody.parse_obj({
            "advisory_ids": obj.get("advisoryIDs"),
            "advisory_primary_src_urls": obj.get("advisoryPrimarySrcURLs"),
            "applying_patch_on": obj.get("applyingPatchOn"),
            "cloud_one_status": obj.get("cloudOneStatus"),
            "cloud_one_status_only": obj.get("cloudOneStatusOnly"),
            "comments": [TaskCommentResponseBody.from_dict(_item) for _item in obj.get("comments")] if obj.get("comments") is not None else None,
            "created_at": obj.get("createdAt"),
            "cve_id": obj.get("cveID"),
            "cvss": CvssResponseBody.from_dict(obj.get("cvss")) if obj.get("cvss") is not None else None,
            "deadline_on": obj.get("deadlineOn"),
            "detection_methods": [DetectionMethodResponseBody.from_dict(_item) for _item in obj.get("detectionMethods")] if obj.get("detectionMethods") is not None else None,
            "detection_tools": [DetectionToolResponseBody.from_dict(_item) for _item in obj.get("detectionTools")] if obj.get("detectionTools") is not None else None,
            "group": GroupResponseBody.from_dict(obj.get("group")) if obj.get("group") is not None else None,
            "has_exploit": obj.get("hasExploit"),
            "has_mitigation": obj.get("hasMitigation"),
            "id": obj.get("id"),
            "ignore": obj.get("ignore"),
            "ignore_expired_at": obj.get("ignoreExpiredAt"),
            "ignore_until": obj.get("ignoreUntil"),
            "is_deadline_on_autochanged": obj.get("isDeadlineOnAutochanged"),
            "is_important": obj.get("isImportant"),
            "main_user_id": obj.get("mainUserID"),
            "main_user_name": obj.get("mainUserName"),
            "newed_at": obj.get("newedAt"),
            "org_alert_tags": obj.get("orgAlertTags"),
            "package_statuses": obj.get("packageStatuses"),
            "pkg_cpes": [PkgCpeChildResponseBody.from_dict(_item) for _item in obj.get("pkgCpes")] if obj.get("pkgCpes") is not None else None,
            "primary_src_urls": obj.get("primarySrcURLs"),
            "priority": obj.get("priority"),
            "server": ServerChildResponseBody.from_dict(obj.get("server")) if obj.get("server") is not None else None,
            "ssvc_decision_human_impact": obj.get("ssvcDecisionHumanImpact"),
            "ssvc_decision_point_exploitation": obj.get("ssvcDecisionPointExploitation"),
            "ssvc_decision_point_exposure": obj.get("ssvcDecisionPointExposure"),
            "ssvc_decision_point_utility": obj.get("ssvcDecisionPointUtility"),
            "ssvc_decision_point_utility_automatable": obj.get("ssvcDecisionPointUtilityAutomatable"),
            "ssvc_decision_point_utility_density": obj.get("ssvcDecisionPointUtilityDensity"),
            "ssvc_priority": obj.get("ssvcPriority"),
            "status": obj.get("status"),
            "sub_user_id": obj.get("subUserID"),
            "sub_user_name": obj.get("subUserName"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

