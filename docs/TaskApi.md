# openapiclient.TaskApi

All URIs are relative to *https://rest.2119e7c929.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_add_task_comment**](TaskApi.md#task_add_task_comment) | **POST** /v1/task/{taskID}/comment | addTaskComment task
[**task_get_task_detail**](TaskApi.md#task_get_task_detail) | **GET** /v1/task/{taskID} | getTaskDetail task
[**task_get_task_list**](TaskApi.md#task_get_task_list) | **GET** /v1/tasks | getTaskList task
[**task_update_task**](TaskApi.md#task_update_task) | **PUT** /v1/task/{taskID} | updateTask task
[**task_update_task_ignore**](TaskApi.md#task_update_task_ignore) | **PUT** /v1/task/{taskID}/ignore | updateTaskIgnore task


# **task_add_task_comment**
> TaskAddTaskCommentResponseBody task_add_task_comment(task_id, add_task_comment_request_body)

addTaskComment task

add task comment

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
    api_instance = openapiclient.TaskApi(api_client)
    task_id = 56 # int | Task ID
    add_task_comment_request_body = openapiclient.TaskAddTaskCommentRequestBody() # TaskAddTaskCommentRequestBody | 

    try:
        # addTaskComment task
        api_response = api_instance.task_add_task_comment(task_id, add_task_comment_request_body)
        print("The response of TaskApi->task_add_task_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->task_add_task_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task ID | 
 **add_task_comment_request_body** | [**TaskAddTaskCommentRequestBody**](TaskAddTaskCommentRequestBody.md)|  | 

### Return type

[**TaskAddTaskCommentResponseBody**](TaskAddTaskCommentResponseBody.md)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/gob
 - **Accept**: application/json, application/xml, application/gob

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_get_task_detail**
> TaskGetTaskDetailResponseBody task_get_task_detail(task_id)

getTaskDetail task

task detail

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
    api_instance = openapiclient.TaskApi(api_client)
    task_id = 56 # int | Task ID

    try:
        # getTaskDetail task
        api_response = api_instance.task_get_task_detail(task_id)
        print("The response of TaskApi->task_get_task_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->task_get_task_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task ID | 

### Return type

[**TaskGetTaskDetailResponseBody**](TaskGetTaskDetailResponseBody.md)

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

# **task_get_task_list**
> TaskGetTaskListResponseBody task_get_task_list(page=page, limit=limit, offset=offset, filter_status=filter_status, filter_priority=filter_priority, filter_ignore=filter_ignore, filter_main_user_ids=filter_main_user_ids, filter_sub_user_ids=filter_sub_user_ids, filter_cve_id=filter_cve_id, filter_server_id=filter_server_id, filter_role_id=filter_role_id, filter_pkg_id=filter_pkg_id, filter_cpe_id=filter_cpe_id)

getTaskList task

task list

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
    api_instance = openapiclient.TaskApi(api_client)
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
        # getTaskList task
        api_response = api_instance.task_get_task_list(page=page, limit=limit, offset=offset, filter_status=filter_status, filter_priority=filter_priority, filter_ignore=filter_ignore, filter_main_user_ids=filter_main_user_ids, filter_sub_user_ids=filter_sub_user_ids, filter_cve_id=filter_cve_id, filter_server_id=filter_server_id, filter_role_id=filter_role_id, filter_pkg_id=filter_pkg_id, filter_cpe_id=filter_cpe_id)
        print("The response of TaskApi->task_get_task_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->task_get_task_list: %s\n" % e)
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

[**TaskGetTaskListResponseBody**](TaskGetTaskListResponseBody.md)

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

# **task_update_task**
> TaskUpdateTaskResponseBody task_update_task(task_id, update_task_request_body)

updateTask task

update task

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
    api_instance = openapiclient.TaskApi(api_client)
    task_id = 56 # int | Task ID
    update_task_request_body = openapiclient.TaskUpdateTaskRequestBody() # TaskUpdateTaskRequestBody | 

    try:
        # updateTask task
        api_response = api_instance.task_update_task(task_id, update_task_request_body)
        print("The response of TaskApi->task_update_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->task_update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task ID | 
 **update_task_request_body** | [**TaskUpdateTaskRequestBody**](TaskUpdateTaskRequestBody.md)|  | 

### Return type

[**TaskUpdateTaskResponseBody**](TaskUpdateTaskResponseBody.md)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/gob
 - **Accept**: application/json, application/xml, application/gob

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_update_task_ignore**
> task_update_task_ignore(task_id, update_task_ignore_request_body)

updateTaskIgnore task

update task ignore

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
    api_instance = openapiclient.TaskApi(api_client)
    task_id = 56 # int | Task ID
    update_task_ignore_request_body = openapiclient.TaskUpdateTaskIgnoreRequestBody() # TaskUpdateTaskIgnoreRequestBody | 

    try:
        # updateTaskIgnore task
        api_instance.task_update_task_ignore(task_id, update_task_ignore_request_body)
    except Exception as e:
        print("Exception when calling TaskApi->task_update_task_ignore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task ID | 
 **update_task_ignore_request_body** | [**TaskUpdateTaskIgnoreRequestBody**](TaskUpdateTaskIgnoreRequestBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/gob
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

