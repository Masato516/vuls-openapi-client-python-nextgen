# TaskListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_running_process** | **bool** | プロセスが実行中かどうか | [optional] 
**advisory_ids** | **List[str]** | advisoryIDs of cve | 
**applying_patch_on** | **datetime** | ApplyingPatchOn of task | [optional] 
**cloud_one_detect_only** | **bool** | CloudOneでのみ検知した脆弱性かどうか | [optional] 
**cloud_one_status** | **str** | status of cloudone | [optional] 
**created_at** | **datetime** | created time of task | 
**cve** | [**CveChildResponseBody**](CveChildResponseBody.md) |  | [optional] 
**cve_id** | **str** | CVE ID of task | 
**deadline_on** | **date** | deadline of task | [optional] 
**detection_methods** | [**List[DetectionMethodResponseBody]**](DetectionMethodResponseBody.md) | DetectionMethods of task | 
**detection_tools** | [**List[DetectionToolResponseBody]**](DetectionToolResponseBody.md) | DetectionTools of task | 
**exploit_level** | **str** | exploit level of cve | [optional] 
**group** | [**GroupResponseBody**](GroupResponseBody.md) |  | [optional] 
**has_danger** | **bool** | Dangerフラグが付与されているかどうか | 
**has_exploit** | **bool** | hasExploit of cve | [optional] 
**has_mitigation** | **bool** | hasMitigation of cve | [optional] 
**id** | **int** | ID of task | 
**ignore** | **bool** | Ignore of task | 
**ignore_expired_at** | **datetime** | the date of ignore expiration | [optional] 
**ignore_until** | **str** | Ignore until of task | [optional] 
**is_important** | **bool** | 重要フィルターに該当するかどうか | 
**listening_ports** | **List[str]** | listened ports | 
**main_user_id** | **int** | MainUserID of task | [optional] 
**main_user_name** | **str** | MainUserName of task | [optional] 
**newed_at** | **datetime** | the time when task status became &#39;new&#39; | 
**org_alert_tags** | **List[str]** | SpecialAlertTags of task | [optional] 
**os_family** | **str** | OS Name of server | 
**os_version** | **str** | OS Version of server | 
**pkg_cpe_names** | **List[str]** | Package And CPE Names of task | [optional] 
**pkg_fixed_status** | **str** | fix status of package | [optional] 
**pkg_fixed_status_names** | **str** | fix status name of package | [optional] 
**priority** | **str** | Priority of task | 
**server** | [**ServerChildResponseBody**](ServerChildResponseBody.md) |  | [optional] 
**server_id** | **int** | ServerID of task | 
**server_name** | **str** | ServerName of task | 
**server_tags** | **List[str]** | ServerTags of task | [optional] 
**server_uuid** | **str** | ServerUUID of task | 
**ssvc_priority** | **str** | SSVCPriority | [optional] 
**status** | **str** | Status of task | 
**sub_user_id** | **int** | SubUserID of task | [optional] 
**sub_user_name** | **str** | SubUserName of task | [optional] 
**updatable_pkg_cpe_names** | **List[str]** | Updatable Package And CPE Names of task | [optional] 
**updated_at** | **datetime** | updated time of task | 
**vuln_info** | [**VulnSummaryResponseBody**](VulnSummaryResponseBody.md) |  | [optional] 

## Example

```python
from openapiclient.models.task_list_response_body import TaskListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaskListResponseBody from a JSON string
task_list_response_body_instance = TaskListResponseBody.from_json(json)
# print the JSON string representation of the object
print TaskListResponseBody.to_json()

# convert the object into a dict
task_list_response_body_dict = task_list_response_body_instance.to_dict()
# create an instance of TaskListResponseBody from a dict
task_list_response_body_form_dict = task_list_response_body.from_dict(task_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


