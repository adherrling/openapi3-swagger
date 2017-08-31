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


class UserAckState(object):
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
        'needs_ack': 'bool',
        'ack_id': 'str'
    }

    attribute_map = {
        'needs_ack': 'needsAck',
        'ack_id': 'ackId'
    }

    def __init__(self, needs_ack=None, ack_id=None):
        """
        UserAckState - a model defined in Swagger
        """

        self._needs_ack = None
        self._ack_id = None
        self.discriminator = None

        if needs_ack is not None:
          self.needs_ack = needs_ack
        if ack_id is not None:
          self.ack_id = ack_id

    @property
    def needs_ack(self):
        """
        Gets the needs_ack of this UserAckState.
        Indicates the related item has not been acknowledged.

        :return: The needs_ack of this UserAckState.
        :rtype: bool
        """
        return self._needs_ack

    @needs_ack.setter
    def needs_ack(self, needs_ack):
        """
        Sets the needs_ack of this UserAckState.
        Indicates the related item has not been acknowledged.

        :param needs_ack: The needs_ack of this UserAckState.
        :type: bool
        """

        self._needs_ack = needs_ack

    @property
    def ack_id(self):
        """
        Gets the ack_id of this UserAckState.
        Identifier to use when acknowledging the related item.[category]:[entityId]:[targetId]

        :return: The ack_id of this UserAckState.
        :rtype: str
        """
        return self._ack_id

    @ack_id.setter
    def ack_id(self, ack_id):
        """
        Sets the ack_id of this UserAckState.
        Identifier to use when acknowledging the related item.[category]:[entityId]:[targetId]

        :param ack_id: The ack_id of this UserAckState.
        :type: str
        """

        self._ack_id = ack_id

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
        if not isinstance(other, UserAckState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
