# NeedRestartProcResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**init_system** | **str** | InitSystem of NeedRestartProc | 
**path** | **str** | Path of NeedRestartProc | 
**pid** | **str** | PID | 
**service_name** | **str** | ServiceName of NeedRestartProc | 

## Example

```python
from openapiclient.models.need_restart_proc_response_body import NeedRestartProcResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of NeedRestartProcResponseBody from a JSON string
need_restart_proc_response_body_instance = NeedRestartProcResponseBody.from_json(json)
# print the JSON string representation of the object
print NeedRestartProcResponseBody.to_json()

# convert the object into a dict
need_restart_proc_response_body_dict = need_restart_proc_response_body_instance.to_dict()
# create an instance of NeedRestartProcResponseBody from a dict
need_restart_proc_response_body_form_dict = need_restart_proc_response_body.from_dict(need_restart_proc_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


