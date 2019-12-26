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


class CampaignEmailSendRequest(object):
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
        'list_id': 'int',
        'segments': 'EmailSendSegment',
        'notify': 'list[int]',
        'destination_field': 'str',
        'unique_contacts_only': 'bool',
        'schedule_date': 'datetime'
    }

    attribute_map = {
        'list_id': 'list_id',
        'segments': 'segments',
        'notify': 'notify',
        'destination_field': 'destination_field',
        'unique_contacts_only': 'unique_contacts_only',
        'schedule_date': 'schedule_date'
    }

    def __init__(self, list_id=None, segments=None, notify=None, destination_field=None, unique_contacts_only=False, schedule_date=None, local_vars_configuration=None):  # noqa: E501
        """CampaignEmailSendRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._list_id = None
        self._segments = None
        self._notify = None
        self._destination_field = None
        self._unique_contacts_only = None
        self._schedule_date = None
        self.discriminator = None

        self.list_id = list_id
        self.segments = segments
        if notify is not None:
            self.notify = notify
        if destination_field is not None:
            self.destination_field = destination_field
        if unique_contacts_only is not None:
            self.unique_contacts_only = unique_contacts_only
        if schedule_date is not None:
            self.schedule_date = schedule_date

    @property
    def list_id(self):
        """Gets the list_id of this CampaignEmailSendRequest.  # noqa: E501


        :return: The list_id of this CampaignEmailSendRequest.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this CampaignEmailSendRequest.


        :param list_id: The list_id of this CampaignEmailSendRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and list_id is None:  # noqa: E501
            raise ValueError("Invalid value for `list_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                list_id is not None and list_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `list_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._list_id = list_id

    @property
    def segments(self):
        """Gets the segments of this CampaignEmailSendRequest.  # noqa: E501


        :return: The segments of this CampaignEmailSendRequest.  # noqa: E501
        :rtype: EmailSendSegment
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this CampaignEmailSendRequest.


        :param segments: The segments of this CampaignEmailSendRequest.  # noqa: E501
        :type: EmailSendSegment
        """
        if self.local_vars_configuration.client_side_validation and segments is None:  # noqa: E501
            raise ValueError("Invalid value for `segments`, must not be `None`")  # noqa: E501

        self._segments = segments

    @property
    def notify(self):
        """Gets the notify of this CampaignEmailSendRequest.  # noqa: E501

        Array of IDs of the users to notify  # noqa: E501

        :return: The notify of this CampaignEmailSendRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this CampaignEmailSendRequest.

        Array of IDs of the users to notify  # noqa: E501

        :param notify: The notify of this CampaignEmailSendRequest.  # noqa: E501
        :type: list[int]
        """

        self._notify = notify

    @property
    def destination_field(self):
        """Gets the destination_field of this CampaignEmailSendRequest.  # noqa: E501

        Destination field of this campaign, which must be an email field (email or extra field id).                         If not sent, defaults to the general email field  # noqa: E501

        :return: The destination_field of this CampaignEmailSendRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_field

    @destination_field.setter
    def destination_field(self, destination_field):
        """Sets the destination_field of this CampaignEmailSendRequest.

        Destination field of this campaign, which must be an email field (email or extra field id).                         If not sent, defaults to the general email field  # noqa: E501

        :param destination_field: The destination_field of this CampaignEmailSendRequest.  # noqa: E501
        :type: str
        """

        self._destination_field = destination_field

    @property
    def unique_contacts_only(self):
        """Gets the unique_contacts_only of this CampaignEmailSendRequest.  # noqa: E501

        True to send the campaign only to unique contacts  # noqa: E501

        :return: The unique_contacts_only of this CampaignEmailSendRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unique_contacts_only

    @unique_contacts_only.setter
    def unique_contacts_only(self, unique_contacts_only):
        """Sets the unique_contacts_only of this CampaignEmailSendRequest.

        True to send the campaign only to unique contacts  # noqa: E501

        :param unique_contacts_only: The unique_contacts_only of this CampaignEmailSendRequest.  # noqa: E501
        :type: bool
        """

        self._unique_contacts_only = unique_contacts_only

    @property
    def schedule_date(self):
        """Gets the schedule_date of this CampaignEmailSendRequest.  # noqa: E501

        The date and time  # noqa: E501

        :return: The schedule_date of this CampaignEmailSendRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._schedule_date

    @schedule_date.setter
    def schedule_date(self, schedule_date):
        """Sets the schedule_date of this CampaignEmailSendRequest.

        The date and time  # noqa: E501

        :param schedule_date: The schedule_date of this CampaignEmailSendRequest.  # noqa: E501
        :type: datetime
        """

        self._schedule_date = schedule_date

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
        if not isinstance(other, CampaignEmailSendRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignEmailSendRequest):
            return True

        return self.to_dict() != other.to_dict()
