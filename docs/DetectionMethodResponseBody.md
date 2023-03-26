# DetectionMethodResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Detection Method Name | 
**reliability_score** | **int** | ReliabilityScore | 

## Example

```python
from openapiclient.models.detection_method_response_body import DetectionMethodResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of DetectionMethodResponseBody from a JSON string
detection_method_response_body_instance = DetectionMethodResponseBody.from_json(json)
# print the JSON string representation of the object
print DetectionMethodResponseBody.to_json()

# convert the object into a dict
detection_method_response_body_dict = detection_method_response_body_instance.to_dict()
# create an instance of DetectionMethodResponseBody from a dict
detection_method_response_body_form_dict = detection_method_response_body.from_dict(detection_method_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


