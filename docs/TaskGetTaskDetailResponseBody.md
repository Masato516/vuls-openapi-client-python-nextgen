# TaskGetTaskDetailResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_ids** | **List[str]** | advisoryIDs of cve | [optional] 
**advisory_primary_src_urls** | **Dict[str, str]** | advisory primary src | [optional] 
**applying_patch_on** | **date** | ApplyingPatchOn of task | [optional] 
**cloud_one_status** | **str** | cloudone status | [optional] 
**cloud_one_status_only** | **bool** | only detected by cloudone status | [optional] 
**comments** | [**List[TaskCommentResponseBody]**](TaskCommentResponseBody.md) | Comment of task | [optional] 
**created_at** | **datetime** | created time of task | 
**cve_id** | **str** | CVE ID of task | 
**cvss** | [**CvssResponseBody**](CvssResponseBody.md) |  | 
**deadline_on** | **date** | DeadlineOn of task | [optional] 
**detection_methods** | [**List[DetectionMethodResponseBody]**](DetectionMethodResponseBody.md) | DetectionMethod of task | [optional] 
**detection_tools** | [**List[DetectionToolResponseBody]**](DetectionToolResponseBody.md) | DetectionTools of task | [optional] 
**group** | [**GroupResponseBody**](GroupResponseBody.md) |  | [optional] 
**has_exploit** | **bool** | hasExploit of cve | [optional] 
**has_mitigation** | **bool** | hasMitigation of cve | [optional] 
**id** | **int** | ID of task | 
**ignore** | **bool** | Ignore of task | 
**ignore_expired_at** | **datetime** | the date of ignore expiration | [optional] 
**ignore_until** | **str** | Ignore until of task | [optional] 
**is_deadline_on_autochanged** | **bool** | DeadlineOn of task | [optional] 
**is_important** | **bool** | the task is important | 
**main_user_id** | **int** | MainUserID of task | [optional] 
**main_user_name** | **str** | MainUserName of task | [optional] 
**newed_at** | **datetime** | the time when task status became &#39;new&#39; | 
**org_alert_tags** | **List[str]** | SpecialAlertTags of task | [optional] 
**package_statuses** | **Dict[str, str]** | packageStatus of task | [optional] 
**pkg_cpes** | [**List[PkgCpeChildResponseBody]**](PkgCpeChildResponseBody.md) | Pcakge And Cpe list of task | [optional] 
**primary_src_urls** | **Dict[str, List[str]]** | primary src urls | [optional] 
**priority** | **str** | Priority of task | 
**server** | [**ServerChildResponseBody**](ServerChildResponseBody.md) |  | 
**ssvc_decision_human_impact** | **str** | ssvc decisionPoint: human impact | [optional] 
**ssvc_decision_point_exploitation** | **str** | ssvc decisionPoint: exploitation | [optional] 
**ssvc_decision_point_exposure** | **str** | ssvc decisionPoint: exposure | [optional] 
**ssvc_decision_point_utility** | **str** | ssvc decisionPoint: utility | [optional] 
**ssvc_decision_point_utility_automatable** | **str** | ssvc decisionPoint: utility.automatable | [optional] 
**ssvc_decision_point_utility_density** | **str** | ssvc decisionPoint: utility.density | [optional] 
**ssvc_priority** | **str** | ssvc priority | [optional] 
**status** | **str** | Status of task | 
**sub_user_id** | **int** | SubUserID of task | [optional] 
**sub_user_name** | **str** | SubUserName of task | [optional] 
**updated_at** | **datetime** | updated time of task | 

## Example

```python
from openapiclient.models.task_get_task_detail_response_body import TaskGetTaskDetailResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaskGetTaskDetailResponseBody from a JSON string
task_get_task_detail_response_body_instance = TaskGetTaskDetailResponseBody.from_json(json)
# print the JSON string representation of the object
print TaskGetTaskDetailResponseBody.to_json()

# convert the object into a dict
task_get_task_detail_response_body_dict = task_get_task_detail_response_body_instance.to_dict()
# create an instance of TaskGetTaskDetailResponseBody from a dict
task_get_task_detail_response_body_form_dict = task_get_task_detail_response_body.from_dict(task_get_task_detail_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


