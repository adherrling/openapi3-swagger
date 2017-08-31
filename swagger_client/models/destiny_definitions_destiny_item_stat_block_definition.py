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


class DestinyDefinitionsDestinyItemStatBlockDefinition(object):
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
        'stat_group_hash': 'int',
        'stats': 'dict(str, ComponentsschemasDestinyDefinitionsDestinyInventoryItemStatDefinition)',
        'has_displayable_stats': 'bool',
        'primary_base_stat_hash': 'int'
    }

    attribute_map = {
        'stat_group_hash': 'statGroupHash',
        'stats': 'stats',
        'has_displayable_stats': 'hasDisplayableStats',
        'primary_base_stat_hash': 'primaryBaseStatHash'
    }

    def __init__(self, stat_group_hash=None, stats=None, has_displayable_stats=None, primary_base_stat_hash=None):
        """
        DestinyDefinitionsDestinyItemStatBlockDefinition - a model defined in Swagger
        """

        self._stat_group_hash = None
        self._stats = None
        self._has_displayable_stats = None
        self._primary_base_stat_hash = None
        self.discriminator = None

        if stat_group_hash is not None:
          self.stat_group_hash = stat_group_hash
        if stats is not None:
          self.stats = stats
        if has_displayable_stats is not None:
          self.has_displayable_stats = has_displayable_stats
        if primary_base_stat_hash is not None:
          self.primary_base_stat_hash = primary_base_stat_hash

    @property
    def stat_group_hash(self):
        """
        Gets the stat_group_hash of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        If the item's stats are meant to be modified by a DestinyStatGroupDefinition, this willbe the identifier for that definition.  If you are using live data or precomputed stats data on the DestinyInventoryItemDefinition.stats.statsproperty, you don't have to worry about statGroupHash and how it alters stats: the already alteredstats are provided to you.  But if you want to see how the sausage gets made, or perform computationsyourself, this is valuable information.

        :return: The stat_group_hash of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        :rtype: int
        """
        return self._stat_group_hash

    @stat_group_hash.setter
    def stat_group_hash(self, stat_group_hash):
        """
        Sets the stat_group_hash of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        If the item's stats are meant to be modified by a DestinyStatGroupDefinition, this willbe the identifier for that definition.  If you are using live data or precomputed stats data on the DestinyInventoryItemDefinition.stats.statsproperty, you don't have to worry about statGroupHash and how it alters stats: the already alteredstats are provided to you.  But if you want to see how the sausage gets made, or perform computationsyourself, this is valuable information.

        :param stat_group_hash: The stat_group_hash of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        :type: int
        """

        self._stat_group_hash = stat_group_hash

    @property
    def stats(self):
        """
        Gets the stats of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        If you are looking for precomputed values for the stats on a weapon, this is where they are stored.Technically these are the \"Display\" stat values.  Please see DestinyStatsDefinition for whatDisplay Stat Values means, it's a very long story... but essentially these are the closest valuesBNet can get to the item stats that you see in-game.  These stats are keyed by the DestinyStatDefinition's hash identifier for the statthat's found on the item.

        :return: The stats of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        :rtype: dict(str, ComponentsschemasDestinyDefinitionsDestinyInventoryItemStatDefinition)
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """
        Sets the stats of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        If you are looking for precomputed values for the stats on a weapon, this is where they are stored.Technically these are the \"Display\" stat values.  Please see DestinyStatsDefinition for whatDisplay Stat Values means, it's a very long story... but essentially these are the closest valuesBNet can get to the item stats that you see in-game.  These stats are keyed by the DestinyStatDefinition's hash identifier for the statthat's found on the item.

        :param stats: The stats of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        :type: dict(str, ComponentsschemasDestinyDefinitionsDestinyInventoryItemStatDefinition)
        """

        self._stats = stats

    @property
    def has_displayable_stats(self):
        """
        Gets the has_displayable_stats of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        A quick and lazy way to determine whether any stat other than the \"primary\" stat is actuallyvisible on the item.  Items often have stats that we return in case people find them useful, butthey're not part of the \"Stat Group\" and thus we wouldn't display them in our UI.  If this is False,then we're not going to display any of these stats other than the primary one.

        :return: The has_displayable_stats of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        :rtype: bool
        """
        return self._has_displayable_stats

    @has_displayable_stats.setter
    def has_displayable_stats(self, has_displayable_stats):
        """
        Sets the has_displayable_stats of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        A quick and lazy way to determine whether any stat other than the \"primary\" stat is actuallyvisible on the item.  Items often have stats that we return in case people find them useful, butthey're not part of the \"Stat Group\" and thus we wouldn't display them in our UI.  If this is False,then we're not going to display any of these stats other than the primary one.

        :param has_displayable_stats: The has_displayable_stats of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        :type: bool
        """

        self._has_displayable_stats = has_displayable_stats

    @property
    def primary_base_stat_hash(self):
        """
        Gets the primary_base_stat_hash of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        This stat is determined to be the \"primary\" stat, and can be looked up in the stats or anyother stat collection related to the item.  Use this hash to look up the stat's value using DestinyInventoryItemDefinition.stats.stats,and the renderable data for the primary stat in the related DestinyStatDefinition.

        :return: The primary_base_stat_hash of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        :rtype: int
        """
        return self._primary_base_stat_hash

    @primary_base_stat_hash.setter
    def primary_base_stat_hash(self, primary_base_stat_hash):
        """
        Sets the primary_base_stat_hash of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        This stat is determined to be the \"primary\" stat, and can be looked up in the stats or anyother stat collection related to the item.  Use this hash to look up the stat's value using DestinyInventoryItemDefinition.stats.stats,and the renderable data for the primary stat in the related DestinyStatDefinition.

        :param primary_base_stat_hash: The primary_base_stat_hash of this DestinyDefinitionsDestinyItemStatBlockDefinition.
        :type: int
        """

        self._primary_base_stat_hash = primary_base_stat_hash

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
        if not isinstance(other, DestinyDefinitionsDestinyItemStatBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
