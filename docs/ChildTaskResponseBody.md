# ChildTaskResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applying_patch_on** | **datetime** | ApplyingPatchOn of task | [optional] 
**created_at** | **datetime** | created time of task | 
**cve_id** | **str** | CVE ID of task | 
**id** | **int** | ID of task | 
**ignore** | **bool** | Ignore of task | 
**ignore_until** | **str** | Ignore until of task | [optional] 
**main_user_id** | **int** | MainUserID of task | [optional] 
**main_user_name** | **str** | MainUserName of task | [optional] 
**priority** | **str** | Priority of task | 
**server_id** | **int** | ServerID of task | 
**status** | **str** | Status of task | 
**sub_user_id** | **int** | SubUserID of task | [optional] 
**sub_user_name** | **str** | SubUserName of task | [optional] 
**updated_at** | **datetime** | updated time of task | 

## Example

```python
from openapiclient.models.child_task_response_body import ChildTaskResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChildTaskResponseBody from a JSON string
child_task_response_body_instance = ChildTaskResponseBody.from_json(json)
# print the JSON string representation of the object
print ChildTaskResponseBody.to_json()

# convert the object into a dict
child_task_response_body_dict = child_task_response_body_instance.to_dict()
# create an instance of ChildTaskResponseBody from a dict
child_task_response_body_form_dict = child_task_response_body.from_dict(child_task_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


