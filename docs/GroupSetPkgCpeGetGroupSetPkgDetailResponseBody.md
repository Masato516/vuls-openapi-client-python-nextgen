# GroupSetPkgCpeGetGroupSetPkgDetailResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_procs** | [**List[AffectedProcResponseBody]**](AffectedProcResponseBody.md) | AffectedProcess list of package | [optional] 
**created_at** | **datetime** | crated time of package or cpe | 
**group** | [**GroupResponseBody**](GroupResponseBody.md) |  | [optional] 
**id** | **int** | ID of package | [optional] 
**name** | **str** | Name of package or cpe | 
**need_restart_procs** | [**List[NeedRestartProcResponseBody]**](NeedRestartProcResponseBody.md) | NeedRestartProcess list of package | [optional] 
**new_release** | **str** | New Release of package | [optional] 
**new_version** | **str** | New Version of package | [optional] 
**package_statuses** | **Dict[str, str]** | package status of package | [optional] 
**release** | **str** | Release of package | 
**repository** | **str** | Repository of package | [optional] 
**server** | [**ServerChildResponseBody**](ServerChildResponseBody.md) |  | [optional] 
**tasks** | [**List[ChildTaskResponseBody]**](ChildTaskResponseBody.md) | updated time of server | [optional] 
**updated_at** | **datetime** | updated time of package or cpe | 
**version** | **str** | Version of package or cpe | 

## Example

```python
from openapiclient.models.group_set_pkg_cpe_get_group_set_pkg_detail_response_body import GroupSetPkgCpeGetGroupSetPkgDetailResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSetPkgCpeGetGroupSetPkgDetailResponseBody from a JSON string
group_set_pkg_cpe_get_group_set_pkg_detail_response_body_instance = GroupSetPkgCpeGetGroupSetPkgDetailResponseBody.from_json(json)
# print the JSON string representation of the object
print GroupSetPkgCpeGetGroupSetPkgDetailResponseBody.to_json()

# convert the object into a dict
group_set_pkg_cpe_get_group_set_pkg_detail_response_body_dict = group_set_pkg_cpe_get_group_set_pkg_detail_response_body_instance.to_dict()
# create an instance of GroupSetPkgCpeGetGroupSetPkgDetailResponseBody from a dict
group_set_pkg_cpe_get_group_set_pkg_detail_response_body_form_dict = group_set_pkg_cpe_get_group_set_pkg_detail_response_body.from_dict(group_set_pkg_cpe_get_group_set_pkg_detail_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


