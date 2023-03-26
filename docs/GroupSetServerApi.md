# openapiclient.GroupSetServerApi

All URIs are relative to *https://rest.2119e7c929.vuls.biz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_set_server_get_group_set_server_detail**](GroupSetServerApi.md#group_set_server_get_group_set_server_detail) | **GET** /v1/groupSet/server/{serverID} | getGroupSetServerDetail groupSetServer
[**group_set_server_get_group_set_server_detail_by_uuid**](GroupSetServerApi.md#group_set_server_get_group_set_server_detail_by_uuid) | **GET** /v1/groupSet/server/uuid/{serverUuid} | getGroupSetServerDetailByUUID groupSetServer
[**group_set_server_get_group_set_server_list**](GroupSetServerApi.md#group_set_server_get_group_set_server_list) | **GET** /v1/groupSet/servers | getGroupSetServerList groupSetServer


# **group_set_server_get_group_set_server_detail**
> GroupSetServerGetGroupSetServerDetailResponseBody group_set_server_get_group_set_server_detail(server_id)

getGroupSetServerDetail groupSetServer

group set server detail

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
    api_instance = openapiclient.GroupSetServerApi(api_client)
    server_id = 56 # int | Server ID

    try:
        # getGroupSetServerDetail groupSetServer
        api_response = api_instance.group_set_server_get_group_set_server_detail(server_id)
        print("The response of GroupSetServerApi->group_set_server_get_group_set_server_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupSetServerApi->group_set_server_get_group_set_server_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| Server ID | 

### Return type

[**GroupSetServerGetGroupSetServerDetailResponseBody**](GroupSetServerGetGroupSetServerDetailResponseBody.md)

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

# **group_set_server_get_group_set_server_detail_by_uuid**
> GroupSetServerGetGroupSetServerDetailByUUIDResponseBody group_set_server_get_group_set_server_detail_by_uuid(server_uuid)

getGroupSetServerDetailByUUID groupSetServer

group set server detail by UUID

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
    api_instance = openapiclient.GroupSetServerApi(api_client)
    server_uuid = 'server_uuid_example' # str | Server UUID

    try:
        # getGroupSetServerDetailByUUID groupSetServer
        api_response = api_instance.group_set_server_get_group_set_server_detail_by_uuid(server_uuid)
        print("The response of GroupSetServerApi->group_set_server_get_group_set_server_detail_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupSetServerApi->group_set_server_get_group_set_server_detail_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_uuid** | **str**| Server UUID | 

### Return type

[**GroupSetServerGetGroupSetServerDetailByUUIDResponseBody**](GroupSetServerGetGroupSetServerDetailByUUIDResponseBody.md)

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

# **group_set_server_get_group_set_server_list**
> GroupSetServerGetGroupSetServerListResponseBody group_set_server_get_group_set_server_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id, filter_role_id=filter_role_id, filter_tag_name=filter_tag_name)

getGroupSetServerList groupSetServer

group set server list

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
    api_instance = openapiclient.GroupSetServerApi(api_client)
    page = 1 # int | Page Number (optional) (default to 1)
    limit = 20 # int | Limit (optional) (default to 20)
    offset = 0 # int | Offset (optional) (default to 0)
    filter_cve_id = 'filter_cve_id_example' # str | CveID filter (optional)
    filter_role_id = 56 # int | ServerRoleID filter (optional)
    filter_tag_name = 'filter_tag_name_example' # str | ServerTagName filter (optional)

    try:
        # getGroupSetServerList groupSetServer
        api_response = api_instance.group_set_server_get_group_set_server_list(page=page, limit=limit, offset=offset, filter_cve_id=filter_cve_id, filter_role_id=filter_role_id, filter_tag_name=filter_tag_name)
        print("The response of GroupSetServerApi->group_set_server_get_group_set_server_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupSetServerApi->group_set_server_get_group_set_server_list: %s\n" % e)
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

[**GroupSetServerGetGroupSetServerListResponseBody**](GroupSetServerGetGroupSetServerListResponseBody.md)

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

