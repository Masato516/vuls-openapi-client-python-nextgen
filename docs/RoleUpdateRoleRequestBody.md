# RoleUpdateRoleRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | RoleName of role | [optional] 

## Example

```python
from openapiclient.models.role_update_role_request_body import RoleUpdateRoleRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of RoleUpdateRoleRequestBody from a JSON string
role_update_role_request_body_instance = RoleUpdateRoleRequestBody.from_json(json)
# print the JSON string representation of the object
print RoleUpdateRoleRequestBody.to_json()

# convert the object into a dict
role_update_role_request_body_dict = role_update_role_request_body_instance.to_dict()
# create an instance of RoleUpdateRoleRequestBody from a dict
role_update_role_request_body_form_dict = role_update_role_request_body.from_dict(role_update_role_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


