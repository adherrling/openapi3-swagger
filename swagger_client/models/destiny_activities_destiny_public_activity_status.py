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


class DestinyActivitiesDestinyPublicActivityStatus(object):
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
        'challenge_objective_hashes': 'list[int]',
        'modifier_hashes': 'list[int]',
        'reward_tooltip_items': 'list[ComponentsschemasDestinyDestinyItemQuantity]'
    }

    attribute_map = {
        'challenge_objective_hashes': 'challengeObjectiveHashes',
        'modifier_hashes': 'modifierHashes',
        'reward_tooltip_items': 'rewardTooltipItems'
    }

    def __init__(self, challenge_objective_hashes=None, modifier_hashes=None, reward_tooltip_items=None):
        """
        DestinyActivitiesDestinyPublicActivityStatus - a model defined in Swagger
        """

        self._challenge_objective_hashes = None
        self._modifier_hashes = None
        self._reward_tooltip_items = None
        self.discriminator = None

        if challenge_objective_hashes is not None:
          self.challenge_objective_hashes = challenge_objective_hashes
        if modifier_hashes is not None:
          self.modifier_hashes = modifier_hashes
        if reward_tooltip_items is not None:
          self.reward_tooltip_items = reward_tooltip_items

    @property
    def challenge_objective_hashes(self):
        """
        Gets the challenge_objective_hashes of this DestinyActivitiesDestinyPublicActivityStatus.
        Active Challenges for the activity, if any - represented as hashes for DestinyObjectiveDefinitions.

        :return: The challenge_objective_hashes of this DestinyActivitiesDestinyPublicActivityStatus.
        :rtype: list[int]
        """
        return self._challenge_objective_hashes

    @challenge_objective_hashes.setter
    def challenge_objective_hashes(self, challenge_objective_hashes):
        """
        Sets the challenge_objective_hashes of this DestinyActivitiesDestinyPublicActivityStatus.
        Active Challenges for the activity, if any - represented as hashes for DestinyObjectiveDefinitions.

        :param challenge_objective_hashes: The challenge_objective_hashes of this DestinyActivitiesDestinyPublicActivityStatus.
        :type: list[int]
        """

        self._challenge_objective_hashes = challenge_objective_hashes

    @property
    def modifier_hashes(self):
        """
        Gets the modifier_hashes of this DestinyActivitiesDestinyPublicActivityStatus.
        The active modifiers on this activity, if any - represented as hashes for DestinyActivityModifierDefinitions.

        :return: The modifier_hashes of this DestinyActivitiesDestinyPublicActivityStatus.
        :rtype: list[int]
        """
        return self._modifier_hashes

    @modifier_hashes.setter
    def modifier_hashes(self, modifier_hashes):
        """
        Sets the modifier_hashes of this DestinyActivitiesDestinyPublicActivityStatus.
        The active modifiers on this activity, if any - represented as hashes for DestinyActivityModifierDefinitions.

        :param modifier_hashes: The modifier_hashes of this DestinyActivitiesDestinyPublicActivityStatus.
        :type: list[int]
        """

        self._modifier_hashes = modifier_hashes

    @property
    def reward_tooltip_items(self):
        """
        Gets the reward_tooltip_items of this DestinyActivitiesDestinyPublicActivityStatus.
        If the activity itself provides any specific \"mock\" rewards, this will be the items and their quantity.  Why \"mock\", you ask?  Because these are the rewards as they are represented in the tooltip of the Activity.  These are often pointers to fake items that look good in a tooltip, but represent an abstract concept of what you will get for a reward rather than the specific items you may obtain.

        :return: The reward_tooltip_items of this DestinyActivitiesDestinyPublicActivityStatus.
        :rtype: list[ComponentsschemasDestinyDestinyItemQuantity]
        """
        return self._reward_tooltip_items

    @reward_tooltip_items.setter
    def reward_tooltip_items(self, reward_tooltip_items):
        """
        Sets the reward_tooltip_items of this DestinyActivitiesDestinyPublicActivityStatus.
        If the activity itself provides any specific \"mock\" rewards, this will be the items and their quantity.  Why \"mock\", you ask?  Because these are the rewards as they are represented in the tooltip of the Activity.  These are often pointers to fake items that look good in a tooltip, but represent an abstract concept of what you will get for a reward rather than the specific items you may obtain.

        :param reward_tooltip_items: The reward_tooltip_items of this DestinyActivitiesDestinyPublicActivityStatus.
        :type: list[ComponentsschemasDestinyDestinyItemQuantity]
        """

        self._reward_tooltip_items = reward_tooltip_items

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
        if not isinstance(other, DestinyActivitiesDestinyPublicActivityStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
