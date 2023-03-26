# GroupSetCveGetGroupSetCveListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cves** | [**List[GroupSetCveListResponseBody]**](GroupSetCveListResponseBody.md) | Group Set Cves list | [optional] 
**paging** | [**PagingResponseBody**](PagingResponseBody.md) |  | [optional] 

## Example

```python
from openapiclient.models.group_set_cve_get_group_set_cve_list_response_body import GroupSetCveGetGroupSetCveListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSetCveGetGroupSetCveListResponseBody from a JSON string
group_set_cve_get_group_set_cve_list_response_body_instance = GroupSetCveGetGroupSetCveListResponseBody.from_json(json)
# print the JSON string representation of the object
print GroupSetCveGetGroupSetCveListResponseBody.to_json()

# convert the object into a dict
group_set_cve_get_group_set_cve_list_response_body_dict = group_set_cve_get_group_set_cve_list_response_body_instance.to_dict()
# create an instance of GroupSetCveGetGroupSetCveListResponseBody from a dict
group_set_cve_get_group_set_cve_list_response_body_form_dict = group_set_cve_get_group_set_cve_list_response_body.from_dict(group_set_cve_get_group_set_cve_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


