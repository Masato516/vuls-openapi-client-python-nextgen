# LockfileAddLockfileRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_content** | **str** | fileContent of the lockfile (or Base64 string of fileContent) | 
**path** | **str** | Path of lockfile | 
**server_id** | **int** | ServerID | 

## Example

```python
from openapiclient.models.lockfile_add_lockfile_request_body import LockfileAddLockfileRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of LockfileAddLockfileRequestBody from a JSON string
lockfile_add_lockfile_request_body_instance = LockfileAddLockfileRequestBody.from_json(json)
# print the JSON string representation of the object
print LockfileAddLockfileRequestBody.to_json()

# convert the object into a dict
lockfile_add_lockfile_request_body_dict = lockfile_add_lockfile_request_body_instance.to_dict()
# create an instance of LockfileAddLockfileRequestBody from a dict
lockfile_add_lockfile_request_body_form_dict = lockfile_add_lockfile_request_body.from_dict(lockfile_add_lockfile_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


