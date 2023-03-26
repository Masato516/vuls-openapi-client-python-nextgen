# EnvMetricV3ResponseBody

EnvMetricV3 describes a envMetricV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | created time | 
**cve_id** | **str** | CveID of envMetricV3 | 
**ma** | **str** | MA of envMetricV3 | 
**mac** | **str** | MAC of envMetricV3 | 
**mav** | **str** | MAV of envMetricV3 | 
**mc** | **str** | MC of envMetricV3 | 
**mpr** | **str** | MPR of envMetricV3 | 
**ms** | **str** | MS of envMetricV3 | 
**mui** | **str** | MUI of envMetricV3 | 
**role_id** | **int** | ServerRoleID of envMetricV3 | 
**role_name** | **str** | ServerRoleName of envMetricV3 | 
**updated_at** | **datetime** | updated time | 

## Example

```python
from openapiclient.models.env_metric_v3_response_body import EnvMetricV3ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnvMetricV3ResponseBody from a JSON string
env_metric_v3_response_body_instance = EnvMetricV3ResponseBody.from_json(json)
# print the JSON string representation of the object
print EnvMetricV3ResponseBody.to_json()

# convert the object into a dict
env_metric_v3_response_body_dict = env_metric_v3_response_body_instance.to_dict()
# create an instance of EnvMetricV3ResponseBody from a dict
env_metric_v3_response_body_form_dict = env_metric_v3_response_body.from_dict(env_metric_v3_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


