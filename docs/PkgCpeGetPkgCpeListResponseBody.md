# PkgCpeGetPkgCpeListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**PagingResponseBody**](PagingResponseBody.md) |  | [optional] 
**pkg_cpes** | [**List[PkgCpeListResponseBody]**](PkgCpeListResponseBody.md) | PkgCpes list | [optional] 

## Example

```python
from openapiclient.models.pkg_cpe_get_pkg_cpe_list_response_body import PkgCpeGetPkgCpeListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of PkgCpeGetPkgCpeListResponseBody from a JSON string
pkg_cpe_get_pkg_cpe_list_response_body_instance = PkgCpeGetPkgCpeListResponseBody.from_json(json)
# print the JSON string representation of the object
print PkgCpeGetPkgCpeListResponseBody.to_json()

# convert the object into a dict
pkg_cpe_get_pkg_cpe_list_response_body_dict = pkg_cpe_get_pkg_cpe_list_response_body_instance.to_dict()
# create an instance of PkgCpeGetPkgCpeListResponseBody from a dict
pkg_cpe_get_pkg_cpe_list_response_body_form_dict = pkg_cpe_get_pkg_cpe_list_response_body.from_dict(pkg_cpe_get_pkg_cpe_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


