# LibraryPkgChildResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | crated time of package or cpe | 
**id** | **int** | ID of library package | 
**name** | **str** | Name of library package | 
**updated_at** | **datetime** | updated time of package or cpe | 
**version** | **str** | Version of library package | 

## Example

```python
from openapiclient.models.library_pkg_child_response_body import LibraryPkgChildResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryPkgChildResponseBody from a JSON string
library_pkg_child_response_body_instance = LibraryPkgChildResponseBody.from_json(json)
# print the JSON string representation of the object
print LibraryPkgChildResponseBody.to_json()

# convert the object into a dict
library_pkg_child_response_body_dict = library_pkg_child_response_body_instance.to_dict()
# create an instance of LibraryPkgChildResponseBody from a dict
library_pkg_child_response_body_form_dict = library_pkg_child_response_body.from_dict(library_pkg_child_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


