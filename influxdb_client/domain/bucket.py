# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class Bucket(object):
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
        'links': 'BucketLinks',
        'id': 'str',
        'type': 'str',
        'name': 'str',
        'description': 'str',
        'org_id': 'str',
        'rp': 'str',
        'schema_type': 'SchemaType',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'retention_rules': 'list[BucketRetentionRules]',
        'labels': 'list[Label]'
    }

    attribute_map = {
        'links': 'links',
        'id': 'id',
        'type': 'type',
        'name': 'name',
        'description': 'description',
        'org_id': 'orgID',
        'rp': 'rp',
        'schema_type': 'schemaType',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'retention_rules': 'retentionRules',
        'labels': 'labels'
    }

    def __init__(self, links=None, id=None, type='user', name=None, description=None, org_id=None, rp=None, schema_type=None, created_at=None, updated_at=None, retention_rules=None, labels=None):  # noqa: E501,D401,D403
        """Bucket - a model defined in OpenAPI."""  # noqa: E501
        self._links = None
        self._id = None
        self._type = None
        self._name = None
        self._description = None
        self._org_id = None
        self._rp = None
        self._schema_type = None
        self._created_at = None
        self._updated_at = None
        self._retention_rules = None
        self._labels = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        self.name = name
        if description is not None:
            self.description = description
        if org_id is not None:
            self.org_id = org_id
        if rp is not None:
            self.rp = rp
        if schema_type is not None:
            self.schema_type = schema_type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.retention_rules = retention_rules
        if labels is not None:
            self.labels = labels

    @property
    def links(self):
        """Get the links of this Bucket.

        :return: The links of this Bucket.
        :rtype: BucketLinks
        """  # noqa: E501
        return self._links

    @links.setter
    def links(self, links):
        """Set the links of this Bucket.

        :param links: The links of this Bucket.
        :type: BucketLinks
        """  # noqa: E501
        self._links = links

    @property
    def id(self):
        """Get the id of this Bucket.

        :return: The id of this Bucket.
        :rtype: str
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this Bucket.

        :param id: The id of this Bucket.
        :type: str
        """  # noqa: E501
        self._id = id

    @property
    def type(self):
        """Get the type of this Bucket.

        :return: The type of this Bucket.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this Bucket.

        :param type: The type of this Bucket.
        :type: str
        """  # noqa: E501
        self._type = type

    @property
    def name(self):
        """Get the name of this Bucket.

        :return: The name of this Bucket.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this Bucket.

        :param name: The name of this Bucket.
        :type: str
        """  # noqa: E501
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        self._name = name

    @property
    def description(self):
        """Get the description of this Bucket.

        :return: The description of this Bucket.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this Bucket.

        :param description: The description of this Bucket.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def org_id(self):
        """Get the org_id of this Bucket.

        :return: The org_id of this Bucket.
        :rtype: str
        """  # noqa: E501
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Set the org_id of this Bucket.

        :param org_id: The org_id of this Bucket.
        :type: str
        """  # noqa: E501
        self._org_id = org_id

    @property
    def rp(self):
        """Get the rp of this Bucket.

        :return: The rp of this Bucket.
        :rtype: str
        """  # noqa: E501
        return self._rp

    @rp.setter
    def rp(self, rp):
        """Set the rp of this Bucket.

        :param rp: The rp of this Bucket.
        :type: str
        """  # noqa: E501
        self._rp = rp

    @property
    def schema_type(self):
        """Get the schema_type of this Bucket.

        :return: The schema_type of this Bucket.
        :rtype: SchemaType
        """  # noqa: E501
        return self._schema_type

    @schema_type.setter
    def schema_type(self, schema_type):
        """Set the schema_type of this Bucket.

        :param schema_type: The schema_type of this Bucket.
        :type: SchemaType
        """  # noqa: E501
        self._schema_type = schema_type

    @property
    def created_at(self):
        """Get the created_at of this Bucket.

        :return: The created_at of this Bucket.
        :rtype: datetime
        """  # noqa: E501
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Set the created_at of this Bucket.

        :param created_at: The created_at of this Bucket.
        :type: datetime
        """  # noqa: E501
        self._created_at = created_at

    @property
    def updated_at(self):
        """Get the updated_at of this Bucket.

        :return: The updated_at of this Bucket.
        :rtype: datetime
        """  # noqa: E501
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Set the updated_at of this Bucket.

        :param updated_at: The updated_at of this Bucket.
        :type: datetime
        """  # noqa: E501
        self._updated_at = updated_at

    @property
    def retention_rules(self):
        """Get the retention_rules of this Bucket.

        Rules to expire or retain data.  No rules means data never expires.

        :return: The retention_rules of this Bucket.
        :rtype: list[BucketRetentionRules]
        """  # noqa: E501
        return self._retention_rules

    @retention_rules.setter
    def retention_rules(self, retention_rules):
        """Set the retention_rules of this Bucket.

        Rules to expire or retain data.  No rules means data never expires.

        :param retention_rules: The retention_rules of this Bucket.
        :type: list[BucketRetentionRules]
        """  # noqa: E501
        if retention_rules is None:
            raise ValueError("Invalid value for `retention_rules`, must not be `None`")  # noqa: E501
        self._retention_rules = retention_rules

    @property
    def labels(self):
        """Get the labels of this Bucket.

        :return: The labels of this Bucket.
        :rtype: list[Label]
        """  # noqa: E501
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Set the labels of this Bucket.

        :param labels: The labels of this Bucket.
        :type: list[Label]
        """  # noqa: E501
        self._labels = labels

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
        if not isinstance(other, Bucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
