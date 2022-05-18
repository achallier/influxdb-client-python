# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class PackageClause(object):
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
        'type': 'str',
        'name': 'Identifier'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name'
    }

    def __init__(self, type=None, name=None):  # noqa: E501,D401,D403
        """PackageClause - a model defined in OpenAPI."""  # noqa: E501
        self._type = None
        self._name = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name

    @property
    def type(self):
        """Get the type of this PackageClause.

        Type of AST node

        :return: The type of this PackageClause.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this PackageClause.

        Type of AST node

        :param type: The type of this PackageClause.
        :type: str
        """  # noqa: E501
        self._type = type

    @property
    def name(self):
        """Get the name of this PackageClause.

        :return: The name of this PackageClause.
        :rtype: Identifier
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this PackageClause.

        :param name: The name of this PackageClause.
        :type: Identifier
        """  # noqa: E501
        self._name = name

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
        if not isinstance(other, PackageClause):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
