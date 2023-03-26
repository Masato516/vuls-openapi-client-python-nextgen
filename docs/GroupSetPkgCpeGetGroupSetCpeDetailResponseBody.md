# GroupSetPkgCpeGetGroupSetCpeDetailResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe_uri** | **str** | Cpe URI of cpe | [optional] 
**created_at** | **datetime** | crated time of package or cpe | 
**group** | [**GroupResponseBody**](GroupResponseBody.md) |  | [optional] 
**id** | **int** | ID of package or cpe | 
**name** | **str** | Name of package or cpe | 
**server** | [**ServerChildResponseBody**](ServerChildResponseBody.md) |  | 
**tasks** | [**List[ChildTaskResponseBody]**](ChildTaskResponseBody.md) | updated time of server | [optional] 
**updated_at** | **datetime** | updated time of package or cpe | 
**version** | **str** | Version of package or cpe | 

## Example

```python
from openapiclient.models.group_set_pkg_cpe_get_group_set_cpe_detail_response_body import GroupSetPkgCpeGetGroupSetCpeDetailResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSetPkgCpeGetGroupSetCpeDetailResponseBody from a JSON string
group_set_pkg_cpe_get_group_set_cpe_detail_response_body_instance = GroupSetPkgCpeGetGroupSetCpeDetailResponseBody.from_json(json)
# print the JSON string representation of the object
print GroupSetPkgCpeGetGroupSetCpeDetailResponseBody.to_json()

# convert the object into a dict
group_set_pkg_cpe_get_group_set_cpe_detail_response_body_dict = group_set_pkg_cpe_get_group_set_cpe_detail_response_body_instance.to_dict()
# create an instance of GroupSetPkgCpeGetGroupSetCpeDetailResponseBody from a dict
group_set_pkg_cpe_get_group_set_cpe_detail_response_body_form_dict = group_set_pkg_cpe_get_group_set_cpe_detail_response_body.from_dict(group_set_pkg_cpe_get_group_set_cpe_detail_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


