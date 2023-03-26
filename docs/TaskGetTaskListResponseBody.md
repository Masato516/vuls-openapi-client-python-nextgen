# TaskGetTaskListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**PagingResponseBody**](PagingResponseBody.md) |  | [optional] 
**tasks** | [**List[TaskListResponseBody]**](TaskListResponseBody.md) | Task list | [optional] 

## Example

```python
from openapiclient.models.task_get_task_list_response_body import TaskGetTaskListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaskGetTaskListResponseBody from a JSON string
task_get_task_list_response_body_instance = TaskGetTaskListResponseBody.from_json(json)
# print the JSON string representation of the object
print TaskGetTaskListResponseBody.to_json()

# convert the object into a dict
task_get_task_list_response_body_dict = task_get_task_list_response_body_instance.to_dict()
# create an instance of TaskGetTaskListResponseBody from a dict
task_get_task_list_response_body_form_dict = task_get_task_list_response_body.from_dict(task_get_task_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


