# CveGetCveListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cves** | [**List[CveListResponseBody]**](CveListResponseBody.md) | Cves list | [optional] 
**paging** | [**PagingResponseBody**](PagingResponseBody.md) |  | [optional] 

## Example

```python
from openapiclient.models.cve_get_cve_list_response_body import CveGetCveListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CveGetCveListResponseBody from a JSON string
cve_get_cve_list_response_body_instance = CveGetCveListResponseBody.from_json(json)
# print the JSON string representation of the object
print CveGetCveListResponseBody.to_json()

# convert the object into a dict
cve_get_cve_list_response_body_dict = cve_get_cve_list_response_body_instance.to_dict()
# create an instance of CveGetCveListResponseBody from a dict
cve_get_cve_list_response_body_form_dict = cve_get_cve_list_response_body.from_dict(cve_get_cve_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


