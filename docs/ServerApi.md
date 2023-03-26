# openapiclient.ServerApi

All URIs are relative to *https://rest.2119e7c929.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**server_create_pkg_paste_server**](ServerApi.md#server_create_pkg_paste_server) | **POST** /v1/server/paste | createPkgPasteServer server
[**server_delete_server**](ServerApi.md#server_delete_server) | **DELETE** /v1/server/{serverID} | deleteServer server
[**server_get_server_detail**](ServerApi.md#server_get_server_detail) | **GET** /v1/server/{serverID} | getServerDetail server
[**server_get_server_detail_by_uuid**](ServerApi.md#server_get_server_detail_by_uuid) | **GET** /v1/server/uuid/{serverUuid} | getServerDetailByUUID server
[**server_get_server_list**](ServerApi.md#server_get_server_list) | **GET** /v1/servers | getServerList server
[**server_scan_server**](ServerApi.md#server_scan_server) | **POST** /v1/server/scan/{serverID} | scanServer server
[**server_update_pkg_paste_server**](ServerApi.md#server_update_pkg_paste_server) | **PUT** /v1/server/paste/{serverID} | updatePkgPasteServer server
[**server_update_server**](ServerApi.md#server_update_server) | **PUT** /v1/server/{serverID} | updateServer server


# **server_create_pkg_paste_server**
> ServerCreatePkgPasteServerResponseBody server_create_pkg_paste_server(create_pkg_paste_server_request_body)

createPkgPasteServer server

create paste server

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
    api_instance = openapiclient.ServerApi(api_client)
    create_pkg_paste_server_request_body = openapiclient.ServerCreatePkgPasteServerRequestBody() # ServerCreatePkgPasteServerRequestBody | 

    try:
        # createPkgPasteServer server
        api_response = api_instance.server_create_pkg_paste_server(create_pkg_paste_server_request_body)
        print("The response of ServerApi->server_create_pkg_paste_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->server_create_pkg_paste_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_pkg_paste_server_request_body** | [**ServerCreatePkgPasteServerRequestBody**](ServerCreatePkgPasteServerRequestBody.md)|  | 

### Return type

[**ServerCreatePkgPasteServerResponseBody**](ServerCreatePkgPasteServerResponseBody.md)

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

# **server_delete_server**
> server_delete_server(server_id)

deleteServer server

server delete

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
    api_instance = openapiclient.ServerApi(api_client)
    server_id = 56 # int | Server ID

    try:
        # deleteServer server
        api_instance.server_delete_server(server_id)
    except Exception as e:
        print("Exception when calling ServerApi->server_delete_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Server ID | 

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

# **server_get_server_detail**
> ServerGetServerDetailResponseBody server_get_server_detail(server_id)

getServerDetail server

server detail

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
    api_instance = openapiclient.ServerApi(api_client)
    server_id = 56 # int | Server ID

    try:
        # getServerDetail server
        api_response = api_instance.server_get_server_detail(server_id)
        print("The response of ServerApi->server_get_server_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->server_get_server_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Server ID | 

### Return type

[**ServerGetServerDetailResponseBody**](ServerGetServerDetailResponseBody.md)

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

# **server_get_server_detail_by_uuid**
> ServerGetServerDetailByUUIDResponseBody server_get_server_detail_by_uuid(server_uuid)

getServerDetailByUUID server

server detail by UUID

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
    api_instance = openapiclient.ServerApi(api_client)
    server_uuid = 'server_uuid_example' # str | Server UUID

    try:
        # getServerDetailByUUID server
        api_response = api_instance.server_get_server_detail_by_uuid(server_uuid)
        print("The response of ServerApi->server_get_server_detail_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->server_get_server_detail_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_uuid** | **str**| Server UUID | 

### Return type

[**ServerGetServerDetailByUUIDResponseBody**](ServerGetServerDetailByUUIDResponseBody.md)

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

# **server_get_server_list**
> ServerGetServerListResponseBody server_get_server_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id, filter_role_id=filter_role_id, filter_tag_name=filter_tag_name)

getServerList server

server list

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
    api_instance = openapiclient.ServerApi(api_client)
    page = 1 # int | Page Number (optional) (default to 1)
    limit = 20 # int | Limit (optional) (default to 20)
    offset = 0 # int | Offset (optional) (default to 0)
    filter_cve_id = 'filter_cve_id_example' # str | CveID filter (optional)
    filter_role_id = 56 # int | ServerRoleID filter (optional)
    filter_tag_name = 'filter_tag_name_example' # str | ServerTagName filter (optional)

    try:
        # getServerList server
        api_response = api_instance.server_get_server_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id, filter_role_id=filter_role_id, filter_tag_name=filter_tag_name)
        print("The response of ServerApi->server_get_server_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->server_get_server_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] [default to 1]
 **limit** | **int**| Limit | [optional] [default to 20]
 **offset** | **int**| Offset | [optional] [default to 0]
 **filter_cve_id** | **str**| CveID filter | [optional] 
 **filter_role_id** | **int**| ServerRoleID filter | [optional] 
 **filter_tag_name** | **str**| ServerTagName filter | [optional] 

### Return type

[**ServerGetServerListResponseBody**](ServerGetServerListResponseBody.md)

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

# **server_scan_server**
> server_scan_server(server_id)

scanServer server

scan server manually

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
    api_instance = openapiclient.ServerApi(api_client)
    server_id = 56 # int | Server ID

    try:
        # scanServer server
        api_instance.server_scan_server(server_id)
    except Exception as e:
        print("Exception when calling ServerApi->server_scan_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Server ID | 

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

# **server_update_pkg_paste_server**
> server_update_pkg_paste_server(server_id, update_pkg_paste_server_request_body)

updatePkgPasteServer server

update paste server

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
    api_instance = openapiclient.ServerApi(api_client)
    server_id = 56 # int | Server ID
    update_pkg_paste_server_request_body = openapiclient.ServerUpdatePkgPasteServerRequestBody() # ServerUpdatePkgPasteServerRequestBody | 

    try:
        # updatePkgPasteServer server
        api_instance.server_update_pkg_paste_server(server_id, update_pkg_paste_server_request_body)
    except Exception as e:
        print("Exception when calling ServerApi->server_update_pkg_paste_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Server ID | 
 **update_pkg_paste_server_request_body** | [**ServerUpdatePkgPasteServerRequestBody**](ServerUpdatePkgPasteServerRequestBody.md)|  | 

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

# **server_update_server**
> ServerUpdateServerResponseBody server_update_server(server_id, update_server_request_body)

updateServer server

update server

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
    api_instance = openapiclient.ServerApi(api_client)
    server_id = 56 # int | Server ID
    update_server_request_body = openapiclient.ServerUpdateServerRequestBody() # ServerUpdateServerRequestBody | 

    try:
        # updateServer server
        api_response = api_instance.server_update_server(server_id, update_server_request_body)
        print("The response of ServerApi->server_update_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->server_update_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Server ID | 
 **update_server_request_body** | [**ServerUpdateServerRequestBody**](ServerUpdateServerRequestBody.md)|  | 

### Return type

[**ServerUpdateServerResponseBody**](ServerUpdateServerResponseBody.md)

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

