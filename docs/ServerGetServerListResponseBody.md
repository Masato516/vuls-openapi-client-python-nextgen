# ServerGetServerListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**PagingResponseBody**](PagingResponseBody.md) |  | [optional] 
**servers** | [**List[ServerListResponseBody]**](ServerListResponseBody.md) | Servers list | [optional] 

## Example

```python
from openapiclient.models.server_get_server_list_response_body import ServerGetServerListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ServerGetServerListResponseBody from a JSON string
server_get_server_list_response_body_instance = ServerGetServerListResponseBody.from_json(json)
# print the JSON string representation of the object
print ServerGetServerListResponseBody.to_json()

# convert the object into a dict
server_get_server_list_response_body_dict = server_get_server_list_response_body_instance.to_dict()
# create an instance of ServerGetServerListResponseBody from a dict
server_get_server_list_response_body_form_dict = server_get_server_list_response_body.from_dict(server_get_server_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


