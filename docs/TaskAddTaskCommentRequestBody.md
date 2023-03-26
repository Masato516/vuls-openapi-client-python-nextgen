# TaskAddTaskCommentRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_content** | **str** | comment content | 

## Example

```python
from openapiclient.models.task_add_task_comment_request_body import TaskAddTaskCommentRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaskAddTaskCommentRequestBody from a JSON string
task_add_task_comment_request_body_instance = TaskAddTaskCommentRequestBody.from_json(json)
# print the JSON string representation of the object
print TaskAddTaskCommentRequestBody.to_json()

# convert the object into a dict
task_add_task_comment_request_body_dict = task_add_task_comment_request_body_instance.to_dict()
# create an instance of TaskAddTaskCommentRequestBody from a dict
task_add_task_comment_request_body_form_dict = task_add_task_comment_request_body.from_dict(task_add_task_comment_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


