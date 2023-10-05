# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr, conint

from typing import Optional, Union

from lakefs_sdk.models.action_run import ActionRun
from lakefs_sdk.models.action_run_list import ActionRunList
from lakefs_sdk.models.hook_run_list import HookRunList

from lakefs_sdk.api_client import ApiClient
from lakefs_sdk.api_response import ApiResponse
from lakefs_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ActionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_run(self, repository : StrictStr, run_id : StrictStr, **kwargs) -> ActionRun:  # noqa: E501
        """get a run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_run(repository, run_id, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param run_id: (required)
        :type run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ActionRun
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_run_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_run_with_http_info(repository, run_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_run_with_http_info(self, repository : StrictStr, run_id : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """get a run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_run_with_http_info(repository, run_id, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param run_id: (required)
        :type run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
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
        :rtype: tuple(ActionRun, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'repository',
            'run_id'
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
                    " to method get_run" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']

        if _params['run_id']:
            _path_params['run_id'] = _params['run_id']


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
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {
            '200': "ActionRun",
            '401': "Error",
            '404': "Error",
        }

        return self.api_client.call_api(
            '/repositories/{repository}/actions/runs/{run_id}', 'GET',
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
    def get_run_hook_output(self, repository : StrictStr, run_id : StrictStr, hook_run_id : StrictStr, **kwargs) -> bytearray:  # noqa: E501
        """get run hook output  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_run_hook_output(repository, run_id, hook_run_id, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param run_id: (required)
        :type run_id: str
        :param hook_run_id: (required)
        :type hook_run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_run_hook_output_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_run_hook_output_with_http_info(repository, run_id, hook_run_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_run_hook_output_with_http_info(self, repository : StrictStr, run_id : StrictStr, hook_run_id : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """get run hook output  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_run_hook_output_with_http_info(repository, run_id, hook_run_id, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param run_id: (required)
        :type run_id: str
        :param hook_run_id: (required)
        :type hook_run_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
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
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'repository',
            'run_id',
            'hook_run_id'
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
                    " to method get_run_hook_output" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']

        if _params['run_id']:
            _path_params['run_id'] = _params['run_id']

        if _params['hook_run_id']:
            _path_params['hook_run_id'] = _params['hook_run_id']


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
            ['application/octet-stream', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {
            '200': "bytearray",
            '401': "Error",
            '404': "Error",
        }

        return self.api_client.call_api(
            '/repositories/{repository}/actions/runs/{run_id}/hooks/{hook_run_id}/output', 'GET',
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
    def list_repository_runs(self, repository : StrictStr, after : Annotated[Optional[StrictStr], Field(description="return items after this value")] = None, amount : Annotated[Optional[conint(strict=True, le=1000, ge=-1)], Field(description="how many items to return")] = None, branch : Optional[StrictStr] = None, commit : Optional[StrictStr] = None, **kwargs) -> ActionRunList:  # noqa: E501
        """list runs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_repository_runs(repository, after, amount, branch, commit, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param after: return items after this value
        :type after: str
        :param amount: how many items to return
        :type amount: int
        :param branch:
        :type branch: str
        :param commit:
        :type commit: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ActionRunList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_repository_runs_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_repository_runs_with_http_info(repository, after, amount, branch, commit, **kwargs)  # noqa: E501

    @validate_arguments
    def list_repository_runs_with_http_info(self, repository : StrictStr, after : Annotated[Optional[StrictStr], Field(description="return items after this value")] = None, amount : Annotated[Optional[conint(strict=True, le=1000, ge=-1)], Field(description="how many items to return")] = None, branch : Optional[StrictStr] = None, commit : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """list runs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_repository_runs_with_http_info(repository, after, amount, branch, commit, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param after: return items after this value
        :type after: str
        :param amount: how many items to return
        :type amount: int
        :param branch:
        :type branch: str
        :param commit:
        :type commit: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
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
        :rtype: tuple(ActionRunList, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'repository',
            'after',
            'amount',
            'branch',
            'commit'
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
                    " to method list_repository_runs" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']


        # process the query parameters
        _query_params = []
        if _params.get('after') is not None:  # noqa: E501
            _query_params.append(('after', _params['after']))

        if _params.get('amount') is not None:  # noqa: E501
            _query_params.append(('amount', _params['amount']))

        if _params.get('branch') is not None:  # noqa: E501
            _query_params.append(('branch', _params['branch']))

        if _params.get('commit') is not None:  # noqa: E501
            _query_params.append(('commit', _params['commit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {
            '200': "ActionRunList",
            '401': "Error",
            '404': "Error",
        }

        return self.api_client.call_api(
            '/repositories/{repository}/actions/runs', 'GET',
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
    def list_run_hooks(self, repository : StrictStr, run_id : StrictStr, after : Annotated[Optional[StrictStr], Field(description="return items after this value")] = None, amount : Annotated[Optional[conint(strict=True, le=1000, ge=-1)], Field(description="how many items to return")] = None, **kwargs) -> HookRunList:  # noqa: E501
        """list run hooks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_run_hooks(repository, run_id, after, amount, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param run_id: (required)
        :type run_id: str
        :param after: return items after this value
        :type after: str
        :param amount: how many items to return
        :type amount: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: HookRunList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_run_hooks_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_run_hooks_with_http_info(repository, run_id, after, amount, **kwargs)  # noqa: E501

    @validate_arguments
    def list_run_hooks_with_http_info(self, repository : StrictStr, run_id : StrictStr, after : Annotated[Optional[StrictStr], Field(description="return items after this value")] = None, amount : Annotated[Optional[conint(strict=True, le=1000, ge=-1)], Field(description="how many items to return")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """list run hooks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_run_hooks_with_http_info(repository, run_id, after, amount, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param run_id: (required)
        :type run_id: str
        :param after: return items after this value
        :type after: str
        :param amount: how many items to return
        :type amount: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
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
        :rtype: tuple(HookRunList, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'repository',
            'run_id',
            'after',
            'amount'
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
                    " to method list_run_hooks" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']

        if _params['run_id']:
            _path_params['run_id'] = _params['run_id']


        # process the query parameters
        _query_params = []
        if _params.get('after') is not None:  # noqa: E501
            _query_params.append(('after', _params['after']))

        if _params.get('amount') is not None:  # noqa: E501
            _query_params.append(('amount', _params['amount']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {
            '200': "HookRunList",
            '401': "Error",
            '404': "Error",
        }

        return self.api_client.call_api(
            '/repositories/{repository}/actions/runs/{run_id}/hooks', 'GET',
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