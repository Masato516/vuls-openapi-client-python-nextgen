# GroupSetServerGetGroupSetServerDetailByUUIDResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | crated time of server | 
**default_user_id** | **int** | default user ID of server | [optional] 
**default_user_name** | **str** | default user name of server | [optional] 
**group** | [**GroupResponseBody**](GroupResponseBody.md) |  | [optional] 
**host_uuid** | **str** | UUID of server | 
**id** | **int** | ID of server | 
**last_scanned_at** | **str** | last scanned time of server | [optional] 
**last_uploaded_at** | **str** | last uploaded time of server | [optional] 
**need_kernel_restart** | **bool** | Whether server needs kernel restart | 
**os_family** | **str** | OS Name of server | 
**os_version** | **str** | OS Version of server | 
**platform_instance_id** | **str** | platformInstanceId of server | 
**platform_name** | **str** | platformName of server | 
**server_ipv4** | **str** | IPv4 of server | 
**server_name** | **str** | Name of server | 
**server_uuid** | **str** | UUID of server | 
**serverrole_id** | **int** | ID of server role | 
**serverrole_name** | **str** | Name of server role | 
**tags** | [**List[ServerTagResponseBody]**](ServerTagResponseBody.md) | tags is list of server tag | [optional] 
**tasks** | [**List[ChildTaskResponseBody]**](ChildTaskResponseBody.md) | tasks of server | [optional] 
**updated_at** | **str** | updated time of server | 

## Example

```python
from openapiclient.models.group_set_server_get_group_set_server_detail_by_uuid_response_body import GroupSetServerGetGroupSetServerDetailByUUIDResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSetServerGetGroupSetServerDetailByUUIDResponseBody from a JSON string
group_set_server_get_group_set_server_detail_by_uuid_response_body_instance = GroupSetServerGetGroupSetServerDetailByUUIDResponseBody.from_json(json)
# print the JSON string representation of the object
print GroupSetServerGetGroupSetServerDetailByUUIDResponseBody.to_json()

# convert the object into a dict
group_set_server_get_group_set_server_detail_by_uuid_response_body_dict = group_set_server_get_group_set_server_detail_by_uuid_response_body_instance.to_dict()
# create an instance of GroupSetServerGetGroupSetServerDetailByUUIDResponseBody from a dict
group_set_server_get_group_set_server_detail_by_uuid_response_body_form_dict = group_set_server_get_group_set_server_detail_by_uuid_response_body.from_dict(group_set_server_get_group_set_server_detail_by_uuid_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


