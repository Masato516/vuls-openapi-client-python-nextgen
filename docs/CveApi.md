# openapiclient.CveApi

All URIs are relative to *https://rest.2119e7c929.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cve_get_cve_detail**](CveApi.md#cve_get_cve_detail) | **GET** /v1/cve/{cveID} | getCveDetail cve
[**cve_get_cve_list**](CveApi.md#cve_get_cve_list) | **GET** /v1/cves | getCveList cve


# **cve_get_cve_detail**
> CveGetCveDetailResponseBody cve_get_cve_detail(cve_id)

getCveDetail cve

cve detail

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
    api_instance = openapiclient.CveApi(api_client)
    cve_id = 'cve_id_example' # str | Cve ID

    try:
        # getCveDetail cve
        api_response = api_instance.cve_get_cve_detail(cve_id)
        print("The response of CveApi->cve_get_cve_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CveApi->cve_get_cve_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_id** | **str**| Cve ID | 

### Return type

[**CveGetCveDetailResponseBody**](CveGetCveDetailResponseBody.md)

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

# **cve_get_cve_list**
> CveGetCveListResponseBody cve_get_cve_list(page=page, limit=limit, offset=offset, filter_server_id=filter_server_id, filter_role_id=filter_role_id, filter_pkg_id=filter_pkg_id, filter_cpe_id=filter_cpe_id)

getCveList cve

cve list

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
    api_instance = openapiclient.CveApi(api_client)
    page = 1 # int | Page Number (optional) (default to 1)
    limit = 20 # int | Limit (optional) (default to 20)
    offset = 0 # int | Offset (optional) (default to 0)
    filter_server_id = 56 # int | ServerID filter (optional)
    filter_role_id = 56 # int | ServerRoleID filter (optional)
    filter_pkg_id = 56 # int | PackageID filter (optional)
    filter_cpe_id = 56 # int | CpeID filter (optional)

    try:
        # getCveList cve
        api_response = api_instance.cve_get_cve_list(page=page, limit=limit, offset=offset, filter_server_id=filter_server_id, filter_role_id=filter_role_id, filter_pkg_id=filter_pkg_id, filter_cpe_id=filter_cpe_id)
        print("The response of CveApi->cve_get_cve_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CveApi->cve_get_cve_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] [default to 1]
 **limit** | **int**| Limit | [optional] [default to 20]
 **offset** | **int**| Offset | [optional] [default to 0]
 **filter_server_id** | **int**| ServerID filter | [optional] 
 **filter_role_id** | **int**| ServerRoleID filter | [optional] 
 **filter_pkg_id** | **int**| PackageID filter | [optional] 
 **filter_cpe_id** | **int**| CpeID filter | [optional] 

### Return type

[**CveGetCveListResponseBody**](CveGetCveListResponseBody.md)

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

