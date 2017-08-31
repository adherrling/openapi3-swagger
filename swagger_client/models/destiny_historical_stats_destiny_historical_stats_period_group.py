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


class DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup(object):
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
        'period': 'datetime',
        'values': 'dict(str, ComponentsschemasDestinyHistoricalStatsDestinyHistoricalStatsValue)'
    }

    attribute_map = {
        'period': 'period',
        'values': 'values'
    }

    def __init__(self, period=None, values=None):
        """
        DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup - a model defined in Swagger
        """

        self._period = None
        self._values = None
        self.discriminator = None

        if period is not None:
          self.period = period
        if values is not None:
          self.values = values

    @property
    def period(self):
        """
        Gets the period of this DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup.
        Period for the group.  If the stat periodType is day, then this will have a specific day. If the type is monthly, thenthis value will be the first day of the applicable month. This value is not set when the periodType is 'all time'.

        :return: The period of this DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup.
        :rtype: datetime
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup.
        Period for the group.  If the stat periodType is day, then this will have a specific day. If the type is monthly, thenthis value will be the first day of the applicable month. This value is not set when the periodType is 'all time'.

        :param period: The period of this DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup.
        :type: datetime
        """

        self._period = period

    @property
    def values(self):
        """
        Gets the values of this DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup.
        Collection of stats for the period.

        :return: The values of this DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup.
        :rtype: dict(str, ComponentsschemasDestinyHistoricalStatsDestinyHistoricalStatsValue)
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup.
        Collection of stats for the period.

        :param values: The values of this DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup.
        :type: dict(str, ComponentsschemasDestinyHistoricalStatsDestinyHistoricalStatsValue)
        """

        self._values = values

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
        if not isinstance(other, DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other