# EnvMetricV2ResponseBody

EnvMetricV2 describes a envMetricV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp** | **str** | CDP of envMetricV2 | 
**created_at** | **datetime** | created time | 
**cve_id** | **str** | CveID of envMetricV2 | 
**role_id** | **int** | ServerRoleID of envMetricV2 | 
**role_name** | **str** | ServerRoleName of envMetricV2 | 
**td** | **str** | TD of envMetricV2 | 
**updated_at** | **datetime** | updated time | 

## Example

```python
from openapiclient.models.env_metric_v2_response_body import EnvMetricV2ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnvMetricV2ResponseBody from a JSON string
env_metric_v2_response_body_instance = EnvMetricV2ResponseBody.from_json(json)
# print the JSON string representation of the object
print EnvMetricV2ResponseBody.to_json()

# convert the object into a dict
env_metric_v2_response_body_dict = env_metric_v2_response_body_instance.to_dict()
# create an instance of EnvMetricV2ResponseBody from a dict
env_metric_v2_response_body_form_dict = env_metric_v2_response_body.from_dict(env_metric_v2_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


