# openapiclient.PkgCpeApi

All URIs are relative to *https://rest.2119e7c929.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pkg_cpe_add_cpe**](PkgCpeApi.md#pkg_cpe_add_cpe) | **POST** /v1/pkgCpe/cpe | addCpe pkgCpe
[**pkg_cpe_delete_cpe**](PkgCpeApi.md#pkg_cpe_delete_cpe) | **DELETE** /v1/pkgCpe/cpe/{cpeID} | deleteCpe pkgCpe
[**pkg_cpe_delete_cpe_deprecated**](PkgCpeApi.md#pkg_cpe_delete_cpe_deprecated) | **DELETE** /v1/pkgCpe/cpe | deleteCpe_deprecated pkgCpe
[**pkg_cpe_get_cpe_detail**](PkgCpeApi.md#pkg_cpe_get_cpe_detail) | **GET** /v1/pkgCpe/cpe/{cpeID} | getCpeDetail pkgCpe
[**pkg_cpe_get_pkg_cpe_list**](PkgCpeApi.md#pkg_cpe_get_pkg_cpe_list) | **GET** /v1/pkgCpes | getPkgCpeList pkgCpe
[**pkg_cpe_get_pkg_detail**](PkgCpeApi.md#pkg_cpe_get_pkg_detail) | **GET** /v1/pkgCpe/pkg/{pkgID} | getPkgDetail pkgCpe


# **pkg_cpe_add_cpe**
> PkgCpeAddCpeResponseBody pkg_cpe_add_cpe(add_cpe_request_body)

addCpe pkgCpe

add cpe

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
    api_instance = openapiclient.PkgCpeApi(api_client)
    add_cpe_request_body = openapiclient.PkgCpeAddCpeRequestBody() # PkgCpeAddCpeRequestBody | 

    try:
        # addCpe pkgCpe
        api_response = api_instance.pkg_cpe_add_cpe(add_cpe_request_body)
        print("The response of PkgCpeApi->pkg_cpe_add_cpe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_add_cpe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_cpe_request_body** | [**PkgCpeAddCpeRequestBody**](PkgCpeAddCpeRequestBody.md)|  | 

### Return type

[**PkgCpeAddCpeResponseBody**](PkgCpeAddCpeResponseBody.md)

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

# **pkg_cpe_delete_cpe**
> pkg_cpe_delete_cpe(cpe_id)

deleteCpe pkgCpe

delete cpe (urlにcpeIDを指定してください。cpeIDの指定のないアクセス方法は今後削除されます。)

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
    api_instance = openapiclient.PkgCpeApi(api_client)
    cpe_id = 56 # int | cpe ID

    try:
        # deleteCpe pkgCpe
        api_instance.pkg_cpe_delete_cpe(cpe_id)
    except Exception as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_delete_cpe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpe_id** | **int**| cpe ID | 

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

# **pkg_cpe_delete_cpe_deprecated**
> pkg_cpe_delete_cpe_deprecated(delete_cpe_deprecated_request_body)

deleteCpe_deprecated pkgCpe

[deprecated] urlにcpeIDを指定して利用してください。cpeIDの指定のないこちらのアクセス方法は今後削除されます。

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
    api_instance = openapiclient.PkgCpeApi(api_client)
    delete_cpe_deprecated_request_body = openapiclient.PkgCpeDeleteCpeDeprecatedRequestBody() # PkgCpeDeleteCpeDeprecatedRequestBody | 

    try:
        # deleteCpe_deprecated pkgCpe
        api_instance.pkg_cpe_delete_cpe_deprecated(delete_cpe_deprecated_request_body)
    except Exception as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_delete_cpe_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_cpe_deprecated_request_body** | [**PkgCpeDeleteCpeDeprecatedRequestBody**](PkgCpeDeleteCpeDeprecatedRequestBody.md)|  | 

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

# **pkg_cpe_get_cpe_detail**
> PkgCpeGetCpeDetailResponseBody pkg_cpe_get_cpe_detail(cpe_id)

getCpeDetail pkgCpe

cpe detail

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
    api_instance = openapiclient.PkgCpeApi(api_client)
    cpe_id = 56 # int | cpe ID

    try:
        # getCpeDetail pkgCpe
        api_response = api_instance.pkg_cpe_get_cpe_detail(cpe_id)
        print("The response of PkgCpeApi->pkg_cpe_get_cpe_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_get_cpe_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpe_id** | **int**| cpe ID | 

### Return type

[**PkgCpeGetCpeDetailResponseBody**](PkgCpeGetCpeDetailResponseBody.md)

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

# **pkg_cpe_get_pkg_cpe_list**
> PkgCpeGetPkgCpeListResponseBody pkg_cpe_get_pkg_cpe_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id, filter_task_id=filter_task_id, filter_server_id=filter_server_id, filter_role_id=filter_role_id)

getPkgCpeList pkgCpe

pkgCpe list

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
    api_instance = openapiclient.PkgCpeApi(api_client)
    page = 1 # int | Page Number (optional) (default to 1)
    limit = 20 # int | Limit (optional) (default to 20)
    offset = 0 # int | Offset (optional) (default to 0)
    filter_cve_id = 'filter_cve_id_example' # str | CveID filter (optional)
    filter_task_id = 56 # int | TaskID filter (optional)
    filter_server_id = 56 # int | ServerID filter (optional)
    filter_role_id = 56 # int | ServerRoleID filter (optional)

    try:
        # getPkgCpeList pkgCpe
        api_response = api_instance.pkg_cpe_get_pkg_cpe_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id, filter_task_id=filter_task_id, filter_server_id=filter_server_id, filter_role_id=filter_role_id)
        print("The response of PkgCpeApi->pkg_cpe_get_pkg_cpe_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_get_pkg_cpe_list: %s\n" % e)
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

[**PkgCpeGetPkgCpeListResponseBody**](PkgCpeGetPkgCpeListResponseBody.md)

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

# **pkg_cpe_get_pkg_detail**
> PkgCpeGetPkgDetailResponseBody pkg_cpe_get_pkg_detail(pkg_id)

getPkgDetail pkgCpe

pkg detail

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
    api_instance = openapiclient.PkgCpeApi(api_client)
    pkg_id = 56 # int | PackageID

    try:
        # getPkgDetail pkgCpe
        api_response = api_instance.pkg_cpe_get_pkg_detail(pkg_id)
        print("The response of PkgCpeApi->pkg_cpe_get_pkg_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PkgCpeApi->pkg_cpe_get_pkg_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkg_id** | **int**| PackageID | 

### Return type

[**PkgCpeGetPkgDetailResponseBody**](PkgCpeGetPkgDetailResponseBody.md)

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

