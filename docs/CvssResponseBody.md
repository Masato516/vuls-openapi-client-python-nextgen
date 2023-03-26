# CvssResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_id** | **str** |  | [optional] 
**max_cvss_v2** | [**CvssResponseBodyMaxCvssV2**](CvssResponseBodyMaxCvssV2.md) |  | [optional] 
**max_cvss_v3** | [**CvssResponseBodyMaxCvssV2**](CvssResponseBodyMaxCvssV2.md) |  | [optional] 
**vuln_info** | [**CvssResponseBodyVulnInfo**](CvssResponseBodyVulnInfo.md) |  | [optional] 

## Example

```python
from openapiclient.models.cvss_response_body import CvssResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CvssResponseBody from a JSON string
cvss_response_body_instance = CvssResponseBody.from_json(json)
# print the JSON string representation of the object
print CvssResponseBody.to_json()

# convert the object into a dict
cvss_response_body_dict = cvss_response_body_instance.to_dict()
# create an instance of CvssResponseBody from a dict
cvss_response_body_form_dict = cvss_response_body.from_dict(cvss_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


