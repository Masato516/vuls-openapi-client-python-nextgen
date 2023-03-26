# RoleGetRoleDetailResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_task_count** | **int** | AllTaskCount of server role | [optional] 
**created_at** | **datetime** | created time of server role | 
**env_metric_v2s** | [**List[EnvMetricV2ResponseBody]**](EnvMetricV2ResponseBody.md) | envMetricV2s of server role | [optional] 
**env_metric_v3s** | [**List[EnvMetricV3ResponseBody]**](EnvMetricV3ResponseBody.md) | envMetricV3s of server role | [optional] 
**id** | **int** | ID of server role | 
**is_default** | **bool** | isDefault of server role | [optional] 
**name** | **str** | Name of server role | 
**new_task_count** | **int** | NewTaskCount of server role | [optional] 
**sec_metric** | [**SecMetricResponseBody**](SecMetricResponseBody.md) |  | [optional] 
**servers** | [**List[ServerChildResponseBody]**](ServerChildResponseBody.md) | Servers of server role | [optional] 
**updated_at** | **datetime** | updated time of server role | 

## Example

```python
from openapiclient.models.role_get_role_detail_response_body import RoleGetRoleDetailResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of RoleGetRoleDetailResponseBody from a JSON string
role_get_role_detail_response_body_instance = RoleGetRoleDetailResponseBody.from_json(json)
# print the JSON string representation of the object
print RoleGetRoleDetailResponseBody.to_json()

# convert the object into a dict
role_get_role_detail_response_body_dict = role_get_role_detail_response_body_instance.to_dict()
# create an instance of RoleGetRoleDetailResponseBody from a dict
role_get_role_detail_response_body_form_dict = role_get_role_detail_response_body.from_dict(role_get_role_detail_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


