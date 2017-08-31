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


class DestinyEntitiesCharactersDestinyCharacterProgressionComponent(object):
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
        'progressions': 'dict(str, ComponentsschemasDestinyDestinyProgression)',
        'factions': 'dict(str, ComponentsschemasDestinyProgressionDestinyFactionProgression)',
        'milestones': 'dict(str, ComponentsschemasDestinyMilestonesDestinyMilestone)',
        'quests': 'list[ComponentsschemasDestinyQuestsDestinyQuestStatus]',
        'uninstanced_item_objectives': 'dict(str, list[ComponentsschemasDestinyQuestsDestinyObjectiveProgress])'
    }

    attribute_map = {
        'progressions': 'progressions',
        'factions': 'factions',
        'milestones': 'milestones',
        'quests': 'quests',
        'uninstanced_item_objectives': 'uninstancedItemObjectives'
    }

    def __init__(self, progressions=None, factions=None, milestones=None, quests=None, uninstanced_item_objectives=None):
        """
        DestinyEntitiesCharactersDestinyCharacterProgressionComponent - a model defined in Swagger
        """

        self._progressions = None
        self._factions = None
        self._milestones = None
        self._quests = None
        self._uninstanced_item_objectives = None
        self.discriminator = None

        if progressions is not None:
          self.progressions = progressions
        if factions is not None:
          self.factions = factions
        if milestones is not None:
          self.milestones = milestones
        if quests is not None:
          self.quests = quests
        if uninstanced_item_objectives is not None:
          self.uninstanced_item_objectives = uninstanced_item_objectives

    @property
    def progressions(self):
        """
        Gets the progressions of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        A Dictionary of all known progressions for the Character, keyed by the Progression's hash.  Not all progressions have user-facing data, but those who do will have that data contained in the DestinyProgressionDefinition.

        :return: The progressions of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        :rtype: dict(str, ComponentsschemasDestinyDestinyProgression)
        """
        return self._progressions

    @progressions.setter
    def progressions(self, progressions):
        """
        Sets the progressions of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        A Dictionary of all known progressions for the Character, keyed by the Progression's hash.  Not all progressions have user-facing data, but those who do will have that data contained in the DestinyProgressionDefinition.

        :param progressions: The progressions of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        :type: dict(str, ComponentsschemasDestinyDestinyProgression)
        """

        self._progressions = progressions

    @property
    def factions(self):
        """
        Gets the factions of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        A dictionary of all known Factions, keyed by the Faction's hash.  It contains data about this character'sstatus with the faction.

        :return: The factions of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        :rtype: dict(str, ComponentsschemasDestinyProgressionDestinyFactionProgression)
        """
        return self._factions

    @factions.setter
    def factions(self, factions):
        """
        Sets the factions of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        A dictionary of all known Factions, keyed by the Faction's hash.  It contains data about this character'sstatus with the faction.

        :param factions: The factions of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        :type: dict(str, ComponentsschemasDestinyProgressionDestinyFactionProgression)
        """

        self._factions = factions

    @property
    def milestones(self):
        """
        Gets the milestones of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        Milestones are related to the simple progressions shown in the game, but return additional andhopefully helpful information for users about the specifics of the Milestone's status.

        :return: The milestones of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        :rtype: dict(str, ComponentsschemasDestinyMilestonesDestinyMilestone)
        """
        return self._milestones

    @milestones.setter
    def milestones(self, milestones):
        """
        Sets the milestones of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        Milestones are related to the simple progressions shown in the game, but return additional andhopefully helpful information for users about the specifics of the Milestone's status.

        :param milestones: The milestones of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        :type: dict(str, ComponentsschemasDestinyMilestonesDestinyMilestone)
        """

        self._milestones = milestones

    @property
    def quests(self):
        """
        Gets the quests of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        If the user has any active quests, the quests' statuses will be returned here.  Note that quests have been largely supplanted by Milestones, but that doesn't mean thatthey won't make a comeback independent of milestones at some point.

        :return: The quests of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        :rtype: list[ComponentsschemasDestinyQuestsDestinyQuestStatus]
        """
        return self._quests

    @quests.setter
    def quests(self, quests):
        """
        Sets the quests of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        If the user has any active quests, the quests' statuses will be returned here.  Note that quests have been largely supplanted by Milestones, but that doesn't mean thatthey won't make a comeback independent of milestones at some point.

        :param quests: The quests of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        :type: list[ComponentsschemasDestinyQuestsDestinyQuestStatus]
        """

        self._quests = quests

    @property
    def uninstanced_item_objectives(self):
        """
        Gets the uninstanced_item_objectives of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        Sometimes, you have items in your inventory that don't have instances, but still haveObjective information.  This provides you that objective information for uninstanceditems.    This dictionary is keyed by the item's hash: which you can use to look up thename and description for the overall task(s) implied by the objective.The value is the list of objectives for this item, and their statuses.

        :return: The uninstanced_item_objectives of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        :rtype: dict(str, list[ComponentsschemasDestinyQuestsDestinyObjectiveProgress])
        """
        return self._uninstanced_item_objectives

    @uninstanced_item_objectives.setter
    def uninstanced_item_objectives(self, uninstanced_item_objectives):
        """
        Sets the uninstanced_item_objectives of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        Sometimes, you have items in your inventory that don't have instances, but still haveObjective information.  This provides you that objective information for uninstanceditems.    This dictionary is keyed by the item's hash: which you can use to look up thename and description for the overall task(s) implied by the objective.The value is the list of objectives for this item, and their statuses.

        :param uninstanced_item_objectives: The uninstanced_item_objectives of this DestinyEntitiesCharactersDestinyCharacterProgressionComponent.
        :type: dict(str, list[ComponentsschemasDestinyQuestsDestinyObjectiveProgress])
        """

        self._uninstanced_item_objectives = uninstanced_item_objectives

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
        if not isinstance(other, DestinyEntitiesCharactersDestinyCharacterProgressionComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
