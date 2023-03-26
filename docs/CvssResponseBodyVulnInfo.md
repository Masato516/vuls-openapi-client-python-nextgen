# CvssResponseBodyVulnInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_dict** | **object** |  | [optional] 
**ctis** | **List[str]** |  | [optional] 
**cve_contents** | **object** |  | [optional] 
**cve_id** | **str** |  | [optional] 
**exploits** | **List[object]** |  | [optional] 
**mitigations** | **List[object]** |  | [optional] 

## Example

```python
from openapiclient.models.cvss_response_body_vuln_info import CvssResponseBodyVulnInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CvssResponseBodyVulnInfo from a JSON string
cvss_response_body_vuln_info_instance = CvssResponseBodyVulnInfo.from_json(json)
# print the JSON string representation of the object
print CvssResponseBodyVulnInfo.to_json()

# convert the object into a dict
cvss_response_body_vuln_info_dict = cvss_response_body_vuln_info_instance.to_dict()
# create an instance of CvssResponseBodyVulnInfo from a dict
cvss_response_body_vuln_info_form_dict = cvss_response_body_vuln_info.from_dict(cvss_response_body_vuln_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


