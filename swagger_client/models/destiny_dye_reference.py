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


class DestinyDyeReference(object):
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
        'channel_hash': 'int',
        'dye_hash': 'int'
    }

    attribute_map = {
        'channel_hash': 'channelHash',
        'dye_hash': 'dyeHash'
    }

    def __init__(self, channel_hash=None, dye_hash=None):
        """
        DestinyDyeReference - a model defined in Swagger
        """

        self._channel_hash = None
        self._dye_hash = None
        self.discriminator = None

        if channel_hash is not None:
          self.channel_hash = channel_hash
        if dye_hash is not None:
          self.dye_hash = dye_hash

    @property
    def channel_hash(self):
        """
        Gets the channel_hash of this DestinyDyeReference.

        :return: The channel_hash of this DestinyDyeReference.
        :rtype: int
        """
        return self._channel_hash

    @channel_hash.setter
    def channel_hash(self, channel_hash):
        """
        Sets the channel_hash of this DestinyDyeReference.

        :param channel_hash: The channel_hash of this DestinyDyeReference.
        :type: int
        """

        self._channel_hash = channel_hash

    @property
    def dye_hash(self):
        """
        Gets the dye_hash of this DestinyDyeReference.

        :return: The dye_hash of this DestinyDyeReference.
        :rtype: int
        """
        return self._dye_hash

    @dye_hash.setter
    def dye_hash(self, dye_hash):
        """
        Sets the dye_hash of this DestinyDyeReference.

        :param dye_hash: The dye_hash of this DestinyDyeReference.
        :type: int
        """

        self._dye_hash = dye_hash

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
        if not isinstance(other, DestinyDyeReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
