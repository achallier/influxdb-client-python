# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class TemplateSummaryDiffBucketsNewOld(object):
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
        'description': 'str',
        'retention_rules': 'list[BucketRetentionRules]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'retention_rules': 'retentionRules'
    }

    def __init__(self, name=None, description=None, retention_rules=None):  # noqa: E501,D401,D403
        """TemplateSummaryDiffBucketsNewOld - a model defined in OpenAPI."""  # noqa: E501
        self._name = None
        self._description = None
        self._retention_rules = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if retention_rules is not None:
            self.retention_rules = retention_rules

    @property
    def name(self):
        """Get the name of this TemplateSummaryDiffBucketsNewOld.

        :return: The name of this TemplateSummaryDiffBucketsNewOld.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this TemplateSummaryDiffBucketsNewOld.

        :param name: The name of this TemplateSummaryDiffBucketsNewOld.
        :type: str
        """  # noqa: E501
        self._name = name

    @property
    def description(self):
        """Get the description of this TemplateSummaryDiffBucketsNewOld.

        :return: The description of this TemplateSummaryDiffBucketsNewOld.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this TemplateSummaryDiffBucketsNewOld.

        :param description: The description of this TemplateSummaryDiffBucketsNewOld.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def retention_rules(self):
        """Get the retention_rules of this TemplateSummaryDiffBucketsNewOld.

        Rules to expire or retain data.  No rules means data never expires.

        :return: The retention_rules of this TemplateSummaryDiffBucketsNewOld.
        :rtype: list[BucketRetentionRules]
        """  # noqa: E501
        return self._retention_rules

    @retention_rules.setter
    def retention_rules(self, retention_rules):
        """Set the retention_rules of this TemplateSummaryDiffBucketsNewOld.

        Rules to expire or retain data.  No rules means data never expires.

        :param retention_rules: The retention_rules of this TemplateSummaryDiffBucketsNewOld.
        :type: list[BucketRetentionRules]
        """  # noqa: E501
        self._retention_rules = retention_rules

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
        if not isinstance(other, TemplateSummaryDiffBucketsNewOld):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
