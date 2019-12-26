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


class CampaignWebPushSendRequest(object):
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
        'site_id': 'int',
        'segments': 'OSegmentsWithoutContactActionSend',
        'notify': 'list[int]',
        'schedule_date': 'datetime'
    }

    attribute_map = {
        'site_id': 'site_id',
        'segments': 'segments',
        'notify': 'notify',
        'schedule_date': 'schedule_date'
    }

    def __init__(self, site_id=None, segments=None, notify=None, schedule_date=None, local_vars_configuration=None):  # noqa: E501
        """CampaignWebPushSendRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._site_id = None
        self._segments = None
        self._notify = None
        self._schedule_date = None
        self.discriminator = None

        self.site_id = site_id
        self.segments = segments
        if notify is not None:
            self.notify = notify
        if schedule_date is not None:
            self.schedule_date = schedule_date

    @property
    def site_id(self):
        """Gets the site_id of this CampaignWebPushSendRequest.  # noqa: E501


        :return: The site_id of this CampaignWebPushSendRequest.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this CampaignWebPushSendRequest.


        :param site_id: The site_id of this CampaignWebPushSendRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and site_id is None:  # noqa: E501
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                site_id is not None and site_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `site_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._site_id = site_id

    @property
    def segments(self):
        """Gets the segments of this CampaignWebPushSendRequest.  # noqa: E501


        :return: The segments of this CampaignWebPushSendRequest.  # noqa: E501
        :rtype: OSegmentsWithoutContactActionSend
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this CampaignWebPushSendRequest.


        :param segments: The segments of this CampaignWebPushSendRequest.  # noqa: E501
        :type: OSegmentsWithoutContactActionSend
        """
        if self.local_vars_configuration.client_side_validation and segments is None:  # noqa: E501
            raise ValueError("Invalid value for `segments`, must not be `None`")  # noqa: E501

        self._segments = segments

    @property
    def notify(self):
        """Gets the notify of this CampaignWebPushSendRequest.  # noqa: E501

        Array of IDs of the users to notify  # noqa: E501

        :return: The notify of this CampaignWebPushSendRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this CampaignWebPushSendRequest.

        Array of IDs of the users to notify  # noqa: E501

        :param notify: The notify of this CampaignWebPushSendRequest.  # noqa: E501
        :type: list[int]
        """

        self._notify = notify

    @property
    def schedule_date(self):
        """Gets the schedule_date of this CampaignWebPushSendRequest.  # noqa: E501

        The date and time  # noqa: E501

        :return: The schedule_date of this CampaignWebPushSendRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._schedule_date

    @schedule_date.setter
    def schedule_date(self, schedule_date):
        """Sets the schedule_date of this CampaignWebPushSendRequest.

        The date and time  # noqa: E501

        :param schedule_date: The schedule_date of this CampaignWebPushSendRequest.  # noqa: E501
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
        if not isinstance(other, CampaignWebPushSendRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignWebPushSendRequest):
            return True

        return self.to_dict() != other.to_dict()
