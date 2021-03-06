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


class DestinyDefinitionsMilestonesDestinyMilestoneDefinition(object):
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
        'display_properties': 'ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition',
        'image': 'str',
        'recruitable': 'bool',
        'friendly_name': 'str',
        'show_in_explorer': 'bool',
        'has_predictable_dates': 'bool',
        'quests': 'dict(str, ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneQuestDefinition)',
        'rewards': 'dict(str, ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneRewardCategoryDefinition)',
        'vendors': 'list[ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneVendorDefinition]',
        'values': 'dict(str, ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneValueDefinition)',
        'is_in_game_milestone': 'bool',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'image': 'image',
        'recruitable': 'recruitable',
        'friendly_name': 'friendlyName',
        'show_in_explorer': 'showInExplorer',
        'has_predictable_dates': 'hasPredictableDates',
        'quests': 'quests',
        'rewards': 'rewards',
        'vendors': 'vendors',
        'values': 'values',
        'is_in_game_milestone': 'isInGameMilestone',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, image=None, recruitable=None, friendly_name=None, show_in_explorer=None, has_predictable_dates=None, quests=None, rewards=None, vendors=None, values=None, is_in_game_milestone=None, hash=None, index=None, redacted=None):
        """
        DestinyDefinitionsMilestonesDestinyMilestoneDefinition - a model defined in Swagger
        """

        self._display_properties = None
        self._image = None
        self._recruitable = None
        self._friendly_name = None
        self._show_in_explorer = None
        self._has_predictable_dates = None
        self._quests = None
        self._rewards = None
        self._vendors = None
        self._values = None
        self._is_in_game_milestone = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
          self.display_properties = display_properties
        if image is not None:
          self.image = image
        if recruitable is not None:
          self.recruitable = recruitable
        if friendly_name is not None:
          self.friendly_name = friendly_name
        if show_in_explorer is not None:
          self.show_in_explorer = show_in_explorer
        if has_predictable_dates is not None:
          self.has_predictable_dates = has_predictable_dates
        if quests is not None:
          self.quests = quests
        if rewards is not None:
          self.rewards = rewards
        if vendors is not None:
          self.vendors = vendors
        if values is not None:
          self.values = values
        if is_in_game_milestone is not None:
          self.is_in_game_milestone = is_in_game_milestone
        if hash is not None:
          self.hash = hash
        if index is not None:
          self.index = index
        if redacted is not None:
          self.redacted = redacted

    @property
    def display_properties(self):
        """
        Gets the display_properties of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.

        :return: The display_properties of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """
        Sets the display_properties of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.

        :param display_properties: The display_properties of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def image(self):
        """
        Gets the image of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        A custom image someone made just for the milestone.  Isn't that special?

        :return: The image of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        A custom image someone made just for the milestone.  Isn't that special?

        :param image: The image of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: str
        """

        self._image = image

    @property
    def recruitable(self):
        """
        Gets the recruitable of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        If True, then the Milestone has been integrated with BNet's recruiting feature.

        :return: The recruitable of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: bool
        """
        return self._recruitable

    @recruitable.setter
    def recruitable(self, recruitable):
        """
        Sets the recruitable of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        If True, then the Milestone has been integrated with BNet's recruiting feature.

        :param recruitable: The recruitable of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: bool
        """

        self._recruitable = recruitable

    @property
    def friendly_name(self):
        """
        Gets the friendly_name of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        If the milestone has a friendly identifier for association with other features - such as Recruiting - thatidentifier can be found here.  This is \"friendly\" in that it looks better in a URL than whateverthe identifier for the Milestone actually is.

        :return: The friendly_name of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """
        Sets the friendly_name of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        If the milestone has a friendly identifier for association with other features - such as Recruiting - thatidentifier can be found here.  This is \"friendly\" in that it looks better in a URL than whateverthe identifier for the Milestone actually is.

        :param friendly_name: The friendly_name of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def show_in_explorer(self):
        """
        Gets the show_in_explorer of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        If TRUE, this entry should be returned in the list of milestones for the \"Explore Destiny\"(i.e. new BNet homepage) features of Bungie.net (as long as the underlying event is active)

        :return: The show_in_explorer of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: bool
        """
        return self._show_in_explorer

    @show_in_explorer.setter
    def show_in_explorer(self, show_in_explorer):
        """
        Sets the show_in_explorer of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        If TRUE, this entry should be returned in the list of milestones for the \"Explore Destiny\"(i.e. new BNet homepage) features of Bungie.net (as long as the underlying event is active)

        :param show_in_explorer: The show_in_explorer of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: bool
        """

        self._show_in_explorer = show_in_explorer

    @property
    def has_predictable_dates(self):
        """
        Gets the has_predictable_dates of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        A shortcut for clients - and the server - to understand whether we can predict the start and end datesfor this event.  In practice, there are multiple ways that an event could have predictable date ranges, but not allevents will be able to be predicted via any mechanism (for instance, events that are manually triggered on and off)

        :return: The has_predictable_dates of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: bool
        """
        return self._has_predictable_dates

    @has_predictable_dates.setter
    def has_predictable_dates(self, has_predictable_dates):
        """
        Sets the has_predictable_dates of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        A shortcut for clients - and the server - to understand whether we can predict the start and end datesfor this event.  In practice, there are multiple ways that an event could have predictable date ranges, but not allevents will be able to be predicted via any mechanism (for instance, events that are manually triggered on and off)

        :param has_predictable_dates: The has_predictable_dates of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: bool
        """

        self._has_predictable_dates = has_predictable_dates

    @property
    def quests(self):
        """
        Gets the quests of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        The full set of possible Quests that give the overview of the Milestone event/activity in question.Only one of these can be active at a time for a given Conceptual Milestone, but many of them may be\"available\" for the user to choose from. (for instance, with Milestones you can choose from the threeavailable Quests, but only one can be active at a time)Keyed by the quest item.

        :return: The quests of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: dict(str, ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneQuestDefinition)
        """
        return self._quests

    @quests.setter
    def quests(self, quests):
        """
        Sets the quests of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        The full set of possible Quests that give the overview of the Milestone event/activity in question.Only one of these can be active at a time for a given Conceptual Milestone, but many of them may be\"available\" for the user to choose from. (for instance, with Milestones you can choose from the threeavailable Quests, but only one can be active at a time)Keyed by the quest item.

        :param quests: The quests of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: dict(str, ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneQuestDefinition)
        """

        self._quests = quests

    @property
    def rewards(self):
        """
        Gets the rewards of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        If this milestone can provide rewards, this will define the categoriesinto which the individual reward entries are placed.

        :return: The rewards of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: dict(str, ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneRewardCategoryDefinition)
        """
        return self._rewards

    @rewards.setter
    def rewards(self, rewards):
        """
        Sets the rewards of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        If this milestone can provide rewards, this will define the categoriesinto which the individual reward entries are placed.

        :param rewards: The rewards of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: dict(str, ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneRewardCategoryDefinition)
        """

        self._rewards = rewards

    @property
    def vendors(self):
        """
        Gets the vendors of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        Sometimes, milestones will have rewards provided by Vendors.  This definition gives the information neededto understand which vendors are relevant, the order in which they should be returned if order matters,and the conditions under which the Vendor is relevant to the user.

        :return: The vendors of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneVendorDefinition]
        """
        return self._vendors

    @vendors.setter
    def vendors(self, vendors):
        """
        Sets the vendors of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        Sometimes, milestones will have rewards provided by Vendors.  This definition gives the information neededto understand which vendors are relevant, the order in which they should be returned if order matters,and the conditions under which the Vendor is relevant to the user.

        :param vendors: The vendors of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneVendorDefinition]
        """

        self._vendors = vendors

    @property
    def values(self):
        """
        Gets the values of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        Sometimes, milestones will have arbitrary values associated with them that are of interest to usor to third party developers.  This is the collection of those values' definitions, keyed by the identifierof the value and providing useful definition information such as localizable names and descriptions for the value.

        :return: The values of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: dict(str, ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneValueDefinition)
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        Sometimes, milestones will have arbitrary values associated with them that are of interest to usor to third party developers.  This is the collection of those values' definitions, keyed by the identifierof the value and providing useful definition information such as localizable names and descriptions for the value.

        :param values: The values of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: dict(str, ComponentsschemasDestinyDefinitionsMilestonesDestinyMilestoneValueDefinition)
        """

        self._values = values

    @property
    def is_in_game_milestone(self):
        """
        Gets the is_in_game_milestone of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        Some milestones are explicit objectives that you can see and interact with in the game.Some milestones are more conceptual, built by BNet to help advise you on activities and eventsthat happen in-game but that aren't explicitly shown in game as Milestones.If this is TRUE, you can see this as a milestone in the game.If this is FALSE, it's an event or activity you can participate in, but you won't see it asa Milestone in the game's UI.

        :return: The is_in_game_milestone of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: bool
        """
        return self._is_in_game_milestone

    @is_in_game_milestone.setter
    def is_in_game_milestone(self, is_in_game_milestone):
        """
        Sets the is_in_game_milestone of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        Some milestones are explicit objectives that you can see and interact with in the game.Some milestones are more conceptual, built by BNet to help advise you on activities and eventsthat happen in-game but that aren't explicitly shown in game as Milestones.If this is TRUE, you can see this as a milestone in the game.If this is FALSE, it's an event or activity you can participate in, but you won't see it asa Milestone in the game's UI.

        :param is_in_game_milestone: The is_in_game_milestone of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: bool
        """

        self._is_in_game_milestone = is_in_game_milestone

    @property
    def hash(self):
        """
        Gets the hash of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :return: The hash of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :param hash: The hash of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """
        Gets the index of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        The index of the entity as it was found in the investment tables.

        :return: The index of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        The index of the entity as it was found in the investment tables.

        :param index: The index of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """
        Gets the redacted of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :return: The redacted of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """
        Sets the redacted of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :param redacted: The redacted of this DestinyDefinitionsMilestonesDestinyMilestoneDefinition.
        :type: bool
        """

        self._redacted = redacted

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
        if not isinstance(other, DestinyDefinitionsMilestonesDestinyMilestoneDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
