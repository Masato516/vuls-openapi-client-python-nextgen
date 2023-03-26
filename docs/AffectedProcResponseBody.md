# AffectedProcResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | AffectedProc Name | 
**pid** | **str** | PID | 

## Example

```python
from openapiclient.models.affected_proc_response_body import AffectedProcResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of AffectedProcResponseBody from a JSON string
affected_proc_response_body_instance = AffectedProcResponseBody.from_json(json)
# print the JSON string representation of the object
print AffectedProcResponseBody.to_json()

# convert the object into a dict
affected_proc_response_body_dict = affected_proc_response_body_instance.to_dict()
# create an instance of AffectedProcResponseBody from a dict
affected_proc_response_body_form_dict = affected_proc_response_body.from_dict(affected_proc_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


