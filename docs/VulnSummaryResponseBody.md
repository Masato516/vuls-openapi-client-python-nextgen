# VulnSummaryResponseBody

summary of vulnerability information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_level** | **str** | 警戒レベル | [optional] 
**cwe** | [**List[CweResponseBody]**](CweResponseBody.md) | cwe | 
**has_alert** | **bool** | 警戒情報があるかどうか | 
**is_owasp_top_ten2017** | **bool** | 2017 owasp top tenに記載されているかどうか | 
**title** | **str** | title | 

## Example

```python
from openapiclient.models.vuln_summary_response_body import VulnSummaryResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of VulnSummaryResponseBody from a JSON string
vuln_summary_response_body_instance = VulnSummaryResponseBody.from_json(json)
# print the JSON string representation of the object
print VulnSummaryResponseBody.to_json()

# convert the object into a dict
vuln_summary_response_body_dict = vuln_summary_response_body_instance.to_dict()
# create an instance of VulnSummaryResponseBody from a dict
vuln_summary_response_body_form_dict = vuln_summary_response_body.from_dict(vuln_summary_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


