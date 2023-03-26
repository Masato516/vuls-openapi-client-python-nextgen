# openapiclient.GroupSetTaskApi

All URIs are relative to *https://rest.2119e7c929.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_set_task_get_group_set_task_detail**](GroupSetTaskApi.md#group_set_task_get_group_set_task_detail) | **GET** /v1/groupSet/task/{taskID} | getGroupSetTaskDetail groupSetTask
[**group_set_task_get_group_set_task_list**](GroupSetTaskApi.md#group_set_task_get_group_set_task_list) | **GET** /v1/groupSet/tasks | getGroupSetTaskList groupSetTask


# **group_set_task_get_group_set_task_detail**
> GroupSetTaskGetGroupSetTaskDetailResponseBody group_set_task_get_group_set_task_detail(task_id)

getGroupSetTaskDetail groupSetTask

group set task detail

### Example

* Api Key Authentication (api_key_header_Authorization):
```python
from __future__ import print_function
import time
import os
import openapiclient
from openapiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest.2119e7c929.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapiclient.Configuration(
    host = "https://rest.2119e7c929.vuls.biz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_header_Authorization
configuration.api_key['api_key_header_Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header_Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapiclient.GroupSetTaskApi(api_client)
    task_id = 56 # int | Task ID

    try:
        # getGroupSetTaskDetail groupSetTask
        api_response = api_instance.group_set_task_get_group_set_task_detail(task_id)
        print("The response of GroupSetTaskApi->group_set_task_get_group_set_task_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupSetTaskApi->group_set_task_get_group_set_task_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task ID | 

### Return type

[**GroupSetTaskGetGroupSetTaskDetailResponseBody**](GroupSetTaskGetGroupSetTaskDetailResponseBody.md)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/gob

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_set_task_get_group_set_task_list**
> GroupSetTaskGetGroupSetTaskListResponseBody group_set_task_get_group_set_task_list(page=page, limit=limit, offset=offset, filter_status=filter_status, filter_priority=filter_priority, filter_ignore=filter_ignore, filter_main_user_ids=filter_main_user_ids, filter_sub_user_ids=filter_sub_user_ids, filter_cve_id=filter_cve_id, filter_server_id=filter_server_id, filter_role_id=filter_role_id, filter_pkg_id=filter_pkg_id, filter_cpe_id=filter_cpe_id)

getGroupSetTaskList groupSetTask

group set task list

### Example

* Api Key Authentication (api_key_header_Authorization):
```python
from __future__ import print_function
import time
import os
import openapiclient
from openapiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest.2119e7c929.vuls.biz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapiclient.Configuration(
    host = "https://rest.2119e7c929.vuls.biz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_header_Authorization
configuration.api_key['api_key_header_Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header_Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapiclient.GroupSetTaskApi(api_client)
    page = 1 # int | Page Number (optional) (default to 1)
    limit = 20 # int | Limit (optional) (default to 20)
    offset = 0 # int | Offset (optional) (default to 0)
    filter_status = ["new","investigating","ongoing"] # List[str] | Status filter (optional) (default to ["new","investigating","ongoing"])
    filter_priority = ['filter_priority_example'] # List[str] | Priority filter (optional)
    filter_ignore = True # bool | Ignore filter(trueの場合は、非表示のものを取得しない。falseの場合は全件取得) (optional)
    filter_main_user_ids = [56] # List[int] | MainUserIDs filter (optional)
    filter_sub_user_ids = [56] # List[int] | SubUserIDs filter (optional)
    filter_cve_id = 'filter_cve_id_example' # str | CveID filter (optional)
    filter_server_id = 56 # int | ServerID filter (optional)
    filter_role_id = 56 # int | ServerRoleID filter (optional)
    filter_pkg_id = 56 # int | PackageID filter (optional)
    filter_cpe_id = 56 # int | CpeID filter (optional)

    try:
        # getGroupSetTaskList groupSetTask
        api_response = api_instance.group_set_task_get_group_set_task_list(page=page, limit=limit, offset=offset, filter_status=filter_status, filter_priority=filter_priority, filter_ignore=filter_ignore, filter_main_user_ids=filter_main_user_ids, filter_sub_user_ids=filter_sub_user_ids, filter_cve_id=filter_cve_id, filter_server_id=filter_server_id, filter_role_id=filter_role_id, filter_pkg_id=filter_pkg_id, filter_cpe_id=filter_cpe_id)
        print("The response of GroupSetTaskApi->group_set_task_get_group_set_task_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupSetTaskApi->group_set_task_get_group_set_task_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] [default to 1]
 **limit** | **int**| Limit | [optional] [default to 20]
 **offset** | **int**| Offset | [optional] [default to 0]
 **filter_status** | [**List[str]**](str.md)| Status filter | [optional] [default to [&quot;new&quot;,&quot;investigating&quot;,&quot;ongoing&quot;]]
 **filter_priority** | [**List[str]**](str.md)| Priority filter | [optional] 
 **filter_ignore** | **bool**| Ignore filter(trueの場合は、非表示のものを取得しない。falseの場合は全件取得) | [optional] 
 **filter_main_user_ids** | [**List[int]**](int.md)| MainUserIDs filter | [optional] 
 **filter_sub_user_ids** | [**List[int]**](int.md)| SubUserIDs filter | [optional] 
 **filter_cve_id** | **str**| CveID filter | [optional] 
 **filter_server_id** | **int**| ServerID filter | [optional] 
 **filter_role_id** | **int**| ServerRoleID filter | [optional] 
 **filter_pkg_id** | **int**| PackageID filter | [optional] 
 **filter_cpe_id** | **int**| CpeID filter | [optional] 

### Return type

[**GroupSetTaskGetGroupSetTaskListResponseBody**](GroupSetTaskGetGroupSetTaskListResponseBody.md)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/gob

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

