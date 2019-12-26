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


class EmailBouncesListStatsFields(object):
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
        'bounce_date': 'bool',
        'bounce_type': 'bool',
        'bounce_detail': 'bool'
    }

    attribute_map = {
        'bounce_date': 'bounce_date',
        'bounce_type': 'bounce_type',
        'bounce_detail': 'bounce_detail'
    }

    def __init__(self, bounce_date=None, bounce_type=None, bounce_detail=None, local_vars_configuration=None):  # noqa: E501
        """EmailBouncesListStatsFields - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bounce_date = None
        self._bounce_type = None
        self._bounce_detail = None
        self.discriminator = None

        self.bounce_date = bounce_date
        self.bounce_type = bounce_type
        self.bounce_detail = bounce_detail

    @property
    def bounce_date(self):
        """Gets the bounce_date of this EmailBouncesListStatsFields.  # noqa: E501

        True to include bounce date, false otherwise  # noqa: E501

        :return: The bounce_date of this EmailBouncesListStatsFields.  # noqa: E501
        :rtype: bool
        """
        return self._bounce_date

    @bounce_date.setter
    def bounce_date(self, bounce_date):
        """Sets the bounce_date of this EmailBouncesListStatsFields.

        True to include bounce date, false otherwise  # noqa: E501

        :param bounce_date: The bounce_date of this EmailBouncesListStatsFields.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and bounce_date is None:  # noqa: E501
            raise ValueError("Invalid value for `bounce_date`, must not be `None`")  # noqa: E501

        self._bounce_date = bounce_date

    @property
    def bounce_type(self):
        """Gets the bounce_type of this EmailBouncesListStatsFields.  # noqa: E501

        True to include bounce type, false otherwise  # noqa: E501

        :return: The bounce_type of this EmailBouncesListStatsFields.  # noqa: E501
        :rtype: bool
        """
        return self._bounce_type

    @bounce_type.setter
    def bounce_type(self, bounce_type):
        """Sets the bounce_type of this EmailBouncesListStatsFields.

        True to include bounce type, false otherwise  # noqa: E501

        :param bounce_type: The bounce_type of this EmailBouncesListStatsFields.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and bounce_type is None:  # noqa: E501
            raise ValueError("Invalid value for `bounce_type`, must not be `None`")  # noqa: E501

        self._bounce_type = bounce_type

    @property
    def bounce_detail(self):
        """Gets the bounce_detail of this EmailBouncesListStatsFields.  # noqa: E501

        True to include bounce detail, false otherwise  # noqa: E501

        :return: The bounce_detail of this EmailBouncesListStatsFields.  # noqa: E501
        :rtype: bool
        """
        return self._bounce_detail

    @bounce_detail.setter
    def bounce_detail(self, bounce_detail):
        """Sets the bounce_detail of this EmailBouncesListStatsFields.

        True to include bounce detail, false otherwise  # noqa: E501

        :param bounce_detail: The bounce_detail of this EmailBouncesListStatsFields.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and bounce_detail is None:  # noqa: E501
            raise ValueError("Invalid value for `bounce_detail`, must not be `None`")  # noqa: E501

        self._bounce_detail = bounce_detail

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
        if not isinstance(other, EmailBouncesListStatsFields):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailBouncesListStatsFields):
            return True

        return self.to_dict() != other.to_dict()
