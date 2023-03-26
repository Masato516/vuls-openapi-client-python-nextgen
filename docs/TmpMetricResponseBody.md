# TmpMetricResponseBody

TmpMetric describes a tmpMetric

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | created time | 
**e** | **str** | E of tmpMetric | 
**rc** | **str** | RC of tmpMetric | 
**rl** | **str** | RL of tmpMetric | 
**updated_at** | **datetime** | updated time | 

## Example

```python
from openapiclient.models.tmp_metric_response_body import TmpMetricResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TmpMetricResponseBody from a JSON string
tmp_metric_response_body_instance = TmpMetricResponseBody.from_json(json)
# print the JSON string representation of the object
print TmpMetricResponseBody.to_json()

# convert the object into a dict
tmp_metric_response_body_dict = tmp_metric_response_body_instance.to_dict()
# create an instance of TmpMetricResponseBody from a dict
tmp_metric_response_body_form_dict = tmp_metric_response_body.from_dict(tmp_metric_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


