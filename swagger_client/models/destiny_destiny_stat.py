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


class DestinyDestinyStat(object):
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
        'stat_hash': 'int',
        'value': 'int',
        'maximum_value': 'int'
    }

    attribute_map = {
        'stat_hash': 'statHash',
        'value': 'value',
        'maximum_value': 'maximumValue'
    }

    def __init__(self, stat_hash=None, value=None, maximum_value=None):
        """
        DestinyDestinyStat - a model defined in Swagger
        """

        self._stat_hash = None
        self._value = None
        self._maximum_value = None
        self.discriminator = None

        if stat_hash is not None:
          self.stat_hash = stat_hash
        if value is not None:
          self.value = value
        if maximum_value is not None:
          self.maximum_value = maximum_value

    @property
    def stat_hash(self):
        """
        Gets the stat_hash of this DestinyDestinyStat.
        The hash identifier for the Stat.  Use it to look up the DestinyStatDefinition for static data about the stat.

        :return: The stat_hash of this DestinyDestinyStat.
        :rtype: int
        """
        return self._stat_hash

    @stat_hash.setter
    def stat_hash(self, stat_hash):
        """
        Sets the stat_hash of this DestinyDestinyStat.
        The hash identifier for the Stat.  Use it to look up the DestinyStatDefinition for static data about the stat.

        :param stat_hash: The stat_hash of this DestinyDestinyStat.
        :type: int
        """

        self._stat_hash = stat_hash

    @property
    def value(self):
        """
        Gets the value of this DestinyDestinyStat.
        The current value of the Stat.

        :return: The value of this DestinyDestinyStat.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DestinyDestinyStat.
        The current value of the Stat.

        :param value: The value of this DestinyDestinyStat.
        :type: int
        """

        self._value = value

    @property
    def maximum_value(self):
        """
        Gets the maximum_value of this DestinyDestinyStat.
        The highest possible value for the stat, if we were able to compute it.  (I wouldn't necessarily trust thisvalue right now.  I would like to improve its calculation in later iterations of the API.  Consider thisa placeholder for desired future functionality)

        :return: The maximum_value of this DestinyDestinyStat.
        :rtype: int
        """
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, maximum_value):
        """
        Sets the maximum_value of this DestinyDestinyStat.
        The highest possible value for the stat, if we were able to compute it.  (I wouldn't necessarily trust thisvalue right now.  I would like to improve its calculation in later iterations of the API.  Consider thisa placeholder for desired future functionality)

        :param maximum_value: The maximum_value of this DestinyDestinyStat.
        :type: int
        """

        self._maximum_value = maximum_value

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
        if not isinstance(other, DestinyDestinyStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
