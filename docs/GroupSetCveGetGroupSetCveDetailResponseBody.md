# GroupSetCveGetGroupSetCveDetailResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | created time | 
**cve_id** | **str** | Cve ID string of cve | 
**cvss** | [**CvssResponseBody**](CvssResponseBody.md) |  | 
**cwes** | [**List[CweResponseBody]**](CweResponseBody.md) | cwes of cve | 
**group** | [**GroupResponseBody**](GroupResponseBody.md) |  | [optional] 
**updated_at** | **datetime** | updated time | 

## Example

```python
from openapiclient.models.group_set_cve_get_group_set_cve_detail_response_body import GroupSetCveGetGroupSetCveDetailResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSetCveGetGroupSetCveDetailResponseBody from a JSON string
group_set_cve_get_group_set_cve_detail_response_body_instance = GroupSetCveGetGroupSetCveDetailResponseBody.from_json(json)
# print the JSON string representation of the object
print GroupSetCveGetGroupSetCveDetailResponseBody.to_json()

# convert the object into a dict
group_set_cve_get_group_set_cve_detail_response_body_dict = group_set_cve_get_group_set_cve_detail_response_body_instance.to_dict()
# create an instance of GroupSetCveGetGroupSetCveDetailResponseBody from a dict
group_set_cve_get_group_set_cve_detail_response_body_form_dict = group_set_cve_get_group_set_cve_detail_response_body.from_dict(group_set_cve_get_group_set_cve_detail_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


