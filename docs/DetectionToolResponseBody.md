# DetectionToolResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Detection Tool Name | 
**patch_applied_at** | **datetime** | PatchAppliedAt | [optional] 

## Example

```python
from openapiclient.models.detection_tool_response_body import DetectionToolResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of DetectionToolResponseBody from a JSON string
detection_tool_response_body_instance = DetectionToolResponseBody.from_json(json)
# print the JSON string representation of the object
print DetectionToolResponseBody.to_json()

# convert the object into a dict
detection_tool_response_body_dict = detection_tool_response_body_instance.to_dict()
# create an instance of DetectionToolResponseBody from a dict
detection_tool_response_body_form_dict = detection_tool_response_body.from_dict(detection_tool_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


