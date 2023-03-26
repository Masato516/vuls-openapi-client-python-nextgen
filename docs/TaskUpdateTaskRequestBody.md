# TaskUpdateTaskRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applying_patch_on** | **date** | applyingPatchOn (YYYY-MM-DD) UTC | [optional] 
**main_user_id** | **int** | mainUserID of task | [optional] 
**priority** | **str** | Priority of task | [optional] 
**status** | **str** | Status of task | [optional] 
**sub_user_id** | **int** | subUserID of task | [optional] 

## Example

```python
from openapiclient.models.task_update_task_request_body import TaskUpdateTaskRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaskUpdateTaskRequestBody from a JSON string
task_update_task_request_body_instance = TaskUpdateTaskRequestBody.from_json(json)
# print the JSON string representation of the object
print TaskUpdateTaskRequestBody.to_json()

# convert the object into a dict
task_update_task_request_body_dict = task_update_task_request_body_instance.to_dict()
# create an instance of TaskUpdateTaskRequestBody from a dict
task_update_task_request_body_form_dict = task_update_task_request_body.from_dict(task_update_task_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


