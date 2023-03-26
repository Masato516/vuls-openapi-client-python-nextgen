# PagingResponseBody

Paging describes a paging object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Limit | 
**offset** | **int** | Offset | 
**page** | **int** | Page | 
**total_count** | **int** | TotalCount | 
**total_page** | **int** | Total Page Size | 

## Example

```python
from openapiclient.models.paging_response_body import PagingResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of PagingResponseBody from a JSON string
paging_response_body_instance = PagingResponseBody.from_json(json)
# print the JSON string representation of the object
print PagingResponseBody.to_json()

# convert the object into a dict
paging_response_body_dict = paging_response_body_instance.to_dict()
# create an instance of PagingResponseBody from a dict
paging_response_body_form_dict = paging_response_body.from_dict(paging_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


