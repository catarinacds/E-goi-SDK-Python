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


class ContactExtraFieldDate(object):
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
        'field_id': 'int',
        'format': 'str',
        'value': 'date'
    }

    attribute_map = {
        'field_id': 'field_id',
        'format': 'format',
        'value': 'value'
    }

    def __init__(self, field_id=None, format=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ContactExtraFieldDate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field_id = None
        self._format = None
        self._value = None
        self.discriminator = None

        if field_id is not None:
            self.field_id = field_id
        if format is not None:
            self.format = format
        if value is not None:
            self.value = value

    @property
    def field_id(self):
        """Gets the field_id of this ContactExtraFieldDate.  # noqa: E501


        :return: The field_id of this ContactExtraFieldDate.  # noqa: E501
        :rtype: int
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this ContactExtraFieldDate.


        :param field_id: The field_id of this ContactExtraFieldDate.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                field_id is not None and field_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `field_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._field_id = field_id

    @property
    def format(self):
        """Gets the format of this ContactExtraFieldDate.  # noqa: E501

        Extra field format  # noqa: E501

        :return: The format of this ContactExtraFieldDate.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ContactExtraFieldDate.

        Extra field format  # noqa: E501

        :param format: The format of this ContactExtraFieldDate.  # noqa: E501
        :type: str
        """
        allowed_values = ["date"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def value(self):
        """Gets the value of this ContactExtraFieldDate.  # noqa: E501

        Extra field value  # noqa: E501

        :return: The value of this ContactExtraFieldDate.  # noqa: E501
        :rtype: date
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ContactExtraFieldDate.

        Extra field value  # noqa: E501

        :param value: The value of this ContactExtraFieldDate.  # noqa: E501
        :type: date
        """

        self._value = value

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
        if not isinstance(other, ContactExtraFieldDate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactExtraFieldDate):
            return True

        return self.to_dict() != other.to_dict()
