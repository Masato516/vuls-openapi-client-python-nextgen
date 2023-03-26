# PkgCpeGetCpeDetailResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe_uri** | **str** | Cpe URI of cpe | [optional] 
**created_at** | **datetime** | crated time of package or cpe | 
**group** | [**GroupResponseBody**](GroupResponseBody.md) |  | [optional] 
**id** | **int** | ID of package or cpe | 
**name** | **str** | Name of package or cpe | 
**server** | [**ServerChildResponseBody**](ServerChildResponseBody.md) |  | 
**tasks** | [**List[ChildTaskResponseBody]**](ChildTaskResponseBody.md) | updated time of server | [optional] 
**updated_at** | **datetime** | updated time of package or cpe | 
**version** | **str** | Version of package or cpe | 

## Example

```python
from openapiclient.models.pkg_cpe_get_cpe_detail_response_body import PkgCpeGetCpeDetailResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of PkgCpeGetCpeDetailResponseBody from a JSON string
pkg_cpe_get_cpe_detail_response_body_instance = PkgCpeGetCpeDetailResponseBody.from_json(json)
# print the JSON string representation of the object
print PkgCpeGetCpeDetailResponseBody.to_json()

# convert the object into a dict
pkg_cpe_get_cpe_detail_response_body_dict = pkg_cpe_get_cpe_detail_response_body_instance.to_dict()
# create an instance of PkgCpeGetCpeDetailResponseBody from a dict
pkg_cpe_get_cpe_detail_response_body_form_dict = pkg_cpe_get_cpe_detail_response_body.from_dict(pkg_cpe_get_cpe_detail_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


