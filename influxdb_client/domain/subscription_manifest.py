# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class SubscriptionManifest(object):
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
        'name': 'str',
        'mode': 'str',
        'destinations': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'mode': 'mode',
        'destinations': 'destinations'
    }

    def __init__(self, name=None, mode=None, destinations=None):  # noqa: E501,D401,D403
        """SubscriptionManifest - a model defined in OpenAPI."""  # noqa: E501
        self._name = None
        self._mode = None
        self._destinations = None
        self.discriminator = None

        self.name = name
        self.mode = mode
        self.destinations = destinations

    @property
    def name(self):
        """Get the name of this SubscriptionManifest.

        :return: The name of this SubscriptionManifest.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this SubscriptionManifest.

        :param name: The name of this SubscriptionManifest.
        :type: str
        """  # noqa: E501
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        self._name = name

    @property
    def mode(self):
        """Get the mode of this SubscriptionManifest.

        :return: The mode of this SubscriptionManifest.
        :rtype: str
        """  # noqa: E501
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Set the mode of this SubscriptionManifest.

        :param mode: The mode of this SubscriptionManifest.
        :type: str
        """  # noqa: E501
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        self._mode = mode

    @property
    def destinations(self):
        """Get the destinations of this SubscriptionManifest.

        :return: The destinations of this SubscriptionManifest.
        :rtype: list[str]
        """  # noqa: E501
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Set the destinations of this SubscriptionManifest.

        :param destinations: The destinations of this SubscriptionManifest.
        :type: list[str]
        """  # noqa: E501
        if destinations is None:
            raise ValueError("Invalid value for `destinations`, must not be `None`")  # noqa: E501
        self._destinations = destinations

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
        if not isinstance(other, SubscriptionManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
