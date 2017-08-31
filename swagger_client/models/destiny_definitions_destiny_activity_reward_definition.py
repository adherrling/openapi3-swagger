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


class DestinyDefinitionsDestinyActivityRewardDefinition(object):
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
        'reward_text': 'str',
        'reward_items': 'list[ComponentsschemasDestinyDestinyItemQuantity]'
    }

    attribute_map = {
        'reward_text': 'rewardText',
        'reward_items': 'rewardItems'
    }

    def __init__(self, reward_text=None, reward_items=None):
        """
        DestinyDefinitionsDestinyActivityRewardDefinition - a model defined in Swagger
        """

        self._reward_text = None
        self._reward_items = None
        self.discriminator = None

        if reward_text is not None:
          self.reward_text = reward_text
        if reward_items is not None:
          self.reward_items = reward_items

    @property
    def reward_text(self):
        """
        Gets the reward_text of this DestinyDefinitionsDestinyActivityRewardDefinition.
        The header for the reward set, if any.

        :return: The reward_text of this DestinyDefinitionsDestinyActivityRewardDefinition.
        :rtype: str
        """
        return self._reward_text

    @reward_text.setter
    def reward_text(self, reward_text):
        """
        Sets the reward_text of this DestinyDefinitionsDestinyActivityRewardDefinition.
        The header for the reward set, if any.

        :param reward_text: The reward_text of this DestinyDefinitionsDestinyActivityRewardDefinition.
        :type: str
        """

        self._reward_text = reward_text

    @property
    def reward_items(self):
        """
        Gets the reward_items of this DestinyDefinitionsDestinyActivityRewardDefinition.
        The \"Items provided\" in the reward.  This is almost always a pointer to a DestinyInventoryItemDefintionfor an item that you can't actually earn in-game, but that has name/description/icon information forthe vague concept of the rewards you will receive.  This is because the actual reward generation isnon-deterministic and extremely complicated, so the best the game can do is tell you what you'll getin vague terms.  And so too shall we.  Interesting trivia: you actually *do* earn these items when you complete the activity.  They go into a single-slotbucket on your profile, which is how you see the pop-ups of these rewards when you complete an activity that matchthese \"dummy\" items.  You can even see them if you look at the last one you earned in yourprofile-level inventory through the BNet API!  Who said reading documentation is a waste of time?

        :return: The reward_items of this DestinyDefinitionsDestinyActivityRewardDefinition.
        :rtype: list[ComponentsschemasDestinyDestinyItemQuantity]
        """
        return self._reward_items

    @reward_items.setter
    def reward_items(self, reward_items):
        """
        Sets the reward_items of this DestinyDefinitionsDestinyActivityRewardDefinition.
        The \"Items provided\" in the reward.  This is almost always a pointer to a DestinyInventoryItemDefintionfor an item that you can't actually earn in-game, but that has name/description/icon information forthe vague concept of the rewards you will receive.  This is because the actual reward generation isnon-deterministic and extremely complicated, so the best the game can do is tell you what you'll getin vague terms.  And so too shall we.  Interesting trivia: you actually *do* earn these items when you complete the activity.  They go into a single-slotbucket on your profile, which is how you see the pop-ups of these rewards when you complete an activity that matchthese \"dummy\" items.  You can even see them if you look at the last one you earned in yourprofile-level inventory through the BNet API!  Who said reading documentation is a waste of time?

        :param reward_items: The reward_items of this DestinyDefinitionsDestinyActivityRewardDefinition.
        :type: list[ComponentsschemasDestinyDestinyItemQuantity]
        """

        self._reward_items = reward_items

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
        if not isinstance(other, DestinyDefinitionsDestinyActivityRewardDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
