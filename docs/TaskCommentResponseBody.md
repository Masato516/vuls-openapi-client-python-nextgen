# TaskCommentResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment content of TaskComment | 
**created_at** | **datetime** | created time of TaskComment | 
**id** | **int** | ID of TaskComment | 
**type** | **str** | Type of TaskComment | 
**updated_at** | **datetime** | updated time of TaskComment | 
**user_id** | **int** | UserID of TaskComment | 
**user_name** | **str** | UserName of TaskComment | 

## Example

```python
from openapiclient.models.task_comment_response_body import TaskCommentResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCommentResponseBody from a JSON string
task_comment_response_body_instance = TaskCommentResponseBody.from_json(json)
# print the JSON string representation of the object
print TaskCommentResponseBody.to_json()

# convert the object into a dict
task_comment_response_body_dict = task_comment_response_body_instance.to_dict()
# create an instance of TaskCommentResponseBody from a dict
task_comment_response_body_form_dict = task_comment_response_body.from_dict(task_comment_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


