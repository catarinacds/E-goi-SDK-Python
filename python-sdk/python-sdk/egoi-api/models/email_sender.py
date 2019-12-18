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


class EmailSender(object):
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
        'sender_id': 'int',
        'status': 'str',
        'name': 'str',
        'email': 'str'
    }

    attribute_map = {
        'sender_id': 'sender_id',
        'status': 'status',
        'name': 'name',
        'email': 'email'
    }

    def __init__(self, sender_id=None, status=None, name=None, email=None, local_vars_configuration=None):  # noqa: E501
        """EmailSender - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sender_id = None
        self._status = None
        self._name = None
        self._email = None
        self.discriminator = None

        self.sender_id = sender_id
        if status is not None:
            self.status = status
        self.name = name
        self.email = email

    @property
    def sender_id(self):
        """Gets the sender_id of this EmailSender.  # noqa: E501


        :return: The sender_id of this EmailSender.  # noqa: E501
        :rtype: int
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this EmailSender.


        :param sender_id: The sender_id of this EmailSender.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sender_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sender_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sender_id is not None and sender_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `sender_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._sender_id = sender_id

    @property
    def status(self):
        """Gets the status of this EmailSender.  # noqa: E501

        Status of the sender  # noqa: E501

        :return: The status of this EmailSender.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EmailSender.

        Status of the sender  # noqa: E501

        :param status: The status of this EmailSender.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "moderation", "rejected"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def name(self):
        """Gets the name of this EmailSender.  # noqa: E501

        Sender name  # noqa: E501

        :return: The name of this EmailSender.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailSender.

        Sender name  # noqa: E501

        :param name: The name of this EmailSender.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this EmailSender.  # noqa: E501

        Sender email  # noqa: E501

        :return: The email of this EmailSender.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EmailSender.

        Sender email  # noqa: E501

        :param email: The email of this EmailSender.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

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
        if not isinstance(other, EmailSender):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailSender):
            return True

        return self.to_dict() != other.to_dict()
