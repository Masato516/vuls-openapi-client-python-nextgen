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

from pydantic import Field, StrictBool, StrictInt, StrictStr, conint, conlist, validator

from typing import Optional

from openapiclient.models.group_set_task_get_group_set_task_detail_response_body import GroupSetTaskGetGroupSetTaskDetailResponseBody
from openapiclient.models.group_set_task_get_group_set_task_list_response_body import GroupSetTaskGetGroupSetTaskListResponseBody

from openapiclient.api_client import ApiClient
from openapiclient.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class GroupSetTaskApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def group_set_task_get_group_set_task_detail(self, task_id : Annotated[StrictInt, Field(..., description="Task ID")], **kwargs) -> GroupSetTaskGetGroupSetTaskDetailResponseBody:  # noqa: E501
        """getGroupSetTaskDetail groupSetTask  # noqa: E501

        group set task detail  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.group_set_task_get_group_set_task_detail(task_id, async_req=True)
        >>> result = thread.get()

        :param task_id: Task ID (required)
        :type task_id: int
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
        :rtype: GroupSetTaskGetGroupSetTaskDetailResponseBody
        """
        kwargs['_return_http_data_only'] = True
        return self.group_set_task_get_group_set_task_detail_with_http_info(task_id, **kwargs)  # noqa: E501

    @validate_arguments
    def group_set_task_get_group_set_task_detail_with_http_info(self, task_id : Annotated[StrictInt, Field(..., description="Task ID")], **kwargs):  # noqa: E501
        """getGroupSetTaskDetail groupSetTask  # noqa: E501

        group set task detail  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.group_set_task_get_group_set_task_detail_with_http_info(task_id, async_req=True)
        >>> result = thread.get()

        :param task_id: Task ID (required)
        :type task_id: int
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
        :rtype: tuple(GroupSetTaskGetGroupSetTaskDetailResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'task_id'
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
                    " to method group_set_task_get_group_set_task_detail" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['task_id']:
            _path_params['taskID'] = _params['task_id']


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
            '200': "GroupSetTaskGetGroupSetTaskDetailResponseBody",
        }

        return self.api_client.call_api(
            '/v1/groupSet/task/{taskID}', 'GET',
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
    def group_set_task_get_group_set_task_list(self, page : Annotated[Optional[conint(strict=True, ge=1)], Field(description="Page Number")] = None, limit : Annotated[Optional[conint(strict=True, le=1000, ge=1)], Field(description="Limit")] = None, offset : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset")] = None, filter_status : Annotated[Optional[conlist(StrictStr)], Field(description="Status filter")] = None, filter_priority : Annotated[Optional[conlist(StrictStr)], Field(description="Priority filter")] = None, filter_ignore : Annotated[Optional[StrictBool], Field(description="Ignore filter(trueの場合は、非表示のものを取得しない。falseの場合は全件取得)")] = None, filter_main_user_ids : Annotated[Optional[conlist(StrictInt)], Field(description="MainUserIDs filter")] = None, filter_sub_user_ids : Annotated[Optional[conlist(StrictInt)], Field(description="SubUserIDs filter")] = None, filter_cve_id : Annotated[Optional[StrictStr], Field(description="CveID filter")] = None, filter_server_id : Annotated[Optional[conint(strict=True, ge=1)], Field(description="ServerID filter")] = None, filter_role_id : Annotated[Optional[conint(strict=True, ge=1)], Field(description="ServerRoleID filter")] = None, filter_pkg_id : Annotated[Optional[conint(strict=True, ge=1)], Field(description="PackageID filter")] = None, filter_cpe_id : Annotated[Optional[conint(strict=True, ge=1)], Field(description="CpeID filter")] = None, **kwargs) -> GroupSetTaskGetGroupSetTaskListResponseBody:  # noqa: E501
        """getGroupSetTaskList groupSetTask  # noqa: E501

        group set task list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.group_set_task_get_group_set_task_list(page, limit, offset, filter_status, filter_priority, filter_ignore, filter_main_user_ids, filter_sub_user_ids, filter_cve_id, filter_server_id, filter_role_id, filter_pkg_id, filter_cpe_id, async_req=True)
        >>> result = thread.get()

        :param page: Page Number
        :type page: int
        :param limit: Limit
        :type limit: int
        :param offset: Offset
        :type offset: int
        :param filter_status: Status filter
        :type filter_status: List[str]
        :param filter_priority: Priority filter
        :type filter_priority: List[str]
        :param filter_ignore: Ignore filter(trueの場合は、非表示のものを取得しない。falseの場合は全件取得)
        :type filter_ignore: bool
        :param filter_main_user_ids: MainUserIDs filter
        :type filter_main_user_ids: List[int]
        :param filter_sub_user_ids: SubUserIDs filter
        :type filter_sub_user_ids: List[int]
        :param filter_cve_id: CveID filter
        :type filter_cve_id: str
        :param filter_server_id: ServerID filter
        :type filter_server_id: int
        :param filter_role_id: ServerRoleID filter
        :type filter_role_id: int
        :param filter_pkg_id: PackageID filter
        :type filter_pkg_id: int
        :param filter_cpe_id: CpeID filter
        :type filter_cpe_id: int
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
        :rtype: GroupSetTaskGetGroupSetTaskListResponseBody
        """
        kwargs['_return_http_data_only'] = True
        return self.group_set_task_get_group_set_task_list_with_http_info(page, limit, offset, filter_status, filter_priority, filter_ignore, filter_main_user_ids, filter_sub_user_ids, filter_cve_id, filter_server_id, filter_role_id, filter_pkg_id, filter_cpe_id, **kwargs)  # noqa: E501

    @validate_arguments
    def group_set_task_get_group_set_task_list_with_http_info(self, page : Annotated[Optional[conint(strict=True, ge=1)], Field(description="Page Number")] = None, limit : Annotated[Optional[conint(strict=True, le=1000, ge=1)], Field(description="Limit")] = None, offset : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset")] = None, filter_status : Annotated[Optional[conlist(StrictStr)], Field(description="Status filter")] = None, filter_priority : Annotated[Optional[conlist(StrictStr)], Field(description="Priority filter")] = None, filter_ignore : Annotated[Optional[StrictBool], Field(description="Ignore filter(trueの場合は、非表示のものを取得しない。falseの場合は全件取得)")] = None, filter_main_user_ids : Annotated[Optional[conlist(StrictInt)], Field(description="MainUserIDs filter")] = None, filter_sub_user_ids : Annotated[Optional[conlist(StrictInt)], Field(description="SubUserIDs filter")] = None, filter_cve_id : Annotated[Optional[StrictStr], Field(description="CveID filter")] = None, filter_server_id : Annotated[Optional[conint(strict=True, ge=1)], Field(description="ServerID filter")] = None, filter_role_id : Annotated[Optional[conint(strict=True, ge=1)], Field(description="ServerRoleID filter")] = None, filter_pkg_id : Annotated[Optional[conint(strict=True, ge=1)], Field(description="PackageID filter")] = None, filter_cpe_id : Annotated[Optional[conint(strict=True, ge=1)], Field(description="CpeID filter")] = None, **kwargs):  # noqa: E501
        """getGroupSetTaskList groupSetTask  # noqa: E501

        group set task list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.group_set_task_get_group_set_task_list_with_http_info(page, limit, offset, filter_status, filter_priority, filter_ignore, filter_main_user_ids, filter_sub_user_ids, filter_cve_id, filter_server_id, filter_role_id, filter_pkg_id, filter_cpe_id, async_req=True)
        >>> result = thread.get()

        :param page: Page Number
        :type page: int
        :param limit: Limit
        :type limit: int
        :param offset: Offset
        :type offset: int
        :param filter_status: Status filter
        :type filter_status: List[str]
        :param filter_priority: Priority filter
        :type filter_priority: List[str]
        :param filter_ignore: Ignore filter(trueの場合は、非表示のものを取得しない。falseの場合は全件取得)
        :type filter_ignore: bool
        :param filter_main_user_ids: MainUserIDs filter
        :type filter_main_user_ids: List[int]
        :param filter_sub_user_ids: SubUserIDs filter
        :type filter_sub_user_ids: List[int]
        :param filter_cve_id: CveID filter
        :type filter_cve_id: str
        :param filter_server_id: ServerID filter
        :type filter_server_id: int
        :param filter_role_id: ServerRoleID filter
        :type filter_role_id: int
        :param filter_pkg_id: PackageID filter
        :type filter_pkg_id: int
        :param filter_cpe_id: CpeID filter
        :type filter_cpe_id: int
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
        :rtype: tuple(GroupSetTaskGetGroupSetTaskListResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'page',
            'limit',
            'offset',
            'filter_status',
            'filter_priority',
            'filter_ignore',
            'filter_main_user_ids',
            'filter_sub_user_ids',
            'filter_cve_id',
            'filter_server_id',
            'filter_role_id',
            'filter_pkg_id',
            'filter_cpe_id'
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
                    " to method group_set_task_get_group_set_task_list" % _key
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

        if _params.get('filter_status') is not None:  # noqa: E501
            _query_params.append(('filterStatus', _params['filter_status']))
            _collection_formats['filterStatus'] = 'multi'

        if _params.get('filter_priority') is not None:  # noqa: E501
            _query_params.append(('filterPriority', _params['filter_priority']))
            _collection_formats['filterPriority'] = 'multi'

        if _params.get('filter_ignore') is not None:  # noqa: E501
            _query_params.append(('filterIgnore', _params['filter_ignore']))

        if _params.get('filter_main_user_ids') is not None:  # noqa: E501
            _query_params.append(('filterMainUserIDs', _params['filter_main_user_ids']))
            _collection_formats['filterMainUserIDs'] = 'multi'

        if _params.get('filter_sub_user_ids') is not None:  # noqa: E501
            _query_params.append(('filterSubUserIDs', _params['filter_sub_user_ids']))
            _collection_formats['filterSubUserIDs'] = 'multi'

        if _params.get('filter_cve_id') is not None:  # noqa: E501
            _query_params.append(('filterCveID', _params['filter_cve_id']))

        if _params.get('filter_server_id') is not None:  # noqa: E501
            _query_params.append(('filterServerID', _params['filter_server_id']))

        if _params.get('filter_role_id') is not None:  # noqa: E501
            _query_params.append(('filterRoleID', _params['filter_role_id']))

        if _params.get('filter_pkg_id') is not None:  # noqa: E501
            _query_params.append(('filterPkgID', _params['filter_pkg_id']))

        if _params.get('filter_cpe_id') is not None:  # noqa: E501
            _query_params.append(('filterCpeID', _params['filter_cpe_id']))

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
            '200': "GroupSetTaskGetGroupSetTaskListResponseBody",
        }

        return self.api_client.call_api(
            '/v1/groupSet/tasks', 'GET',
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
