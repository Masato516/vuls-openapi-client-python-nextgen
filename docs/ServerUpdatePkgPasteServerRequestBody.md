# ServerUpdatePkgPasteServerRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kernel_release** | **str** | Kernel Release | [optional] 
**kernel_version** | **str** | Kernel Version | [optional] 
**os_version** | **str** | Server OS Version | [optional] 
**pkg_paste_text** | **str** | pkg paste text | 

## Example

```python
from openapiclient.models.server_update_pkg_paste_server_request_body import ServerUpdatePkgPasteServerRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ServerUpdatePkgPasteServerRequestBody from a JSON string
server_update_pkg_paste_server_request_body_instance = ServerUpdatePkgPasteServerRequestBody.from_json(json)
# print the JSON string representation of the object
print ServerUpdatePkgPasteServerRequestBody.to_json()

# convert the object into a dict
server_update_pkg_paste_server_request_body_dict = server_update_pkg_paste_server_request_body_instance.to_dict()
# create an instance of ServerUpdatePkgPasteServerRequestBody from a dict
server_update_pkg_paste_server_request_body_form_dict = server_update_pkg_paste_server_request_body.from_dict(server_update_pkg_paste_server_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


