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


class DestinyMilestonesDestinyPublicMilestone(object):
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
        'milestone_hash': 'int',
        'available_quests': 'list[ComponentsschemasDestinyMilestonesDestinyPublicMilestoneQuest]',
        'vendor_hashes': 'list[int]',
        'start_date': 'datetime',
        'end_date': 'datetime'
    }

    attribute_map = {
        'milestone_hash': 'milestoneHash',
        'available_quests': 'availableQuests',
        'vendor_hashes': 'vendorHashes',
        'start_date': 'startDate',
        'end_date': 'endDate'
    }

    def __init__(self, milestone_hash=None, available_quests=None, vendor_hashes=None, start_date=None, end_date=None):
        """
        DestinyMilestonesDestinyPublicMilestone - a model defined in Swagger
        """

        self._milestone_hash = None
        self._available_quests = None
        self._vendor_hashes = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if milestone_hash is not None:
          self.milestone_hash = milestone_hash
        if available_quests is not None:
          self.available_quests = available_quests
        if vendor_hashes is not None:
          self.vendor_hashes = vendor_hashes
        if start_date is not None:
          self.start_date = start_date
        if end_date is not None:
          self.end_date = end_date

    @property
    def milestone_hash(self):
        """
        Gets the milestone_hash of this DestinyMilestonesDestinyPublicMilestone.
        The hash identifier for the milestone.  Use it to look up the DestinyMilestoneDefinition forstatic data about the Milestone.

        :return: The milestone_hash of this DestinyMilestonesDestinyPublicMilestone.
        :rtype: int
        """
        return self._milestone_hash

    @milestone_hash.setter
    def milestone_hash(self, milestone_hash):
        """
        Sets the milestone_hash of this DestinyMilestonesDestinyPublicMilestone.
        The hash identifier for the milestone.  Use it to look up the DestinyMilestoneDefinition forstatic data about the Milestone.

        :param milestone_hash: The milestone_hash of this DestinyMilestonesDestinyPublicMilestone.
        :type: int
        """

        self._milestone_hash = milestone_hash

    @property
    def available_quests(self):
        """
        Gets the available_quests of this DestinyMilestonesDestinyPublicMilestone.
        A milestone not need have even a single quest, but if there are active quests they will be returned here.

        :return: The available_quests of this DestinyMilestonesDestinyPublicMilestone.
        :rtype: list[ComponentsschemasDestinyMilestonesDestinyPublicMilestoneQuest]
        """
        return self._available_quests

    @available_quests.setter
    def available_quests(self, available_quests):
        """
        Sets the available_quests of this DestinyMilestonesDestinyPublicMilestone.
        A milestone not need have even a single quest, but if there are active quests they will be returned here.

        :param available_quests: The available_quests of this DestinyMilestonesDestinyPublicMilestone.
        :type: list[ComponentsschemasDestinyMilestonesDestinyPublicMilestoneQuest]
        """

        self._available_quests = available_quests

    @property
    def vendor_hashes(self):
        """
        Gets the vendor_hashes of this DestinyMilestonesDestinyPublicMilestone.
        Sometimes milestones - or activities active in milestones - will have relevant vendors.These are the vendors that are currently relevant.

        :return: The vendor_hashes of this DestinyMilestonesDestinyPublicMilestone.
        :rtype: list[int]
        """
        return self._vendor_hashes

    @vendor_hashes.setter
    def vendor_hashes(self, vendor_hashes):
        """
        Sets the vendor_hashes of this DestinyMilestonesDestinyPublicMilestone.
        Sometimes milestones - or activities active in milestones - will have relevant vendors.These are the vendors that are currently relevant.

        :param vendor_hashes: The vendor_hashes of this DestinyMilestonesDestinyPublicMilestone.
        :type: list[int]
        """

        self._vendor_hashes = vendor_hashes

    @property
    def start_date(self):
        """
        Gets the start_date of this DestinyMilestonesDestinyPublicMilestone.
        If known, this is the date when the Milestone started/became active.

        :return: The start_date of this DestinyMilestonesDestinyPublicMilestone.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this DestinyMilestonesDestinyPublicMilestone.
        If known, this is the date when the Milestone started/became active.

        :param start_date: The start_date of this DestinyMilestonesDestinyPublicMilestone.
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this DestinyMilestonesDestinyPublicMilestone.
        If known, this is the date when the Milestone will expire/recycle/end.

        :return: The end_date of this DestinyMilestonesDestinyPublicMilestone.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this DestinyMilestonesDestinyPublicMilestone.
        If known, this is the date when the Milestone will expire/recycle/end.

        :param end_date: The end_date of this DestinyMilestonesDestinyPublicMilestone.
        :type: datetime
        """

        self._end_date = end_date

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
        if not isinstance(other, DestinyMilestonesDestinyPublicMilestone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
