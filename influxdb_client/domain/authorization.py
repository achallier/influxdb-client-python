# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

from influxdb_client.domain.authorization_update_request import AuthorizationUpdateRequest


class Authorization(AuthorizationUpdateRequest):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'org_id': 'str',
        'permissions': 'list[Permission]',
        'id': 'str',
        'token': 'str',
        'user_id': 'str',
        'user': 'str',
        'org': 'str',
        'links': 'object',
        'status': 'str',
        'description': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'org_id': 'orgID',
        'permissions': 'permissions',
        'id': 'id',
        'token': 'token',
        'user_id': 'userID',
        'user': 'user',
        'org': 'org',
        'links': 'links',
        'status': 'status',
        'description': 'description'
    }

    def __init__(self, created_at=None, updated_at=None, org_id=None, permissions=None, id=None, token=None, user_id=None, user=None, org=None, links=None, status='active', description=None):  # noqa: E501,D401,D403
        """Authorization - a model defined in OpenAPI."""  # noqa: E501
        AuthorizationUpdateRequest.__init__(self, status=status, description=description)  # noqa: E501

        self._created_at = None
        self._updated_at = None
        self._org_id = None
        self._permissions = None
        self._id = None
        self._token = None
        self._user_id = None
        self._user = None
        self._org = None
        self._links = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if org_id is not None:
            self.org_id = org_id
        if permissions is not None:
            self.permissions = permissions
        if id is not None:
            self.id = id
        if token is not None:
            self.token = token
        if user_id is not None:
            self.user_id = user_id
        if user is not None:
            self.user = user
        if org is not None:
            self.org = org
        if links is not None:
            self.links = links

    @property
    def created_at(self):
        """Get the created_at of this Authorization.

        :return: The created_at of this Authorization.
        :rtype: datetime
        """  # noqa: E501
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Set the created_at of this Authorization.

        :param created_at: The created_at of this Authorization.
        :type: datetime
        """  # noqa: E501
        self._created_at = created_at

    @property
    def updated_at(self):
        """Get the updated_at of this Authorization.

        :return: The updated_at of this Authorization.
        :rtype: datetime
        """  # noqa: E501
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Set the updated_at of this Authorization.

        :param updated_at: The updated_at of this Authorization.
        :type: datetime
        """  # noqa: E501
        self._updated_at = updated_at

    @property
    def org_id(self):
        """Get the org_id of this Authorization.

        ID of the organization that the authorization is scoped to.

        :return: The org_id of this Authorization.
        :rtype: str
        """  # noqa: E501
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Set the org_id of this Authorization.

        ID of the organization that the authorization is scoped to.

        :param org_id: The org_id of this Authorization.
        :type: str
        """  # noqa: E501
        self._org_id = org_id

    @property
    def permissions(self):
        """Get the permissions of this Authorization.

        List of permissions for an authorization.  An authorization must have at least one permission.

        :return: The permissions of this Authorization.
        :rtype: list[Permission]
        """  # noqa: E501
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Set the permissions of this Authorization.

        List of permissions for an authorization.  An authorization must have at least one permission.

        :param permissions: The permissions of this Authorization.
        :type: list[Permission]
        """  # noqa: E501
        self._permissions = permissions

    @property
    def id(self):
        """Get the id of this Authorization.

        :return: The id of this Authorization.
        :rtype: str
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this Authorization.

        :param id: The id of this Authorization.
        :type: str
        """  # noqa: E501
        self._id = id

    @property
    def token(self):
        """Get the token of this Authorization.

        Token used to authenticate API requests.

        :return: The token of this Authorization.
        :rtype: str
        """  # noqa: E501
        return self._token

    @token.setter
    def token(self, token):
        """Set the token of this Authorization.

        Token used to authenticate API requests.

        :param token: The token of this Authorization.
        :type: str
        """  # noqa: E501
        self._token = token

    @property
    def user_id(self):
        """Get the user_id of this Authorization.

        ID of the user that created and owns the token.

        :return: The user_id of this Authorization.
        :rtype: str
        """  # noqa: E501
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Set the user_id of this Authorization.

        ID of the user that created and owns the token.

        :param user_id: The user_id of this Authorization.
        :type: str
        """  # noqa: E501
        self._user_id = user_id

    @property
    def user(self):
        """Get the user of this Authorization.

        Name of the user that created and owns the token.

        :return: The user of this Authorization.
        :rtype: str
        """  # noqa: E501
        return self._user

    @user.setter
    def user(self, user):
        """Set the user of this Authorization.

        Name of the user that created and owns the token.

        :param user: The user of this Authorization.
        :type: str
        """  # noqa: E501
        self._user = user

    @property
    def org(self):
        """Get the org of this Authorization.

        Name of the organization that the token is scoped to.

        :return: The org of this Authorization.
        :rtype: str
        """  # noqa: E501
        return self._org

    @org.setter
    def org(self, org):
        """Set the org of this Authorization.

        Name of the organization that the token is scoped to.

        :param org: The org of this Authorization.
        :type: str
        """  # noqa: E501
        self._org = org

    @property
    def links(self):
        """Get the links of this Authorization.

        :return: The links of this Authorization.
        :rtype: object
        """  # noqa: E501
        return self._links

    @links.setter
    def links(self, links):
        """Set the links of this Authorization.

        :param links: The links of this Authorization.
        :type: object
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
        if not isinstance(other, Authorization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
