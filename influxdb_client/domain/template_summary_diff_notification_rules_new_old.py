# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class TemplateSummaryDiffNotificationRulesNewOld(object):
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
        'endpoint_name': 'str',
        'endpoint_id': 'str',
        'endpoint_type': 'str',
        'every': 'str',
        'offset': 'str',
        'message_template': 'str',
        'status': 'str',
        'status_rules': 'list[TemplateSummarySummaryStatusRules]',
        'tag_rules': 'list[TemplateSummarySummaryTagRules]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'endpoint_name': 'endpointName',
        'endpoint_id': 'endpointID',
        'endpoint_type': 'endpointType',
        'every': 'every',
        'offset': 'offset',
        'message_template': 'messageTemplate',
        'status': 'status',
        'status_rules': 'statusRules',
        'tag_rules': 'tagRules'
    }

    def __init__(self, name=None, description=None, endpoint_name=None, endpoint_id=None, endpoint_type=None, every=None, offset=None, message_template=None, status=None, status_rules=None, tag_rules=None):  # noqa: E501,D401,D403
        """TemplateSummaryDiffNotificationRulesNewOld - a model defined in OpenAPI."""  # noqa: E501
        self._name = None
        self._description = None
        self._endpoint_name = None
        self._endpoint_id = None
        self._endpoint_type = None
        self._every = None
        self._offset = None
        self._message_template = None
        self._status = None
        self._status_rules = None
        self._tag_rules = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if endpoint_type is not None:
            self.endpoint_type = endpoint_type
        if every is not None:
            self.every = every
        if offset is not None:
            self.offset = offset
        if message_template is not None:
            self.message_template = message_template
        if status is not None:
            self.status = status
        if status_rules is not None:
            self.status_rules = status_rules
        if tag_rules is not None:
            self.tag_rules = tag_rules

    @property
    def name(self):
        """Get the name of this TemplateSummaryDiffNotificationRulesNewOld.

        :return: The name of this TemplateSummaryDiffNotificationRulesNewOld.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this TemplateSummaryDiffNotificationRulesNewOld.

        :param name: The name of this TemplateSummaryDiffNotificationRulesNewOld.
        :type: str
        """  # noqa: E501
        self._name = name

    @property
    def description(self):
        """Get the description of this TemplateSummaryDiffNotificationRulesNewOld.

        :return: The description of this TemplateSummaryDiffNotificationRulesNewOld.
        :rtype: str
        """  # noqa: E501
        return self._description

    @description.setter
    def description(self, description):
        """Set the description of this TemplateSummaryDiffNotificationRulesNewOld.

        :param description: The description of this TemplateSummaryDiffNotificationRulesNewOld.
        :type: str
        """  # noqa: E501
        self._description = description

    @property
    def endpoint_name(self):
        """Get the endpoint_name of this TemplateSummaryDiffNotificationRulesNewOld.

        :return: The endpoint_name of this TemplateSummaryDiffNotificationRulesNewOld.
        :rtype: str
        """  # noqa: E501
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """Set the endpoint_name of this TemplateSummaryDiffNotificationRulesNewOld.

        :param endpoint_name: The endpoint_name of this TemplateSummaryDiffNotificationRulesNewOld.
        :type: str
        """  # noqa: E501
        self._endpoint_name = endpoint_name

    @property
    def endpoint_id(self):
        """Get the endpoint_id of this TemplateSummaryDiffNotificationRulesNewOld.

        :return: The endpoint_id of this TemplateSummaryDiffNotificationRulesNewOld.
        :rtype: str
        """  # noqa: E501
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Set the endpoint_id of this TemplateSummaryDiffNotificationRulesNewOld.

        :param endpoint_id: The endpoint_id of this TemplateSummaryDiffNotificationRulesNewOld.
        :type: str
        """  # noqa: E501
        self._endpoint_id = endpoint_id

    @property
    def endpoint_type(self):
        """Get the endpoint_type of this TemplateSummaryDiffNotificationRulesNewOld.

        :return: The endpoint_type of this TemplateSummaryDiffNotificationRulesNewOld.
        :rtype: str
        """  # noqa: E501
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """Set the endpoint_type of this TemplateSummaryDiffNotificationRulesNewOld.

        :param endpoint_type: The endpoint_type of this TemplateSummaryDiffNotificationRulesNewOld.
        :type: str
        """  # noqa: E501
        self._endpoint_type = endpoint_type

    @property
    def every(self):
        """Get the every of this TemplateSummaryDiffNotificationRulesNewOld.

        :return: The every of this TemplateSummaryDiffNotificationRulesNewOld.
        :rtype: str
        """  # noqa: E501
        return self._every

    @every.setter
    def every(self, every):
        """Set the every of this TemplateSummaryDiffNotificationRulesNewOld.

        :param every: The every of this TemplateSummaryDiffNotificationRulesNewOld.
        :type: str
        """  # noqa: E501
        self._every = every

    @property
    def offset(self):
        """Get the offset of this TemplateSummaryDiffNotificationRulesNewOld.

        :return: The offset of this TemplateSummaryDiffNotificationRulesNewOld.
        :rtype: str
        """  # noqa: E501
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Set the offset of this TemplateSummaryDiffNotificationRulesNewOld.

        :param offset: The offset of this TemplateSummaryDiffNotificationRulesNewOld.
        :type: str
        """  # noqa: E501
        self._offset = offset

    @property
    def message_template(self):
        """Get the message_template of this TemplateSummaryDiffNotificationRulesNewOld.

        :return: The message_template of this TemplateSummaryDiffNotificationRulesNewOld.
        :rtype: str
        """  # noqa: E501
        return self._message_template

    @message_template.setter
    def message_template(self, message_template):
        """Set the message_template of this TemplateSummaryDiffNotificationRulesNewOld.

        :param message_template: The message_template of this TemplateSummaryDiffNotificationRulesNewOld.
        :type: str
        """  # noqa: E501
        self._message_template = message_template

    @property
    def status(self):
        """Get the status of this TemplateSummaryDiffNotificationRulesNewOld.

        :return: The status of this TemplateSummaryDiffNotificationRulesNewOld.
        :rtype: str
        """  # noqa: E501
        return self._status

    @status.setter
    def status(self, status):
        """Set the status of this TemplateSummaryDiffNotificationRulesNewOld.

        :param status: The status of this TemplateSummaryDiffNotificationRulesNewOld.
        :type: str
        """  # noqa: E501
        self._status = status

    @property
    def status_rules(self):
        """Get the status_rules of this TemplateSummaryDiffNotificationRulesNewOld.

        :return: The status_rules of this TemplateSummaryDiffNotificationRulesNewOld.
        :rtype: list[TemplateSummarySummaryStatusRules]
        """  # noqa: E501
        return self._status_rules

    @status_rules.setter
    def status_rules(self, status_rules):
        """Set the status_rules of this TemplateSummaryDiffNotificationRulesNewOld.

        :param status_rules: The status_rules of this TemplateSummaryDiffNotificationRulesNewOld.
        :type: list[TemplateSummarySummaryStatusRules]
        """  # noqa: E501
        self._status_rules = status_rules

    @property
    def tag_rules(self):
        """Get the tag_rules of this TemplateSummaryDiffNotificationRulesNewOld.

        :return: The tag_rules of this TemplateSummaryDiffNotificationRulesNewOld.
        :rtype: list[TemplateSummarySummaryTagRules]
        """  # noqa: E501
        return self._tag_rules

    @tag_rules.setter
    def tag_rules(self, tag_rules):
        """Set the tag_rules of this TemplateSummaryDiffNotificationRulesNewOld.

        :param tag_rules: The tag_rules of this TemplateSummaryDiffNotificationRulesNewOld.
        :type: list[TemplateSummarySummaryTagRules]
        """  # noqa: E501
        self._tag_rules = tag_rules

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
        if not isinstance(other, TemplateSummaryDiffNotificationRulesNewOld):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
