# CveGetCveDetailResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | created time | 
**cve_id** | **str** | Cve ID string of cve | 
**cvss** | [**CvssResponseBody**](CvssResponseBody.md) |  | 
**cwes** | [**List[CweResponseBody]**](CweResponseBody.md) | cwes of cve | 
**env_metric_v2s** | [**List[EnvMetricV2ResponseBody]**](EnvMetricV2ResponseBody.md) | envMetricV2 of cve | 
**env_metric_v3s** | [**List[EnvMetricV3ResponseBody]**](EnvMetricV3ResponseBody.md) | envMetricV3 of cve | 
**exploit_level** | **str** | ExploitLevel of cve | [optional] 
**has_exploit** | **bool** | exploit exist | [optional] 
**has_mitigation** | **bool** | mitigation exist | [optional] 
**references** | **Dict[str, str]** | references of cve | 
**sec_metrics** | [**List[SecMetricResponseBody]**](SecMetricResponseBody.md) | secMetric of cve | 
**tmp_metric_v2** | [**TmpMetricResponseBody**](TmpMetricResponseBody.md) |  | 
**tmp_metric_v3** | [**TmpMetricResponseBody**](TmpMetricResponseBody.md) |  | 
**updated_at** | **datetime** | updated time | 

## Example

```python
from openapiclient.models.cve_get_cve_detail_response_body import CveGetCveDetailResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CveGetCveDetailResponseBody from a JSON string
cve_get_cve_detail_response_body_instance = CveGetCveDetailResponseBody.from_json(json)
# print the JSON string representation of the object
print CveGetCveDetailResponseBody.to_json()

# convert the object into a dict
cve_get_cve_detail_response_body_dict = cve_get_cve_detail_response_body_instance.to_dict()
# create an instance of CveGetCveDetailResponseBody from a dict
cve_get_cve_detail_response_body_form_dict = cve_get_cve_detail_response_body.from_dict(cve_get_cve_detail_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


