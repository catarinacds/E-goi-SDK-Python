# coding: utf-8

"""
    APIv3 (Beta)

     # Introduction Just a quick pick!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # HTTP Methods for RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import egoi-api
from egoi-api.api.sms_api import SmsApi  # noqa: E501
from egoi-api.rest import ApiException


class TestSmsApi(unittest.TestCase):
    """SmsApi unit test stubs"""

    def setUp(self):
        self.api = egoi-api.api.sms_api.SmsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_action_send_sms(self):
        """Test case for action_send_sms

        Send sms message  # noqa: E501
        """
        pass

    def test_create_sms_campaign(self):
        """Test case for create_sms_campaign

        Create new sms campaign  # noqa: E501
        """
        pass

    def test_patch_sms_campaign(self):
        """Test case for patch_sms_campaign

        Update a specific sms campaign  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
