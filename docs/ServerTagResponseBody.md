# ServerTagResponseBody

ServerTag describes a server tag

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of server tag | 
**name** | **str** | Name of server tag | 

## Example

```python
from openapiclient.models.server_tag_response_body import ServerTagResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ServerTagResponseBody from a JSON string
server_tag_response_body_instance = ServerTagResponseBody.from_json(json)
# print the JSON string representation of the object
print ServerTagResponseBody.to_json()

# convert the object into a dict
server_tag_response_body_dict = server_tag_response_body_instance.to_dict()
# create an instance of ServerTagResponseBody from a dict
server_tag_response_body_form_dict = server_tag_response_body.from_dict(server_tag_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


