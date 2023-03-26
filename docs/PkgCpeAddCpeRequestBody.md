# PkgCpeAddCpeRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe_name** | **str** | Cpe Name(cpe uri or cpe format string) | 
**is_uri** | **bool** | isURI specifies whether cpeName is in URI format or FormatString format. | [optional] [default to True]
**server_id** | **int** | ServerID | 

## Example

```python
from openapiclient.models.pkg_cpe_add_cpe_request_body import PkgCpeAddCpeRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of PkgCpeAddCpeRequestBody from a JSON string
pkg_cpe_add_cpe_request_body_instance = PkgCpeAddCpeRequestBody.from_json(json)
# print the JSON string representation of the object
print PkgCpeAddCpeRequestBody.to_json()

# convert the object into a dict
pkg_cpe_add_cpe_request_body_dict = pkg_cpe_add_cpe_request_body_instance.to_dict()
# create an instance of PkgCpeAddCpeRequestBody from a dict
pkg_cpe_add_cpe_request_body_form_dict = pkg_cpe_add_cpe_request_body.from_dict(pkg_cpe_add_cpe_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


