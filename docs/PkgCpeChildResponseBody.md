# PkgCpeChildResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_procs** | [**List[AffectedProcResponseBody]**](AffectedProcResponseBody.md) | AffectedProcess list of package | [optional] 
**cpe_id** | **int** | CpeID of cpe | [optional] 
**cpe_uri** | **str** | Cpe URI of cpe | [optional] 
**created_at** | **datetime** | crated time of package or cpe | 
**name** | **str** | Name of package or cpe | 
**new_release** | **str** | New Release of package | [optional] 
**new_version** | **str** | New Version of package | [optional] 
**pkg_id** | **int** | Package ID of package | [optional] 
**release** | **str** | Release of package | [optional] 
**repository** | **str** | Repository of package | [optional] 
**server_id** | **int** | ServerID of package or cpe | 
**updated_at** | **datetime** | updated time of package or cpe | 
**version** | **str** | Version of package or cpe | 

## Example

```python
from openapiclient.models.pkg_cpe_child_response_body import PkgCpeChildResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of PkgCpeChildResponseBody from a JSON string
pkg_cpe_child_response_body_instance = PkgCpeChildResponseBody.from_json(json)
# print the JSON string representation of the object
print PkgCpeChildResponseBody.to_json()

# convert the object into a dict
pkg_cpe_child_response_body_dict = pkg_cpe_child_response_body_instance.to_dict()
# create an instance of PkgCpeChildResponseBody from a dict
pkg_cpe_child_response_body_form_dict = pkg_cpe_child_response_body.from_dict(pkg_cpe_child_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


