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


class DestinyMilestonesDestinyMilestoneActivityCompletionStatus(object):
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
        'completed': 'bool',
        'phases': 'list[ComponentsschemasDestinyMilestonesDestinyMilestoneActivityPhase]'
    }

    attribute_map = {
        'completed': 'completed',
        'phases': 'phases'
    }

    def __init__(self, completed=None, phases=None):
        """
        DestinyMilestonesDestinyMilestoneActivityCompletionStatus - a model defined in Swagger
        """

        self._completed = None
        self._phases = None
        self.discriminator = None

        if completed is not None:
          self.completed = completed
        if phases is not None:
          self.phases = phases

    @property
    def completed(self):
        """
        Gets the completed of this DestinyMilestonesDestinyMilestoneActivityCompletionStatus.
        If the activity has been \"completed\", that information will be returned here.

        :return: The completed of this DestinyMilestonesDestinyMilestoneActivityCompletionStatus.
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """
        Sets the completed of this DestinyMilestonesDestinyMilestoneActivityCompletionStatus.
        If the activity has been \"completed\", that information will be returned here.

        :param completed: The completed of this DestinyMilestonesDestinyMilestoneActivityCompletionStatus.
        :type: bool
        """

        self._completed = completed

    @property
    def phases(self):
        """
        Gets the phases of this DestinyMilestonesDestinyMilestoneActivityCompletionStatus.
        If the Activity has discrete \"phases\" that we can track, that info will be here.  Otherwise,this value will be NULL.Note that this is a list and not a dictionary: the order implies the ascending order of phasesor progression in this activity.

        :return: The phases of this DestinyMilestonesDestinyMilestoneActivityCompletionStatus.
        :rtype: list[ComponentsschemasDestinyMilestonesDestinyMilestoneActivityPhase]
        """
        return self._phases

    @phases.setter
    def phases(self, phases):
        """
        Sets the phases of this DestinyMilestonesDestinyMilestoneActivityCompletionStatus.
        If the Activity has discrete \"phases\" that we can track, that info will be here.  Otherwise,this value will be NULL.Note that this is a list and not a dictionary: the order implies the ascending order of phasesor progression in this activity.

        :param phases: The phases of this DestinyMilestonesDestinyMilestoneActivityCompletionStatus.
        :type: list[ComponentsschemasDestinyMilestonesDestinyMilestoneActivityPhase]
        """

        self._phases = phases

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
        if not isinstance(other, DestinyMilestonesDestinyMilestoneActivityCompletionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
