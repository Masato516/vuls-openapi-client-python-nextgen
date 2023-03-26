# ServerCreatePkgPasteServerRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kernel_release** | **str** | Kernel Release | 
**kernel_version** | **str** | Kernel Version | [optional] 
**os_family** | **str** | Server OS Family | 
**os_version** | **str** | Server OS Version | 
**pkg_paste_text** | **str** | pkg paste text | 
**server_name** | **str** | Server Name | 

## Example

```python
from openapiclient.models.server_create_pkg_paste_server_request_body import ServerCreatePkgPasteServerRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ServerCreatePkgPasteServerRequestBody from a JSON string
server_create_pkg_paste_server_request_body_instance = ServerCreatePkgPasteServerRequestBody.from_json(json)
# print the JSON string representation of the object
print ServerCreatePkgPasteServerRequestBody.to_json()

# convert the object into a dict
server_create_pkg_paste_server_request_body_dict = server_create_pkg_paste_server_request_body_instance.to_dict()
# create an instance of ServerCreatePkgPasteServerRequestBody from a dict
server_create_pkg_paste_server_request_body_form_dict = server_create_pkg_paste_server_request_body.from_dict(server_create_pkg_paste_server_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


