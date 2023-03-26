# GroupSetTaskGetGroupSetTaskListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**PagingResponseBody**](PagingResponseBody.md) |  | [optional] 
**tasks** | [**List[TaskListResponseBody]**](TaskListResponseBody.md) | Task list | [optional] 

## Example

```python
from openapiclient.models.group_set_task_get_group_set_task_list_response_body import GroupSetTaskGetGroupSetTaskListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSetTaskGetGroupSetTaskListResponseBody from a JSON string
group_set_task_get_group_set_task_list_response_body_instance = GroupSetTaskGetGroupSetTaskListResponseBody.from_json(json)
# print the JSON string representation of the object
print GroupSetTaskGetGroupSetTaskListResponseBody.to_json()

# convert the object into a dict
group_set_task_get_group_set_task_list_response_body_dict = group_set_task_get_group_set_task_list_response_body_instance.to_dict()
# create an instance of GroupSetTaskGetGroupSetTaskListResponseBody from a dict
group_set_task_get_group_set_task_list_response_body_form_dict = group_set_task_get_group_set_task_list_response_body.from_dict(group_set_task_get_group_set_task_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


