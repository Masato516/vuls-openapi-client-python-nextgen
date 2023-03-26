# ServerChildResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | crated time of server | 
**default_user_id** | **int** | default user ID of server | [optional] 
**default_user_name** | **str** | default user name of server | [optional] 
**host_uuid** | **str** | UUID of server | 
**id** | **int** | ID of server | 
**last_scanned_at** | **str** | last scanned time of server | [optional] 
**last_uploaded_at** | **str** | last uploaded time of server | [optional] 
**need_kernel_restart** | **bool** | Whether server needs kernel restart | 
**os_family** | **str** | OS Name of server | 
**os_version** | **str** | OS Version of server | 
**server_name** | **str** | Name of server | 
**server_uuid** | **str** | UUID of server | 
**serverrole_id** | **int** | ID of server role | 
**serverrole_name** | **str** | Name of server role | 
**tags** | **List[str]** | tags is list of server tag | [optional] 
**updated_at** | **str** | updated time of server | 

## Example

```python
from openapiclient.models.server_child_response_body import ServerChildResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ServerChildResponseBody from a JSON string
server_child_response_body_instance = ServerChildResponseBody.from_json(json)
# print the JSON string representation of the object
print ServerChildResponseBody.to_json()

# convert the object into a dict
server_child_response_body_dict = server_child_response_body_instance.to_dict()
# create an instance of ServerChildResponseBody from a dict
server_child_response_body_form_dict = server_child_response_body.from_dict(server_child_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


