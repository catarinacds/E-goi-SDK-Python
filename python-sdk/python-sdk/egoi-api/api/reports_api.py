# coding: utf-8

"""
    APIv3 (Beta)

     # Introduction Just a quick pick!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # HTTP Methods for RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from egoi-api.api_client import ApiClient
from egoi-api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ReportsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_push_report(self, campaign_hash, **kwargs):  # noqa: E501
        """Get push report  # noqa: E501

        Returns a push report given the campaign hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_push_report(campaign_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_hash: ID of the Campaign (required)
        :param bool operating_systems: True to show operating system stats
        :param bool brands: True to show brand stats
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PushReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_push_report_with_http_info(campaign_hash, **kwargs)  # noqa: E501

    def get_push_report_with_http_info(self, campaign_hash, **kwargs):  # noqa: E501
        """Get push report  # noqa: E501

        Returns a push report given the campaign hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_push_report_with_http_info(campaign_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_hash: ID of the Campaign (required)
        :param bool operating_systems: True to show operating system stats
        :param bool brands: True to show brand stats
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PushReport, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['campaign_hash', 'operating_systems', 'brands']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_push_report" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'campaign_hash' is set
        if self.api_client.client_side_validation and ('campaign_hash' not in local_var_params or  # noqa: E501
                                                        local_var_params['campaign_hash'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `campaign_hash` when calling `get_push_report`")  # noqa: E501

        if self.api_client.client_side_validation and 'campaign_hash' in local_var_params and not re.search(r'[a-zA-Z0-9_-]*', local_var_params['campaign_hash']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `campaign_hash` when calling `get_push_report`, must conform to the pattern `/[a-zA-Z0-9_-]*/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'campaign_hash' in local_var_params:
            path_params['campaign_hash'] = local_var_params['campaign_hash']  # noqa: E501

        query_params = []
        if 'operating_systems' in local_var_params and local_var_params['operating_systems'] is not None:  # noqa: E501
            query_params.append(('operating_systems', local_var_params['operating_systems']))  # noqa: E501
        if 'brands' in local_var_params and local_var_params['brands'] is not None:  # noqa: E501
            query_params.append(('brands', local_var_params['brands']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/reports/push/{campaign_hash}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PushReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sms_report(self, campaign_hash, **kwargs):  # noqa: E501
        """Get sms report  # noqa: E501

        Returns sms report given the campaign hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sms_report(campaign_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_hash: ID of the Campaign (required)
        :param bool networks: True to show network stats
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PhoneReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_sms_report_with_http_info(campaign_hash, **kwargs)  # noqa: E501

    def get_sms_report_with_http_info(self, campaign_hash, **kwargs):  # noqa: E501
        """Get sms report  # noqa: E501

        Returns sms report given the campaign hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sms_report_with_http_info(campaign_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_hash: ID of the Campaign (required)
        :param bool networks: True to show network stats
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PhoneReport, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['campaign_hash', 'networks']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sms_report" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'campaign_hash' is set
        if self.api_client.client_side_validation and ('campaign_hash' not in local_var_params or  # noqa: E501
                                                        local_var_params['campaign_hash'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `campaign_hash` when calling `get_sms_report`")  # noqa: E501

        if self.api_client.client_side_validation and 'campaign_hash' in local_var_params and not re.search(r'[a-zA-Z0-9_-]*', local_var_params['campaign_hash']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `campaign_hash` when calling `get_sms_report`, must conform to the pattern `/[a-zA-Z0-9_-]*/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'campaign_hash' in local_var_params:
            path_params['campaign_hash'] = local_var_params['campaign_hash']  # noqa: E501

        query_params = []
        if 'networks' in local_var_params and local_var_params['networks'] is not None:  # noqa: E501
            query_params.append(('networks', local_var_params['networks']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/reports/sms/{campaign_hash}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PhoneReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_voice_report(self, campaign_hash, **kwargs):  # noqa: E501
        """Get voice report  # noqa: E501

        Returns voice report given the campaign hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_voice_report(campaign_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_hash: ID of the Campaign (required)
        :param bool networks: True to show network stats
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PhoneReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_voice_report_with_http_info(campaign_hash, **kwargs)  # noqa: E501

    def get_voice_report_with_http_info(self, campaign_hash, **kwargs):  # noqa: E501
        """Get voice report  # noqa: E501

        Returns voice report given the campaign hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_voice_report_with_http_info(campaign_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_hash: ID of the Campaign (required)
        :param bool networks: True to show network stats
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PhoneReport, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['campaign_hash', 'networks']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_voice_report" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'campaign_hash' is set
        if self.api_client.client_side_validation and ('campaign_hash' not in local_var_params or  # noqa: E501
                                                        local_var_params['campaign_hash'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `campaign_hash` when calling `get_voice_report`")  # noqa: E501

        if self.api_client.client_side_validation and 'campaign_hash' in local_var_params and not re.search(r'[a-zA-Z0-9_-]*', local_var_params['campaign_hash']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `campaign_hash` when calling `get_voice_report`, must conform to the pattern `/[a-zA-Z0-9_-]*/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'campaign_hash' in local_var_params:
            path_params['campaign_hash'] = local_var_params['campaign_hash']  # noqa: E501

        query_params = []
        if 'networks' in local_var_params and local_var_params['networks'] is not None:  # noqa: E501
            query_params.append(('networks', local_var_params['networks']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/reports/voice/{campaign_hash}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PhoneReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_web_push_report(self, campaign_hash, **kwargs):  # noqa: E501
        """Get webpush report  # noqa: E501

        Returns webpush report given the campaign hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_web_push_report(campaign_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_hash: ID of the Campaign (required)
        :param bool devices: True to show device stats
        :param bool operating_systems: True to show operating systems stats
        :param bool browsers: True to show browser stats
        :param bool url: True to show url stats
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WebPushReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_web_push_report_with_http_info(campaign_hash, **kwargs)  # noqa: E501

    def get_web_push_report_with_http_info(self, campaign_hash, **kwargs):  # noqa: E501
        """Get webpush report  # noqa: E501

        Returns webpush report given the campaign hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_web_push_report_with_http_info(campaign_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str campaign_hash: ID of the Campaign (required)
        :param bool devices: True to show device stats
        :param bool operating_systems: True to show operating systems stats
        :param bool browsers: True to show browser stats
        :param bool url: True to show url stats
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WebPushReport, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['campaign_hash', 'devices', 'operating_systems', 'browsers', 'url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_web_push_report" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'campaign_hash' is set
        if self.api_client.client_side_validation and ('campaign_hash' not in local_var_params or  # noqa: E501
                                                        local_var_params['campaign_hash'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `campaign_hash` when calling `get_web_push_report`")  # noqa: E501

        if self.api_client.client_side_validation and 'campaign_hash' in local_var_params and not re.search(r'[a-zA-Z0-9_-]*', local_var_params['campaign_hash']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `campaign_hash` when calling `get_web_push_report`, must conform to the pattern `/[a-zA-Z0-9_-]*/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'campaign_hash' in local_var_params:
            path_params['campaign_hash'] = local_var_params['campaign_hash']  # noqa: E501

        query_params = []
        if 'devices' in local_var_params and local_var_params['devices'] is not None:  # noqa: E501
            query_params.append(('devices', local_var_params['devices']))  # noqa: E501
        if 'operating_systems' in local_var_params and local_var_params['operating_systems'] is not None:  # noqa: E501
            query_params.append(('operating_systems', local_var_params['operating_systems']))  # noqa: E501
        if 'browsers' in local_var_params and local_var_params['browsers'] is not None:  # noqa: E501
            query_params.append(('browsers', local_var_params['browsers']))  # noqa: E501
        if 'url' in local_var_params and local_var_params['url'] is not None:  # noqa: E501
            query_params.append(('url', local_var_params['url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/reports/web-push/{campaign_hash}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebPushReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
