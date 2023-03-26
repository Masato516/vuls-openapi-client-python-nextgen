# GroupSetServerGetGroupSetServerListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**PagingResponseBody**](PagingResponseBody.md) |  | [optional] 
**servers** | [**List[ServerListResponseBody]**](ServerListResponseBody.md) | Servers list | [optional] 

## Example

```python
from openapiclient.models.group_set_server_get_group_set_server_list_response_body import GroupSetServerGetGroupSetServerListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSetServerGetGroupSetServerListResponseBody from a JSON string
group_set_server_get_group_set_server_list_response_body_instance = GroupSetServerGetGroupSetServerListResponseBody.from_json(json)
# print the JSON string representation of the object
print GroupSetServerGetGroupSetServerListResponseBody.to_json()

# convert the object into a dict
group_set_server_get_group_set_server_list_response_body_dict = group_set_server_get_group_set_server_list_response_body_instance.to_dict()
# create an instance of GroupSetServerGetGroupSetServerListResponseBody from a dict
group_set_server_get_group_set_server_list_response_body_form_dict = group_set_server_get_group_set_server_list_response_body.from_dict(group_set_server_get_group_set_server_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


