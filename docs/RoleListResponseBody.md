# RoleListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_task_count** | **int** | AllTaskCount of server role | [optional] 
**created_at** | **datetime** | created time of server role | 
**id** | **int** | ID of server role | 
**is_default** | **bool** | isDefault of server role | 
**name** | **str** | Name of server role | 
**new_task_count** | **int** | NewTaskCount of server role | [optional] 
**sec_metric** | [**SecMetricResponseBody**](SecMetricResponseBody.md) |  | [optional] 
**server_count** | **int** | Server Count of server role | [optional] 
**updated_at** | **datetime** | updated time of server role | 

## Example

```python
from openapiclient.models.role_list_response_body import RoleListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of RoleListResponseBody from a JSON string
role_list_response_body_instance = RoleListResponseBody.from_json(json)
# print the JSON string representation of the object
print RoleListResponseBody.to_json()

# convert the object into a dict
role_list_response_body_dict = role_list_response_body_instance.to_dict()
# create an instance of RoleListResponseBody from a dict
role_list_response_body_form_dict = role_list_response_body.from_dict(role_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


