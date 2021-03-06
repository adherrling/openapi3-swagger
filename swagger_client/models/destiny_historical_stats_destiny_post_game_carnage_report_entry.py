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


class DestinyHistoricalStatsDestinyPostGameCarnageReportEntry(object):
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
        'standing': 'int',
        'character_id': 'int',
        'values': 'dict(str, ComponentsschemasDestinyHistoricalStatsDestinyHistoricalStatsValue)'
    }

    attribute_map = {
        'standing': 'standing',
        'character_id': 'characterId',
        'values': 'values'
    }

    def __init__(self, standing=None, character_id=None, values=None):
        """
        DestinyHistoricalStatsDestinyPostGameCarnageReportEntry - a model defined in Swagger
        """

        self._standing = None
        self._character_id = None
        self._values = None
        self.discriminator = None

        if standing is not None:
          self.standing = standing
        if character_id is not None:
          self.character_id = character_id
        if values is not None:
          self.values = values

    @property
    def standing(self):
        """
        Gets the standing of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
        Standing of the player

        :return: The standing of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
        :rtype: int
        """
        return self._standing

    @standing.setter
    def standing(self, standing):
        """
        Sets the standing of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
        Standing of the player

        :param standing: The standing of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
        :type: int
        """

        self._standing = standing

    @property
    def character_id(self):
        """
        Gets the character_id of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
        ID of the player's character used in the activity.

        :return: The character_id of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """
        Sets the character_id of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
        ID of the player's character used in the activity.

        :param character_id: The character_id of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
        :type: int
        """

        self._character_id = character_id

    @property
    def values(self):
        """
        Gets the values of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
        Collection of stats for the player in this activity.

        :return: The values of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
        :rtype: dict(str, ComponentsschemasDestinyHistoricalStatsDestinyHistoricalStatsValue)
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
        Collection of stats for the player in this activity.

        :param values: The values of this DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.
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
        if not isinstance(other, DestinyHistoricalStatsDestinyPostGameCarnageReportEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
