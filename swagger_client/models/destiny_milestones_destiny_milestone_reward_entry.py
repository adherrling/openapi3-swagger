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


class DestinyMilestonesDestinyMilestoneRewardEntry(object):
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
        'reward_entry_hash': 'int',
        'earned': 'bool',
        'redeemed': 'bool'
    }

    attribute_map = {
        'reward_entry_hash': 'rewardEntryHash',
        'earned': 'earned',
        'redeemed': 'redeemed'
    }

    def __init__(self, reward_entry_hash=None, earned=None, redeemed=None):
        """
        DestinyMilestonesDestinyMilestoneRewardEntry - a model defined in Swagger
        """

        self._reward_entry_hash = None
        self._earned = None
        self._redeemed = None
        self.discriminator = None

        if reward_entry_hash is not None:
          self.reward_entry_hash = reward_entry_hash
        if earned is not None:
          self.earned = earned
        if redeemed is not None:
          self.redeemed = redeemed

    @property
    def reward_entry_hash(self):
        """
        Gets the reward_entry_hash of this DestinyMilestonesDestinyMilestoneRewardEntry.
        The identifier for the reward entry in question.  It is important to look up the relatedDestinyMilestoneRewardEntryDefinition to get the static details about the reward, whichyou can do by looking up the milestone's DestinyMilestoneDefinition and examining theDestinyMilestoneDefinition.rewards[rewardCategoryHash].rewardEntries[rewardEntryHash] data.

        :return: The reward_entry_hash of this DestinyMilestonesDestinyMilestoneRewardEntry.
        :rtype: int
        """
        return self._reward_entry_hash

    @reward_entry_hash.setter
    def reward_entry_hash(self, reward_entry_hash):
        """
        Sets the reward_entry_hash of this DestinyMilestonesDestinyMilestoneRewardEntry.
        The identifier for the reward entry in question.  It is important to look up the relatedDestinyMilestoneRewardEntryDefinition to get the static details about the reward, whichyou can do by looking up the milestone's DestinyMilestoneDefinition and examining theDestinyMilestoneDefinition.rewards[rewardCategoryHash].rewardEntries[rewardEntryHash] data.

        :param reward_entry_hash: The reward_entry_hash of this DestinyMilestonesDestinyMilestoneRewardEntry.
        :type: int
        """

        self._reward_entry_hash = reward_entry_hash

    @property
    def earned(self):
        """
        Gets the earned of this DestinyMilestonesDestinyMilestoneRewardEntry.
        If TRUE, the player has earned this reward.

        :return: The earned of this DestinyMilestonesDestinyMilestoneRewardEntry.
        :rtype: bool
        """
        return self._earned

    @earned.setter
    def earned(self, earned):
        """
        Sets the earned of this DestinyMilestonesDestinyMilestoneRewardEntry.
        If TRUE, the player has earned this reward.

        :param earned: The earned of this DestinyMilestonesDestinyMilestoneRewardEntry.
        :type: bool
        """

        self._earned = earned

    @property
    def redeemed(self):
        """
        Gets the redeemed of this DestinyMilestonesDestinyMilestoneRewardEntry.
        If TRUE, the player has redeemed/picked up/obtained this reward.Feel free to alias this to \"gotTheShinyBauble\" in your own codebase.

        :return: The redeemed of this DestinyMilestonesDestinyMilestoneRewardEntry.
        :rtype: bool
        """
        return self._redeemed

    @redeemed.setter
    def redeemed(self, redeemed):
        """
        Sets the redeemed of this DestinyMilestonesDestinyMilestoneRewardEntry.
        If TRUE, the player has redeemed/picked up/obtained this reward.Feel free to alias this to \"gotTheShinyBauble\" in your own codebase.

        :param redeemed: The redeemed of this DestinyMilestonesDestinyMilestoneRewardEntry.
        :type: bool
        """

        self._redeemed = redeemed

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
        if not isinstance(other, DestinyMilestonesDestinyMilestoneRewardEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other