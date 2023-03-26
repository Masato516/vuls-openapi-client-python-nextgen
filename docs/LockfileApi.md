# openapiclient.LockfileApi

All URIs are relative to *https://rest.2119e7c929.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lockfile_add_lockfile**](LockfileApi.md#lockfile_add_lockfile) | **POST** /v1/lockfile | addLockfile lockfile
[**lockfile_delete_lockfile**](LockfileApi.md#lockfile_delete_lockfile) | **DELETE** /v1/lockfile/{lockfileID} | deleteLockfile lockfile
[**lockfile_get_lockfile_detail**](LockfileApi.md#lockfile_get_lockfile_detail) | **GET** /v1/lockfile/{lockfileID} | getLockfileDetail lockfile
[**lockfile_get_lockfile_list**](LockfileApi.md#lockfile_get_lockfile_list) | **GET** /v1/lockfiles | getLockfileList lockfile
[**lockfile_update_lockfile**](LockfileApi.md#lockfile_update_lockfile) | **PUT** /v1/lockfile/{lockfileID} | updateLockfile lockfile


# **lockfile_add_lockfile**
> LockfileAddLockfileResponseBody lockfile_add_lockfile(add_lockfile_request_body)

addLockfile lockfile

add lockfile

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
    api_instance = openapiclient.LockfileApi(api_client)
    add_lockfile_request_body = openapiclient.LockfileAddLockfileRequestBody() # LockfileAddLockfileRequestBody | 

    try:
        # addLockfile lockfile
        api_response = api_instance.lockfile_add_lockfile(add_lockfile_request_body)
        print("The response of LockfileApi->lockfile_add_lockfile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LockfileApi->lockfile_add_lockfile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_lockfile_request_body** | [**LockfileAddLockfileRequestBody**](LockfileAddLockfileRequestBody.md)|  | 

### Return type

[**LockfileAddLockfileResponseBody**](LockfileAddLockfileResponseBody.md)

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

# **lockfile_delete_lockfile**
> lockfile_delete_lockfile(lockfile_id)

deleteLockfile lockfile

lockfile delete

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
    api_instance = openapiclient.LockfileApi(api_client)
    lockfile_id = 56 # int | Lockfile ID

    try:
        # deleteLockfile lockfile
        api_instance.lockfile_delete_lockfile(lockfile_id)
    except Exception as e:
        print("Exception when calling LockfileApi->lockfile_delete_lockfile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lockfile_id** | **int**| Lockfile ID | 

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

# **lockfile_get_lockfile_detail**
> LockfileGetLockfileDetailResponseBody lockfile_get_lockfile_detail(lockfile_id)

getLockfileDetail lockfile

lockfile detail

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
    api_instance = openapiclient.LockfileApi(api_client)
    lockfile_id = 56 # int | Lockfile ID

    try:
        # getLockfileDetail lockfile
        api_response = api_instance.lockfile_get_lockfile_detail(lockfile_id)
        print("The response of LockfileApi->lockfile_get_lockfile_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LockfileApi->lockfile_get_lockfile_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lockfile_id** | **int**| Lockfile ID | 

### Return type

[**LockfileGetLockfileDetailResponseBody**](LockfileGetLockfileDetailResponseBody.md)

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

# **lockfile_get_lockfile_list**
> LockfileGetLockfileListResponseBody lockfile_get_lockfile_list(page=page, limit=limit, offset=offset, filter_server_id=filter_server_id, filter_path=filter_path)

getLockfileList lockfile

lockfile list

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
    api_instance = openapiclient.LockfileApi(api_client)
    page = 1 # int | Page Number (optional) (default to 1)
    limit = 20 # int | Limit (optional) (default to 20)
    offset = 0 # int | Offset (optional) (default to 0)
    filter_server_id = 56 # int | ServerID filter (optional)
    filter_path = 'filter_path_example' # str | Path filter (optional)

    try:
        # getLockfileList lockfile
        api_response = api_instance.lockfile_get_lockfile_list(page=page, limit=limit, offset=offset, filter_server_id=filter_server_id, filter_path=filter_path)
        print("The response of LockfileApi->lockfile_get_lockfile_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LockfileApi->lockfile_get_lockfile_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] [default to 1]
 **limit** | **int**| Limit | [optional] [default to 20]
 **offset** | **int**| Offset | [optional] [default to 0]
 **filter_server_id** | **int**| ServerID filter | [optional] 
 **filter_path** | **str**| Path filter | [optional] 

### Return type

[**LockfileGetLockfileListResponseBody**](LockfileGetLockfileListResponseBody.md)

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

# **lockfile_update_lockfile**
> LockfileUpdateLockfileResponseBody lockfile_update_lockfile(lockfile_id, update_lockfile_request_body)

updateLockfile lockfile

update lockfile

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
    api_instance = openapiclient.LockfileApi(api_client)
    lockfile_id = 56 # int | Lockfile ID
    update_lockfile_request_body = openapiclient.LockfileUpdateLockfileRequestBody() # LockfileUpdateLockfileRequestBody | 

    try:
        # updateLockfile lockfile
        api_response = api_instance.lockfile_update_lockfile(lockfile_id, update_lockfile_request_body)
        print("The response of LockfileApi->lockfile_update_lockfile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LockfileApi->lockfile_update_lockfile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lockfile_id** | **int**| Lockfile ID | 
 **update_lockfile_request_body** | [**LockfileUpdateLockfileRequestBody**](LockfileUpdateLockfileRequestBody.md)|  | 

### Return type

[**LockfileUpdateLockfileResponseBody**](LockfileUpdateLockfileResponseBody.md)

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

