# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class BucketLinks(object):
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
        'labels': 'str',
        'members': 'str',
        'org': 'str',
        'owners': 'str',
        '_self': 'str',
        'write': 'str'
    }

    attribute_map = {
        'labels': 'labels',
        'members': 'members',
        'org': 'org',
        'owners': 'owners',
        '_self': 'self',
        'write': 'write'
    }

    def __init__(self, labels=None, members=None, org=None, owners=None, _self=None, write=None):  # noqa: E501,D401,D403
        """BucketLinks - a model defined in OpenAPI."""  # noqa: E501
        self._labels = None
        self._members = None
        self._org = None
        self._owners = None
        self.__self = None
        self._write = None
        self.discriminator = None

        if labels is not None:
            self.labels = labels
        if members is not None:
            self.members = members
        if org is not None:
            self.org = org
        if owners is not None:
            self.owners = owners
        if _self is not None:
            self._self = _self
        if write is not None:
            self.write = write

    @property
    def labels(self):
        """Get the labels of this BucketLinks.

        URI of resource.

        :return: The labels of this BucketLinks.
        :rtype: str
        """  # noqa: E501
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Set the labels of this BucketLinks.

        URI of resource.

        :param labels: The labels of this BucketLinks.
        :type: str
        """  # noqa: E501
        self._labels = labels

    @property
    def members(self):
        """Get the members of this BucketLinks.

        URI of resource.

        :return: The members of this BucketLinks.
        :rtype: str
        """  # noqa: E501
        return self._members

    @members.setter
    def members(self, members):
        """Set the members of this BucketLinks.

        URI of resource.

        :param members: The members of this BucketLinks.
        :type: str
        """  # noqa: E501
        self._members = members

    @property
    def org(self):
        """Get the org of this BucketLinks.

        URI of resource.

        :return: The org of this BucketLinks.
        :rtype: str
        """  # noqa: E501
        return self._org

    @org.setter
    def org(self, org):
        """Set the org of this BucketLinks.

        URI of resource.

        :param org: The org of this BucketLinks.
        :type: str
        """  # noqa: E501
        self._org = org

    @property
    def owners(self):
        """Get the owners of this BucketLinks.

        URI of resource.

        :return: The owners of this BucketLinks.
        :rtype: str
        """  # noqa: E501
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Set the owners of this BucketLinks.

        URI of resource.

        :param owners: The owners of this BucketLinks.
        :type: str
        """  # noqa: E501
        self._owners = owners

    @property
    def _self(self):
        """Get the _self of this BucketLinks.

        URI of resource.

        :return: The _self of this BucketLinks.
        :rtype: str
        """  # noqa: E501
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Set the _self of this BucketLinks.

        URI of resource.

        :param _self: The _self of this BucketLinks.
        :type: str
        """  # noqa: E501
        self.__self = _self

    @property
    def write(self):
        """Get the write of this BucketLinks.

        URI of resource.

        :return: The write of this BucketLinks.
        :rtype: str
        """  # noqa: E501
        return self._write

    @write.setter
    def write(self, write):
        """Set the write of this BucketLinks.

        URI of resource.

        :param write: The write of this BucketLinks.
        :type: str
        """  # noqa: E501
        self._write = write

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
        if not isinstance(other, BucketLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
