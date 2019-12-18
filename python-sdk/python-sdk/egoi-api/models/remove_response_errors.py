# coding: utf-8

"""
    APIv3 (Beta)

     # Introduction Just a quick pick!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # HTTP Methods for RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from egoi-api.configuration import Configuration


class RemoveResponseErrors(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'invalid_unsubscription_reason': 'list[str]',
        'invalid_unsubscription_method': 'list[str]',
        'invalid_data_type': 'list[str]',
        'contact_not_in_list': 'list[str]',
        'contact_already_removed': 'list[str]'
    }

    attribute_map = {
        'invalid_unsubscription_reason': 'invalid_unsubscription_reason',
        'invalid_unsubscription_method': 'invalid_unsubscription_method',
        'invalid_data_type': 'invalid_data_type',
        'contact_not_in_list': 'contact_not_in_list',
        'contact_already_removed': 'contact_already_removed'
    }

    def __init__(self, invalid_unsubscription_reason=None, invalid_unsubscription_method=None, invalid_data_type=None, contact_not_in_list=None, contact_already_removed=None, local_vars_configuration=None):  # noqa: E501
        """RemoveResponseErrors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._invalid_unsubscription_reason = None
        self._invalid_unsubscription_method = None
        self._invalid_data_type = None
        self._contact_not_in_list = None
        self._contact_already_removed = None
        self.discriminator = None

        if invalid_unsubscription_reason is not None:
            self.invalid_unsubscription_reason = invalid_unsubscription_reason
        if invalid_unsubscription_method is not None:
            self.invalid_unsubscription_method = invalid_unsubscription_method
        if invalid_data_type is not None:
            self.invalid_data_type = invalid_data_type
        if contact_not_in_list is not None:
            self.contact_not_in_list = contact_not_in_list
        if contact_already_removed is not None:
            self.contact_already_removed = contact_already_removed

    @property
    def invalid_unsubscription_reason(self):
        """Gets the invalid_unsubscription_reason of this RemoveResponseErrors.  # noqa: E501


        :return: The invalid_unsubscription_reason of this RemoveResponseErrors.  # noqa: E501
        :rtype: list[str]
        """
        return self._invalid_unsubscription_reason

    @invalid_unsubscription_reason.setter
    def invalid_unsubscription_reason(self, invalid_unsubscription_reason):
        """Sets the invalid_unsubscription_reason of this RemoveResponseErrors.


        :param invalid_unsubscription_reason: The invalid_unsubscription_reason of this RemoveResponseErrors.  # noqa: E501
        :type: list[str]
        """

        self._invalid_unsubscription_reason = invalid_unsubscription_reason

    @property
    def invalid_unsubscription_method(self):
        """Gets the invalid_unsubscription_method of this RemoveResponseErrors.  # noqa: E501


        :return: The invalid_unsubscription_method of this RemoveResponseErrors.  # noqa: E501
        :rtype: list[str]
        """
        return self._invalid_unsubscription_method

    @invalid_unsubscription_method.setter
    def invalid_unsubscription_method(self, invalid_unsubscription_method):
        """Sets the invalid_unsubscription_method of this RemoveResponseErrors.


        :param invalid_unsubscription_method: The invalid_unsubscription_method of this RemoveResponseErrors.  # noqa: E501
        :type: list[str]
        """

        self._invalid_unsubscription_method = invalid_unsubscription_method

    @property
    def invalid_data_type(self):
        """Gets the invalid_data_type of this RemoveResponseErrors.  # noqa: E501


        :return: The invalid_data_type of this RemoveResponseErrors.  # noqa: E501
        :rtype: list[str]
        """
        return self._invalid_data_type

    @invalid_data_type.setter
    def invalid_data_type(self, invalid_data_type):
        """Sets the invalid_data_type of this RemoveResponseErrors.


        :param invalid_data_type: The invalid_data_type of this RemoveResponseErrors.  # noqa: E501
        :type: list[str]
        """

        self._invalid_data_type = invalid_data_type

    @property
    def contact_not_in_list(self):
        """Gets the contact_not_in_list of this RemoveResponseErrors.  # noqa: E501


        :return: The contact_not_in_list of this RemoveResponseErrors.  # noqa: E501
        :rtype: list[str]
        """
        return self._contact_not_in_list

    @contact_not_in_list.setter
    def contact_not_in_list(self, contact_not_in_list):
        """Sets the contact_not_in_list of this RemoveResponseErrors.


        :param contact_not_in_list: The contact_not_in_list of this RemoveResponseErrors.  # noqa: E501
        :type: list[str]
        """

        self._contact_not_in_list = contact_not_in_list

    @property
    def contact_already_removed(self):
        """Gets the contact_already_removed of this RemoveResponseErrors.  # noqa: E501


        :return: The contact_already_removed of this RemoveResponseErrors.  # noqa: E501
        :rtype: list[str]
        """
        return self._contact_already_removed

    @contact_already_removed.setter
    def contact_already_removed(self, contact_already_removed):
        """Sets the contact_already_removed of this RemoveResponseErrors.


        :param contact_already_removed: The contact_already_removed of this RemoveResponseErrors.  # noqa: E501
        :type: list[str]
        """

        self._contact_already_removed = contact_already_removed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RemoveResponseErrors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoveResponseErrors):
            return True

        return self.to_dict() != other.to_dict()
