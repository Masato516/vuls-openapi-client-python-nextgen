# CweResponseBody

Cwe describes a cwe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cwe_id** | **str** | cweID of cwe | 
**english** | **str** | english summary of cwe | 
**japanese** | **str** | japanese summary of cwe | 
**owasp_top_ten2017** | **str** | owaspTopTen2017 of cwe  | [optional] 

## Example

```python
from openapiclient.models.cwe_response_body import CweResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CweResponseBody from a JSON string
cwe_response_body_instance = CweResponseBody.from_json(json)
# print the JSON string representation of the object
print CweResponseBody.to_json()

# convert the object into a dict
cwe_response_body_dict = cwe_response_body_instance.to_dict()
# create an instance of CweResponseBody from a dict
cwe_response_body_form_dict = cwe_response_body.from_dict(cwe_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


