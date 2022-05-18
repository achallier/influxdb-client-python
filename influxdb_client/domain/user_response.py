# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class UserResponse(object):
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
        'id': 'str',
        'oauth_id': 'str',
        'name': 'str',
        'status': 'str',
        'links': 'UserResponseLinks'
    }

    attribute_map = {
        'id': 'id',
        'oauth_id': 'oauthID',
        'name': 'name',
        'status': 'status',
        'links': 'links'
    }

    def __init__(self, id=None, oauth_id=None, name=None, status='active', links=None):  # noqa: E501,D401,D403
        """UserResponse - a model defined in OpenAPI."""  # noqa: E501
        self._id = None
        self._oauth_id = None
        self._name = None
        self._status = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if oauth_id is not None:
            self.oauth_id = oauth_id
        self.name = name
        if status is not None:
            self.status = status
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Get the id of this UserResponse.

        :return: The id of this UserResponse.
        :rtype: str
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this UserResponse.

        :param id: The id of this UserResponse.
        :type: str
        """  # noqa: E501
        self._id = id

    @property
    def oauth_id(self):
        """Get the oauth_id of this UserResponse.

        :return: The oauth_id of this UserResponse.
        :rtype: str
        """  # noqa: E501
        return self._oauth_id

    @oauth_id.setter
    def oauth_id(self, oauth_id):
        """Set the oauth_id of this UserResponse.

        :param oauth_id: The oauth_id of this UserResponse.
        :type: str
        """  # noqa: E501
        self._oauth_id = oauth_id

    @property
    def name(self):
        """Get the name of this UserResponse.

        :return: The name of this UserResponse.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this UserResponse.

        :param name: The name of this UserResponse.
        :type: str
        """  # noqa: E501
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        self._name = name

    @property
    def status(self):
        """Get the status of this UserResponse.

        If inactive the user is inactive.

        :return: The status of this UserResponse.
        :rtype: str
        """  # noqa: E501
        return self._status

    @status.setter
    def status(self, status):
        """Set the status of this UserResponse.

        If inactive the user is inactive.

        :param status: The status of this UserResponse.
        :type: str
        """  # noqa: E501
        self._status = status

    @property
    def links(self):
        """Get the links of this UserResponse.

        :return: The links of this UserResponse.
        :rtype: UserResponseLinks
        """  # noqa: E501
        return self._links

    @links.setter
    def links(self, links):
        """Set the links of this UserResponse.

        :param links: The links of this UserResponse.
        :type: UserResponseLinks
        """  # noqa: E501
        self._links = links

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in self.openapi_types.items():
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
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, UserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
