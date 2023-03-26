# SecMetricResponseBody

SecMetric describes a secMetric

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ar** | **str** | AR of secMetric | 
**cr** | **str** | CR of secMetric | 
**created_at** | **datetime** | created time | 
**ir** | **str** | IR of secMetric | 
**role_id** | **int** | ServerRoleID of secMetric | 
**role_name** | **str** | ServerRoleName of secMetric | 
**updated_at** | **datetime** | updated time | 

## Example

```python
from openapiclient.models.sec_metric_response_body import SecMetricResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SecMetricResponseBody from a JSON string
sec_metric_response_body_instance = SecMetricResponseBody.from_json(json)
# print the JSON string representation of the object
print SecMetricResponseBody.to_json()

# convert the object into a dict
sec_metric_response_body_dict = sec_metric_response_body_instance.to_dict()
# create an instance of SecMetricResponseBody from a dict
sec_metric_response_body_form_dict = sec_metric_response_body.from_dict(sec_metric_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


