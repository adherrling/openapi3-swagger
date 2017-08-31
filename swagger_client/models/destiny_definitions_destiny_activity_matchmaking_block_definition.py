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


class DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition(object):
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
        'is_matchmade': 'bool',
        'min_party': 'int',
        'max_party': 'int',
        'max_players': 'int',
        'requires_guardian_oath': 'bool'
    }

    attribute_map = {
        'is_matchmade': 'isMatchmade',
        'min_party': 'minParty',
        'max_party': 'maxParty',
        'max_players': 'maxPlayers',
        'requires_guardian_oath': 'requiresGuardianOath'
    }

    def __init__(self, is_matchmade=None, min_party=None, max_party=None, max_players=None, requires_guardian_oath=None):
        """
        DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition - a model defined in Swagger
        """

        self._is_matchmade = None
        self._min_party = None
        self._max_party = None
        self._max_players = None
        self._requires_guardian_oath = None
        self.discriminator = None

        if is_matchmade is not None:
          self.is_matchmade = is_matchmade
        if min_party is not None:
          self.min_party = min_party
        if max_party is not None:
          self.max_party = max_party
        if max_players is not None:
          self.max_players = max_players
        if requires_guardian_oath is not None:
          self.requires_guardian_oath = requires_guardian_oath

    @property
    def is_matchmade(self):
        """
        Gets the is_matchmade of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        If TRUE, the activity is matchmade.  Otherwise, it requires explicit forming of a party.

        :return: The is_matchmade of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        :rtype: bool
        """
        return self._is_matchmade

    @is_matchmade.setter
    def is_matchmade(self, is_matchmade):
        """
        Sets the is_matchmade of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        If TRUE, the activity is matchmade.  Otherwise, it requires explicit forming of a party.

        :param is_matchmade: The is_matchmade of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        :type: bool
        """

        self._is_matchmade = is_matchmade

    @property
    def min_party(self):
        """
        Gets the min_party of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        The minimum # of people in the fireteam for the activity to launch.

        :return: The min_party of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        :rtype: int
        """
        return self._min_party

    @min_party.setter
    def min_party(self, min_party):
        """
        Sets the min_party of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        The minimum # of people in the fireteam for the activity to launch.

        :param min_party: The min_party of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        :type: int
        """

        self._min_party = min_party

    @property
    def max_party(self):
        """
        Gets the max_party of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        The maximum # of people allowed in a Fireteam.

        :return: The max_party of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        :rtype: int
        """
        return self._max_party

    @max_party.setter
    def max_party(self, max_party):
        """
        Sets the max_party of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        The maximum # of people allowed in a Fireteam.

        :param max_party: The max_party of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        :type: int
        """

        self._max_party = max_party

    @property
    def max_players(self):
        """
        Gets the max_players of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        The maximum # of people allowed across all teams in the activity.

        :return: The max_players of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        :rtype: int
        """
        return self._max_players

    @max_players.setter
    def max_players(self, max_players):
        """
        Sets the max_players of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        The maximum # of people allowed across all teams in the activity.

        :param max_players: The max_players of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        :type: int
        """

        self._max_players = max_players

    @property
    def requires_guardian_oath(self):
        """
        Gets the requires_guardian_oath of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        If true, you have to Solemnly Swear to be up to Nothing But Good(tm) to play.

        :return: The requires_guardian_oath of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        :rtype: bool
        """
        return self._requires_guardian_oath

    @requires_guardian_oath.setter
    def requires_guardian_oath(self, requires_guardian_oath):
        """
        Sets the requires_guardian_oath of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        If true, you have to Solemnly Swear to be up to Nothing But Good(tm) to play.

        :param requires_guardian_oath: The requires_guardian_oath of this DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.
        :type: bool
        """

        self._requires_guardian_oath = requires_guardian_oath

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
        if not isinstance(other, DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
