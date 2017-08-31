# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.

    OpenAPI spec version: 2.0.0
    Contact: support@bungie.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DestinyRequestsActionsDestinyActionRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'membership_type': 'ComponentsschemasBungieMembershipType'
    }

    attribute_map = {
        'membership_type': 'membershipType'
    }

    def __init__(self, membership_type=None):
        """
        DestinyRequestsActionsDestinyActionRequest - a model defined in Swagger
        """

        self._membership_type = None
        self.discriminator = None

        if membership_type is not None:
          self.membership_type = membership_type

    @property
    def membership_type(self):
        """
        Gets the membership_type of this DestinyRequestsActionsDestinyActionRequest.

        :return: The membership_type of this DestinyRequestsActionsDestinyActionRequest.
        :rtype: ComponentsschemasBungieMembershipType
        """
        return self._membership_type

    @membership_type.setter
    def membership_type(self, membership_type):
        """
        Sets the membership_type of this DestinyRequestsActionsDestinyActionRequest.

        :param membership_type: The membership_type of this DestinyRequestsActionsDestinyActionRequest.
        :type: ComponentsschemasBungieMembershipType
        """

        self._membership_type = membership_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DestinyRequestsActionsDestinyActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other