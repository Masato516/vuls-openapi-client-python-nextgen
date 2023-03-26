# ServerUpdateServerRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **str** | Additional information of the server | [optional] 
**default_user_id** | **int** | DefaultUserID of server | [optional] 
**role_id** | **int** | ServerRoleID of server | [optional] 
**server_name** | **str** | ServerName of server | [optional] 

## Example

```python
from openapiclient.models.server_update_server_request_body import ServerUpdateServerRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ServerUpdateServerRequestBody from a JSON string
server_update_server_request_body_instance = ServerUpdateServerRequestBody.from_json(json)
# print the JSON string representation of the object
print ServerUpdateServerRequestBody.to_json()

# convert the object into a dict
server_update_server_request_body_dict = server_update_server_request_body_instance.to_dict()
# create an instance of ServerUpdateServerRequestBody from a dict
server_update_server_request_body_form_dict = server_update_server_request_body.from_dict(server_update_server_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


