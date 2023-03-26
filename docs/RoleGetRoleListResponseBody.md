# RoleGetRoleListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**PagingResponseBody**](PagingResponseBody.md) |  | [optional] 
**roles** | [**List[RoleListResponseBody]**](RoleListResponseBody.md) | ServerRole list | [optional] 

## Example

```python
from openapiclient.models.role_get_role_list_response_body import RoleGetRoleListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of RoleGetRoleListResponseBody from a JSON string
role_get_role_list_response_body_instance = RoleGetRoleListResponseBody.from_json(json)
# print the JSON string representation of the object
print RoleGetRoleListResponseBody.to_json()

# convert the object into a dict
role_get_role_list_response_body_dict = role_get_role_list_response_body_instance.to_dict()
# create an instance of RoleGetRoleListResponseBody from a dict
role_get_role_list_response_body_form_dict = role_get_role_list_response_body.from_dict(role_get_role_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


