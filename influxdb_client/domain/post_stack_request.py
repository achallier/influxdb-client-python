# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class PostStackRequest(object):
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
        'org_id': 'str',
        'name': 'str',
        'description': 'str',
        'urls': 'list[str]'
    }

    attribute_map = {
        'org_id': 'orgID',
        'name': 'name',
        'description': 'description',
        'urls': 'urls'
    }

    def __init__(self, org_id=None, name=None, description=None, urls=None):  # noqa: E501,D401,D403
        """PostStackRequest - a model defined in OpenAPI."""  # noqa: E501
        self._org_id = None
        self._name = None
        self._description = None
        self._urls = None
        self.discriminator = None

        if org_id is not None:
            self.org_id = org_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if urls is not None:
            self.urls = urls

    @property
    def org_id(self):
        """Get the org_id of this PostStackRequest.

        :return: The org_id of this PostStackRequest.
        :rtype: str
        """  # noqa: E501
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Set the org_id of this PostStackRequest.

        :param org_id: The org_id of this PostStackRequest.
        :type: str
        """  # noqa: E501
        self._org_id = org_id

    @property
    def name(self):
        """Get the name of this PostStackRequest.

        :return: The name of this PostStackRequest.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this PostStackRequest.

        :param name: The name of this PostStackRequest.
        :type: str
        """  # noqa: E501
        self._name = name

    @property
    def description(self):
        """Get the description of this PostStackRequest.

        :return: The description of this PostStackRequest.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this PostStackRequest.

        :param description: The description of this PostStackRequest.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def urls(self):
        """Get the urls of this PostStackRequest.

        :return: The urls of this PostStackRequest.
        :rtype: list[str]
        """  # noqa: E501
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Set the urls of this PostStackRequest.

        :param urls: The urls of this PostStackRequest.
        :type: list[str]
        """  # noqa: E501
        self._urls = urls

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
        if not isinstance(other, PostStackRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
