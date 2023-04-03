# coding: utf-8

"""
    Future Vuls Public API

    Future Vuls Public API  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr, conint

from typing import Optional

from openapiclient.models.lockfile_add_lockfile_request_body import LockfileAddLockfileRequestBody
from openapiclient.models.lockfile_add_lockfile_response_body import LockfileAddLockfileResponseBody
from openapiclient.models.lockfile_get_lockfile_detail_response_body import LockfileGetLockfileDetailResponseBody
from openapiclient.models.lockfile_get_lockfile_list_response_body import LockfileGetLockfileListResponseBody
from openapiclient.models.lockfile_update_lockfile_request_body import LockfileUpdateLockfileRequestBody
from openapiclient.models.lockfile_update_lockfile_response_body import LockfileUpdateLockfileResponseBody

from openapiclient.api_client import ApiClient
from openapiclient.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class LockfileApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def lockfile_add_lockfile(self, add_lockfile_request_body : LockfileAddLockfileRequestBody, **kwargs) -> LockfileAddLockfileResponseBody:  # noqa: E501
        """addLockfile lockfile  # noqa: E501

        add lockfile  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_add_lockfile(add_lockfile_request_body, async_req=True)
        >>> result = thread.get()

        :param add_lockfile_request_body: (required)
        :type add_lockfile_request_body: LockfileAddLockfileRequestBody
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: LockfileAddLockfileResponseBody
        """
        kwargs['_return_http_data_only'] = True
        return self.lockfile_add_lockfile_with_http_info(add_lockfile_request_body, **kwargs)  # noqa: E501

    @validate_arguments
    def lockfile_add_lockfile_with_http_info(self, add_lockfile_request_body : LockfileAddLockfileRequestBody, **kwargs):  # noqa: E501
        """addLockfile lockfile  # noqa: E501

        add lockfile  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_add_lockfile_with_http_info(add_lockfile_request_body, async_req=True)
        >>> result = thread.get()

        :param add_lockfile_request_body: (required)
        :type add_lockfile_request_body: LockfileAddLockfileRequestBody
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(LockfileAddLockfileResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'add_lockfile_request_body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lockfile_add_lockfile" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['add_lockfile_request_body']:
            _body_params = _params['add_lockfile_request_body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'application/gob'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'application/xml', 'application/gob']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['api_key_header_Authorization']  # noqa: E501

        _response_types_map = {
            '200': "LockfileAddLockfileResponseBody",
        }

        return self.api_client.call_api(
            '/v1/lockfile', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def lockfile_delete_lockfile(self, lockfile_id : Annotated[StrictInt, Field(..., description="Lockfile ID")], **kwargs) -> None:  # noqa: E501
        """deleteLockfile lockfile  # noqa: E501

        lockfile delete  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_delete_lockfile(lockfile_id, async_req=True)
        >>> result = thread.get()

        :param lockfile_id: Lockfile ID (required)
        :type lockfile_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.lockfile_delete_lockfile_with_http_info(lockfile_id, **kwargs)  # noqa: E501

    @validate_arguments
    def lockfile_delete_lockfile_with_http_info(self, lockfile_id : Annotated[StrictInt, Field(..., description="Lockfile ID")], **kwargs):  # noqa: E501
        """deleteLockfile lockfile  # noqa: E501

        lockfile delete  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_delete_lockfile_with_http_info(lockfile_id, async_req=True)
        >>> result = thread.get()

        :param lockfile_id: Lockfile ID (required)
        :type lockfile_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'lockfile_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lockfile_delete_lockfile" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['lockfile_id']:
            _path_params['lockfileID'] = _params['lockfile_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['api_key_header_Authorization']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/v1/lockfile/{lockfileID}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def lockfile_get_lockfile_detail(self, lockfile_id : Annotated[StrictInt, Field(..., description="Lockfile ID")], **kwargs) -> LockfileGetLockfileDetailResponseBody:  # noqa: E501
        """getLockfileDetail lockfile  # noqa: E501

        lockfile detail  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_get_lockfile_detail(lockfile_id, async_req=True)
        >>> result = thread.get()

        :param lockfile_id: Lockfile ID (required)
        :type lockfile_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: LockfileGetLockfileDetailResponseBody
        """
        kwargs['_return_http_data_only'] = True
        return self.lockfile_get_lockfile_detail_with_http_info(lockfile_id, **kwargs)  # noqa: E501

    @validate_arguments
    def lockfile_get_lockfile_detail_with_http_info(self, lockfile_id : Annotated[StrictInt, Field(..., description="Lockfile ID")], **kwargs):  # noqa: E501
        """getLockfileDetail lockfile  # noqa: E501

        lockfile detail  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_get_lockfile_detail_with_http_info(lockfile_id, async_req=True)
        >>> result = thread.get()

        :param lockfile_id: Lockfile ID (required)
        :type lockfile_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(LockfileGetLockfileDetailResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'lockfile_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lockfile_get_lockfile_detail" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['lockfile_id']:
            _path_params['lockfileID'] = _params['lockfile_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'application/gob'])  # noqa: E501

        # authentication setting
        _auth_settings = ['api_key_header_Authorization']  # noqa: E501

        _response_types_map = {
            '200': "LockfileGetLockfileDetailResponseBody",
        }

        return self.api_client.call_api(
            '/v1/lockfile/{lockfileID}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def lockfile_get_lockfile_list(self, page : Annotated[Optional[conint(strict=True, ge=1)], Field(description="Page Number")] = None, limit : Annotated[Optional[conint(strict=True, le=1000, ge=1)], Field(description="Limit")] = None, offset : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset")] = None, filter_server_id : Annotated[Optional[StrictInt], Field(description="ServerID filter")] = None, filter_path : Annotated[Optional[StrictStr], Field(description="Path filter")] = None, **kwargs) -> LockfileGetLockfileListResponseBody:  # noqa: E501
        """getLockfileList lockfile  # noqa: E501

        lockfile list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_get_lockfile_list(page, limit, offset, filter_server_id, filter_path, async_req=True)
        >>> result = thread.get()

        :param page: Page Number
        :type page: int
        :param limit: Limit
        :type limit: int
        :param offset: Offset
        :type offset: int
        :param filter_server_id: ServerID filter
        :type filter_server_id: int
        :param filter_path: Path filter
        :type filter_path: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: LockfileGetLockfileListResponseBody
        """
        kwargs['_return_http_data_only'] = True
        return self.lockfile_get_lockfile_list_with_http_info(page, limit, offset, filter_server_id, filter_path, **kwargs)  # noqa: E501

    @validate_arguments
    def lockfile_get_lockfile_list_with_http_info(self, page : Annotated[Optional[conint(strict=True, ge=1)], Field(description="Page Number")] = None, limit : Annotated[Optional[conint(strict=True, le=1000, ge=1)], Field(description="Limit")] = None, offset : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset")] = None, filter_server_id : Annotated[Optional[StrictInt], Field(description="ServerID filter")] = None, filter_path : Annotated[Optional[StrictStr], Field(description="Path filter")] = None, **kwargs):  # noqa: E501
        """getLockfileList lockfile  # noqa: E501

        lockfile list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_get_lockfile_list_with_http_info(page, limit, offset, filter_server_id, filter_path, async_req=True)
        >>> result = thread.get()

        :param page: Page Number
        :type page: int
        :param limit: Limit
        :type limit: int
        :param offset: Offset
        :type offset: int
        :param filter_server_id: ServerID filter
        :type filter_server_id: int
        :param filter_path: Path filter
        :type filter_path: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(LockfileGetLockfileListResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'page',
            'limit',
            'offset',
            'filter_server_id',
            'filter_path'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lockfile_get_lockfile_list" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('filter_server_id') is not None:  # noqa: E501
            _query_params.append(('filterServerID', _params['filter_server_id']))

        if _params.get('filter_path') is not None:  # noqa: E501
            _query_params.append(('filterPath', _params['filter_path']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'application/gob'])  # noqa: E501

        # authentication setting
        _auth_settings = ['api_key_header_Authorization']  # noqa: E501

        _response_types_map = {
            '200': "LockfileGetLockfileListResponseBody",
        }

        return self.api_client.call_api(
            '/v1/lockfiles', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def lockfile_update_lockfile(self, lockfile_id : Annotated[StrictInt, Field(..., description="Lockfile ID")], update_lockfile_request_body : LockfileUpdateLockfileRequestBody, **kwargs) -> LockfileUpdateLockfileResponseBody:  # noqa: E501
        """updateLockfile lockfile  # noqa: E501

        update lockfile  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_update_lockfile(lockfile_id, update_lockfile_request_body, async_req=True)
        >>> result = thread.get()

        :param lockfile_id: Lockfile ID (required)
        :type lockfile_id: int
        :param update_lockfile_request_body: (required)
        :type update_lockfile_request_body: LockfileUpdateLockfileRequestBody
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: LockfileUpdateLockfileResponseBody
        """
        kwargs['_return_http_data_only'] = True
        return self.lockfile_update_lockfile_with_http_info(lockfile_id, update_lockfile_request_body, **kwargs)  # noqa: E501

    @validate_arguments
    def lockfile_update_lockfile_with_http_info(self, lockfile_id : Annotated[StrictInt, Field(..., description="Lockfile ID")], update_lockfile_request_body : LockfileUpdateLockfileRequestBody, **kwargs):  # noqa: E501
        """updateLockfile lockfile  # noqa: E501

        update lockfile  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_update_lockfile_with_http_info(lockfile_id, update_lockfile_request_body, async_req=True)
        >>> result = thread.get()

        :param lockfile_id: Lockfile ID (required)
        :type lockfile_id: int
        :param update_lockfile_request_body: (required)
        :type update_lockfile_request_body: LockfileUpdateLockfileRequestBody
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(LockfileUpdateLockfileResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'lockfile_id',
            'update_lockfile_request_body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lockfile_update_lockfile" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['lockfile_id']:
            _path_params['lockfileID'] = _params['lockfile_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_lockfile_request_body']:
            _body_params = _params['update_lockfile_request_body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'application/gob'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'application/xml', 'application/gob']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['api_key_header_Authorization']  # noqa: E501

        _response_types_map = {
            '200': "LockfileUpdateLockfileResponseBody",
        }

        return self.api_client.call_api(
            '/v1/lockfile/{lockfileID}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
