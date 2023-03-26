# openapiclient.RoleApi

All URIs are relative to *https://rest.2119e7c929.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**role_delete_role**](RoleApi.md#role_delete_role) | **DELETE** /v1/role/{roleID} | deleteRole role
[**role_get_role_detail**](RoleApi.md#role_get_role_detail) | **GET** /v1/role/{roleID} | getRoleDetail role
[**role_get_role_list**](RoleApi.md#role_get_role_list) | **GET** /v1/roles | getRoleList role
[**role_update_role**](RoleApi.md#role_update_role) | **PUT** /v1/role/{roleID} | updateRole role


# **role_delete_role**
> role_delete_role(role_id)

deleteRole role

role delete

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
    api_instance = openapiclient.RoleApi(api_client)
    role_id = 56 # int | Role ID

    try:
        # deleteRole role
        api_instance.role_delete_role(role_id)
    except Exception as e:
        print("Exception when calling RoleApi->role_delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| Role ID | 

### Return type

void (empty response body)

### Authorization

[api_key_header_Authorization](../README.md#api_key_header_Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_get_role_detail**
> RoleGetRoleDetailResponseBody role_get_role_detail(role_id)

getRoleDetail role

role detail

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
    api_instance = openapiclient.RoleApi(api_client)
    role_id = 56 # int | Role ID

    try:
        # getRoleDetail role
        api_response = api_instance.role_get_role_detail(role_id)
        print("The response of RoleApi->role_get_role_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->role_get_role_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| Role ID | 

### Return type

[**RoleGetRoleDetailResponseBody**](RoleGetRoleDetailResponseBody.md)

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

# **role_get_role_list**
> RoleGetRoleListResponseBody role_get_role_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id)

getRoleList role

role list

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
    api_instance = openapiclient.RoleApi(api_client)
    page = 1 # int | Page Number (default: 1) (optional) (default to 1)
    limit = 20 # int | Limit (default: 20, max: 100) (optional) (default to 20)
    offset = 0 # int | Offset (optional) (default to 0)
    filter_cve_id = 'filter_cve_id_example' # str | CveID filter (optional)

    try:
        # getRoleList role
        api_response = api_instance.role_get_role_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id)
        print("The response of RoleApi->role_get_role_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->role_get_role_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number (default: 1) | [optional] [default to 1]
 **limit** | **int**| Limit (default: 20, max: 100) | [optional] [default to 20]
 **offset** | **int**| Offset | [optional] [default to 0]
 **filter_cve_id** | **str**| CveID filter | [optional] 

### Return type

[**RoleGetRoleListResponseBody**](RoleGetRoleListResponseBody.md)

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

# **role_update_role**
> RoleUpdateRoleResponseBody role_update_role(role_id, update_role_request_body)

updateRole role

update role

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
    api_instance = openapiclient.RoleApi(api_client)
    role_id = 56 # int | Role ID
    update_role_request_body = openapiclient.RoleUpdateRoleRequestBody() # RoleUpdateRoleRequestBody | 

    try:
        # updateRole role
        api_response = api_instance.role_update_role(role_id, update_role_request_body)
        print("The response of RoleApi->role_update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->role_update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| Role ID | 
 **update_role_request_body** | [**RoleUpdateRoleRequestBody**](RoleUpdateRoleRequestBody.md)|  | 

### Return type

[**RoleUpdateRoleResponseBody**](RoleUpdateRoleResponseBody.md)

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

