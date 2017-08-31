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


class DestinyMilestonesDestinyMilestoneRewardCategory(object):
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
        'reward_category_hash': 'int',
        'entries': 'list[ComponentsschemasDestinyMilestonesDestinyMilestoneRewardEntry]'
    }

    attribute_map = {
        'reward_category_hash': 'rewardCategoryHash',
        'entries': 'entries'
    }

    def __init__(self, reward_category_hash=None, entries=None):
        """
        DestinyMilestonesDestinyMilestoneRewardCategory - a model defined in Swagger
        """

        self._reward_category_hash = None
        self._entries = None
        self.discriminator = None

        if reward_category_hash is not None:
          self.reward_category_hash = reward_category_hash
        if entries is not None:
          self.entries = entries

    @property
    def reward_category_hash(self):
        """
        Gets the reward_category_hash of this DestinyMilestonesDestinyMilestoneRewardCategory.
        Look up the relevant DestinyMilestoneDefinition, and then use rewardCategoryHash to look up thecategory info in DestinyMilestoneDefinition.rewards.

        :return: The reward_category_hash of this DestinyMilestonesDestinyMilestoneRewardCategory.
        :rtype: int
        """
        return self._reward_category_hash

    @reward_category_hash.setter
    def reward_category_hash(self, reward_category_hash):
        """
        Sets the reward_category_hash of this DestinyMilestonesDestinyMilestoneRewardCategory.
        Look up the relevant DestinyMilestoneDefinition, and then use rewardCategoryHash to look up thecategory info in DestinyMilestoneDefinition.rewards.

        :param reward_category_hash: The reward_category_hash of this DestinyMilestonesDestinyMilestoneRewardCategory.
        :type: int
        """

        self._reward_category_hash = reward_category_hash

    @property
    def entries(self):
        """
        Gets the entries of this DestinyMilestonesDestinyMilestoneRewardCategory.
        The individual reward entries for this category, and their status.

        :return: The entries of this DestinyMilestonesDestinyMilestoneRewardCategory.
        :rtype: list[ComponentsschemasDestinyMilestonesDestinyMilestoneRewardEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """
        Sets the entries of this DestinyMilestonesDestinyMilestoneRewardCategory.
        The individual reward entries for this category, and their status.

        :param entries: The entries of this DestinyMilestonesDestinyMilestoneRewardCategory.
        :type: list[ComponentsschemasDestinyMilestonesDestinyMilestoneRewardEntry]
        """

        self._entries = entries

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
        if not isinstance(other, DestinyMilestonesDestinyMilestoneRewardCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
