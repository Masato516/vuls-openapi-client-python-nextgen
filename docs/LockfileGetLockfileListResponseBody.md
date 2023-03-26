# LockfileGetLockfileListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lockfiles** | [**List[LockfileListResponseBody]**](LockfileListResponseBody.md) | Lockfiles list | [optional] 
**paging** | [**PagingResponseBody**](PagingResponseBody.md) |  | [optional] 

## Example

```python
from openapiclient.models.lockfile_get_lockfile_list_response_body import LockfileGetLockfileListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of LockfileGetLockfileListResponseBody from a JSON string
lockfile_get_lockfile_list_response_body_instance = LockfileGetLockfileListResponseBody.from_json(json)
# print the JSON string representation of the object
print LockfileGetLockfileListResponseBody.to_json()

# convert the object into a dict
lockfile_get_lockfile_list_response_body_dict = lockfile_get_lockfile_list_response_body_instance.to_dict()
# create an instance of LockfileGetLockfileListResponseBody from a dict
lockfile_get_lockfile_list_response_body_form_dict = lockfile_get_lockfile_list_response_body.from_dict(lockfile_get_lockfile_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


