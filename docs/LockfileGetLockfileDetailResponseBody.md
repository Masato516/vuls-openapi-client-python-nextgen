# LockfileGetLockfileDetailResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | created time of lockfile | 
**file_content** | **str** | FileContent of lockfile | 
**id** | **int** | ID of lockfile | 
**library_pkgs** | [**List[LibraryPkgChildResponseBody]**](LibraryPkgChildResponseBody.md) | LibraryPkgs of lockfile | [optional] 
**path** | **str** | Path of lockfile | 
**server** | [**ServerChildResponseBody**](ServerChildResponseBody.md) |  | [optional] 
**updated_at** | **str** | updated time of lockfile | 

## Example

```python
from openapiclient.models.lockfile_get_lockfile_detail_response_body import LockfileGetLockfileDetailResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of LockfileGetLockfileDetailResponseBody from a JSON string
lockfile_get_lockfile_detail_response_body_instance = LockfileGetLockfileDetailResponseBody.from_json(json)
# print the JSON string representation of the object
print LockfileGetLockfileDetailResponseBody.to_json()

# convert the object into a dict
lockfile_get_lockfile_detail_response_body_dict = lockfile_get_lockfile_detail_response_body_instance.to_dict()
# create an instance of LockfileGetLockfileDetailResponseBody from a dict
lockfile_get_lockfile_detail_response_body_form_dict = lockfile_get_lockfile_detail_response_body.from_dict(lockfile_get_lockfile_detail_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


