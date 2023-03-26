# GroupSetPkgCpeListResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | ApplicationName of library package | [optional] 
**cpe_fs** | **str** | Cpe FS of cpe | [optional] 
**cpe_id** | **int** | CpeID of cpe | [optional] 
**cpe_uri** | **str** | Cpe URI of cpe | [optional] 
**created_at** | **datetime** | crated time of package or cpe | 
**github_pkg_id** | **int** | githubPKGID of github pkg | [optional] 
**group** | [**GroupResponseBody**](GroupResponseBody.md) |  | 
**library_path** | **str** | LibraryPath of library package | [optional] 
**library_pkg_id** | **int** | libraryPKGID of library pkg | [optional] 
**name** | **str** | Name of package or cpe | 
**need_restart_procs** | [**List[NeedRestartProcResponseBody]**](NeedRestartProcResponseBody.md) | NeedRestartProcess list of package | [optional] 
**new_release** | **str** | New Release of package | [optional] 
**new_version** | **str** | New Version of package | [optional] 
**not_fixed_yet** | **bool** | Flag of Not fixed yet of package | [optional] 
**oss_license** | **str** | ossLicense of library package | [optional] 
**pkg_id** | **int** | Package ID of package | [optional] 
**release** | **str** | Release of package | [optional] 
**repository** | **str** | Repository of package | [optional] 
**server_id** | **int** | ServerID of package or cpe | 
**server_name** | **str** | ServerName of package or cpe | 
**server_uuid** | **str** | ServerUUID of package or cpe | 
**updated_at** | **datetime** | updated time of package or cpe | 
**version** | **str** | Version of package or cpe | 
**wordpress_package_status** | **str** | WordpressPackageStatus of wordpress package | [optional] 
**wordpress_pkg_id** | **int** | wordpressPKGID of wordpress pkg | [optional] 

## Example

```python
from openapiclient.models.group_set_pkg_cpe_list_response_body import GroupSetPkgCpeListResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSetPkgCpeListResponseBody from a JSON string
group_set_pkg_cpe_list_response_body_instance = GroupSetPkgCpeListResponseBody.from_json(json)
# print the JSON string representation of the object
print GroupSetPkgCpeListResponseBody.to_json()

# convert the object into a dict
group_set_pkg_cpe_list_response_body_dict = group_set_pkg_cpe_list_response_body_instance.to_dict()
# create an instance of GroupSetPkgCpeListResponseBody from a dict
group_set_pkg_cpe_list_response_body_form_dict = group_set_pkg_cpe_list_response_body.from_dict(group_set_pkg_cpe_list_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


