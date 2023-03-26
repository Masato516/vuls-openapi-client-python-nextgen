# openapiclient.GroupSetPkgCpeApi

All URIs are relative to *https://rest.2119e7c929.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_set_pkg_cpe_get_group_set_cpe_detail**](GroupSetPkgCpeApi.md#group_set_pkg_cpe_get_group_set_cpe_detail) | **GET** /v1/groupSet/pkgCpe/cpe/{cpeID} | getGroupSetCpeDetail groupSetPkgCpe
[**group_set_pkg_cpe_get_group_set_pkg_cpe_list**](GroupSetPkgCpeApi.md#group_set_pkg_cpe_get_group_set_pkg_cpe_list) | **GET** /v1/groupSet/pkgCpes | getGroupSetPkgCpeList groupSetPkgCpe
[**group_set_pkg_cpe_get_group_set_pkg_detail**](GroupSetPkgCpeApi.md#group_set_pkg_cpe_get_group_set_pkg_detail) | **GET** /v1/groupSet/pkgCpe/pkg/{pkgID} | getGroupSetPkgDetail groupSetPkgCpe


# **group_set_pkg_cpe_get_group_set_cpe_detail**
> GroupSetPkgCpeGetGroupSetCpeDetailResponseBody group_set_pkg_cpe_get_group_set_cpe_detail(cpe_id)

getGroupSetCpeDetail groupSetPkgCpe

group set cpe detail

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
    api_instance = openapiclient.GroupSetPkgCpeApi(api_client)
    cpe_id = 56 # int | cpe ID

    try:
        # getGroupSetCpeDetail groupSetPkgCpe
        api_response = api_instance.group_set_pkg_cpe_get_group_set_cpe_detail(cpe_id)
        print("The response of GroupSetPkgCpeApi->group_set_pkg_cpe_get_group_set_cpe_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupSetPkgCpeApi->group_set_pkg_cpe_get_group_set_cpe_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpe_id** | **int**| cpe ID | 

### Return type

[**GroupSetPkgCpeGetGroupSetCpeDetailResponseBody**](GroupSetPkgCpeGetGroupSetCpeDetailResponseBody.md)

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

# **group_set_pkg_cpe_get_group_set_pkg_cpe_list**
> GroupSetPkgCpeGetGroupSetPkgCpeListResponseBody group_set_pkg_cpe_get_group_set_pkg_cpe_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id, filter_task_id=filter_task_id, filter_server_id=filter_server_id, filter_role_id=filter_role_id)

getGroupSetPkgCpeList groupSetPkgCpe

group set pkgCpe list

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
    api_instance = openapiclient.GroupSetPkgCpeApi(api_client)
    page = 1 # int | Page Number (optional) (default to 1)
    limit = 20 # int | Limit (optional) (default to 20)
    offset = 0 # int | Offset (optional) (default to 0)
    filter_cve_id = 'filter_cve_id_example' # str | CveID filter (optional)
    filter_task_id = 56 # int | TaskID filter (optional)
    filter_server_id = 56 # int | ServerID filter (optional)
    filter_role_id = 56 # int | ServerRoleID filter (optional)

    try:
        # getGroupSetPkgCpeList groupSetPkgCpe
        api_response = api_instance.group_set_pkg_cpe_get_group_set_pkg_cpe_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id, filter_task_id=filter_task_id, filter_server_id=filter_server_id, filter_role_id=filter_role_id)
        print("The response of GroupSetPkgCpeApi->group_set_pkg_cpe_get_group_set_pkg_cpe_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupSetPkgCpeApi->group_set_pkg_cpe_get_group_set_pkg_cpe_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] [default to 1]
 **limit** | **int**| Limit | [optional] [default to 20]
 **offset** | **int**| Offset | [optional] [default to 0]
 **filter_cve_id** | **str**| CveID filter | [optional] 
 **filter_task_id** | **int**| TaskID filter | [optional] 
 **filter_server_id** | **int**| ServerID filter | [optional] 
 **filter_role_id** | **int**| ServerRoleID filter | [optional] 

### Return type

[**GroupSetPkgCpeGetGroupSetPkgCpeListResponseBody**](GroupSetPkgCpeGetGroupSetPkgCpeListResponseBody.md)

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

# **group_set_pkg_cpe_get_group_set_pkg_detail**
> GroupSetPkgCpeGetGroupSetPkgDetailResponseBody group_set_pkg_cpe_get_group_set_pkg_detail(pkg_id)

getGroupSetPkgDetail groupSetPkgCpe

group set pkg detail

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
    api_instance = openapiclient.GroupSetPkgCpeApi(api_client)
    pkg_id = 56 # int | PackageID

    try:
        # getGroupSetPkgDetail groupSetPkgCpe
        api_response = api_instance.group_set_pkg_cpe_get_group_set_pkg_detail(pkg_id)
        print("The response of GroupSetPkgCpeApi->group_set_pkg_cpe_get_group_set_pkg_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupSetPkgCpeApi->group_set_pkg_cpe_get_group_set_pkg_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkg_id** | **int**| PackageID | 

### Return type

[**GroupSetPkgCpeGetGroupSetPkgDetailResponseBody**](GroupSetPkgCpeGetGroupSetPkgDetailResponseBody.md)

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

