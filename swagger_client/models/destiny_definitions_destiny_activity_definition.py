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


class DestinyDefinitionsDestinyActivityDefinition(object):
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
        'release_icon': 'str',
        'release_time': 'int',
        'activity_level': 'int',
        'activity_light_level': 'int',
        'destination_hash': 'int',
        'place_hash': 'int',
        'activity_type_hash': 'int',
        'tier': 'int',
        'pgcr_image': 'str',
        'rewards': 'list[ComponentsschemasDestinyDefinitionsDestinyActivityRewardDefinition]',
        'modifiers': 'list[ComponentsschemasDestinyDefinitionsDestinyActivityModifierReferenceDefinition]',
        'is_playlist': 'bool',
        'challenges': 'list[ComponentsschemasDestinyDefinitionsDestinyActivityChallengeDefinition]',
        'optional_unlock_strings': 'list[ComponentsschemasDestinyDefinitionsDestinyActivityUnlockStringDefinition]',
        'activity_graph_list': 'list[ComponentsschemasDestinyDefinitionsDestinyActivityGraphListEntryDefinition]',
        'activity_mode_hash': 'int',
        'is_pv_p': 'bool',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'release_icon': 'releaseIcon',
        'release_time': 'releaseTime',
        'activity_level': 'activityLevel',
        'activity_light_level': 'activityLightLevel',
        'destination_hash': 'destinationHash',
        'place_hash': 'placeHash',
        'activity_type_hash': 'activityTypeHash',
        'tier': 'tier',
        'pgcr_image': 'pgcrImage',
        'rewards': 'rewards',
        'modifiers': 'modifiers',
        'is_playlist': 'isPlaylist',
        'challenges': 'challenges',
        'optional_unlock_strings': 'optionalUnlockStrings',
        'activity_graph_list': 'activityGraphList',
        'activity_mode_hash': 'activityModeHash',
        'is_pv_p': 'isPvP',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, release_icon=None, release_time=None, activity_level=None, activity_light_level=None, destination_hash=None, place_hash=None, activity_type_hash=None, tier=None, pgcr_image=None, rewards=None, modifiers=None, is_playlist=None, challenges=None, optional_unlock_strings=None, activity_graph_list=None, activity_mode_hash=None, is_pv_p=None, hash=None, index=None, redacted=None):
        """
        DestinyDefinitionsDestinyActivityDefinition - a model defined in Swagger
        """

        self._release_icon = None
        self._release_time = None
        self._activity_level = None
        self._activity_light_level = None
        self._destination_hash = None
        self._place_hash = None
        self._activity_type_hash = None
        self._tier = None
        self._pgcr_image = None
        self._rewards = None
        self._modifiers = None
        self._is_playlist = None
        self._challenges = None
        self._optional_unlock_strings = None
        self._activity_graph_list = None
        self._activity_mode_hash = None
        self._is_pv_p = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if release_icon is not None:
          self.release_icon = release_icon
        if release_time is not None:
          self.release_time = release_time
        if activity_level is not None:
          self.activity_level = activity_level
        if activity_light_level is not None:
          self.activity_light_level = activity_light_level
        if destination_hash is not None:
          self.destination_hash = destination_hash
        if place_hash is not None:
          self.place_hash = place_hash
        if activity_type_hash is not None:
          self.activity_type_hash = activity_type_hash
        if tier is not None:
          self.tier = tier
        if pgcr_image is not None:
          self.pgcr_image = pgcr_image
        if rewards is not None:
          self.rewards = rewards
        if modifiers is not None:
          self.modifiers = modifiers
        if is_playlist is not None:
          self.is_playlist = is_playlist
        if challenges is not None:
          self.challenges = challenges
        if optional_unlock_strings is not None:
          self.optional_unlock_strings = optional_unlock_strings
        if activity_graph_list is not None:
          self.activity_graph_list = activity_graph_list
        if activity_mode_hash is not None:
          self.activity_mode_hash = activity_mode_hash
        if is_pv_p is not None:
          self.is_pv_p = is_pv_p
        if hash is not None:
          self.hash = hash
        if index is not None:
          self.index = index
        if redacted is not None:
          self.redacted = redacted

    @property
    def release_icon(self):
        """
        Gets the release_icon of this DestinyDefinitionsDestinyActivityDefinition.
        If the activity has an icon associated with a specific release (such as a DLC),this is the path to that release's icon.

        :return: The release_icon of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: str
        """
        return self._release_icon

    @release_icon.setter
    def release_icon(self, release_icon):
        """
        Sets the release_icon of this DestinyDefinitionsDestinyActivityDefinition.
        If the activity has an icon associated with a specific release (such as a DLC),this is the path to that release's icon.

        :param release_icon: The release_icon of this DestinyDefinitionsDestinyActivityDefinition.
        :type: str
        """

        self._release_icon = release_icon

    @property
    def release_time(self):
        """
        Gets the release_time of this DestinyDefinitionsDestinyActivityDefinition.
        If the activity will not be visible until a specific and known time, this will bethe seconds since the Epoch when it will become visible.

        :return: The release_time of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: int
        """
        return self._release_time

    @release_time.setter
    def release_time(self, release_time):
        """
        Sets the release_time of this DestinyDefinitionsDestinyActivityDefinition.
        If the activity will not be visible until a specific and known time, this will bethe seconds since the Epoch when it will become visible.

        :param release_time: The release_time of this DestinyDefinitionsDestinyActivityDefinition.
        :type: int
        """

        self._release_time = release_time

    @property
    def activity_level(self):
        """
        Gets the activity_level of this DestinyDefinitionsDestinyActivityDefinition.
        The difficulty level of the activity.

        :return: The activity_level of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: int
        """
        return self._activity_level

    @activity_level.setter
    def activity_level(self, activity_level):
        """
        Sets the activity_level of this DestinyDefinitionsDestinyActivityDefinition.
        The difficulty level of the activity.

        :param activity_level: The activity_level of this DestinyDefinitionsDestinyActivityDefinition.
        :type: int
        """

        self._activity_level = activity_level

    @property
    def activity_light_level(self):
        """
        Gets the activity_light_level of this DestinyDefinitionsDestinyActivityDefinition.
        The recommended light level for this activity.

        :return: The activity_light_level of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: int
        """
        return self._activity_light_level

    @activity_light_level.setter
    def activity_light_level(self, activity_light_level):
        """
        Sets the activity_light_level of this DestinyDefinitionsDestinyActivityDefinition.
        The recommended light level for this activity.

        :param activity_light_level: The activity_light_level of this DestinyDefinitionsDestinyActivityDefinition.
        :type: int
        """

        self._activity_light_level = activity_light_level

    @property
    def destination_hash(self):
        """
        Gets the destination_hash of this DestinyDefinitionsDestinyActivityDefinition.
        The hash identifier for the Destination on which this Activity is played.  Use it to look upthe DestinyDestinationDefinition for human readable info about the destination.A Destination can be thought of as a more specific location than a \"Place\".  For instance,if the \"Place\" is Earth, the \"Destination\" would be a specific city or region on Earth.

        :return: The destination_hash of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: int
        """
        return self._destination_hash

    @destination_hash.setter
    def destination_hash(self, destination_hash):
        """
        Sets the destination_hash of this DestinyDefinitionsDestinyActivityDefinition.
        The hash identifier for the Destination on which this Activity is played.  Use it to look upthe DestinyDestinationDefinition for human readable info about the destination.A Destination can be thought of as a more specific location than a \"Place\".  For instance,if the \"Place\" is Earth, the \"Destination\" would be a specific city or region on Earth.

        :param destination_hash: The destination_hash of this DestinyDefinitionsDestinyActivityDefinition.
        :type: int
        """

        self._destination_hash = destination_hash

    @property
    def place_hash(self):
        """
        Gets the place_hash of this DestinyDefinitionsDestinyActivityDefinition.
        The hash identifier for the \"Place\" on which this Activity is played.  Use it to look upthe DestinyPlaceDefinition for human readable info about the Place.A Place is the largest-scoped concept for location information.  For instance,if the \"Place\" is Earth, the \"Destination\" would be a specific city or region on Earth.

        :return: The place_hash of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: int
        """
        return self._place_hash

    @place_hash.setter
    def place_hash(self, place_hash):
        """
        Sets the place_hash of this DestinyDefinitionsDestinyActivityDefinition.
        The hash identifier for the \"Place\" on which this Activity is played.  Use it to look upthe DestinyPlaceDefinition for human readable info about the Place.A Place is the largest-scoped concept for location information.  For instance,if the \"Place\" is Earth, the \"Destination\" would be a specific city or region on Earth.

        :param place_hash: The place_hash of this DestinyDefinitionsDestinyActivityDefinition.
        :type: int
        """

        self._place_hash = place_hash

    @property
    def activity_type_hash(self):
        """
        Gets the activity_type_hash of this DestinyDefinitionsDestinyActivityDefinition.
        The hash identifier for the Activity Type of this Activity.  You may use it to look upthe DestinyActivityTypeDefinition for human readable info, but be forewarned: Playlists andmany PVP Map Activities will map to generic Activity Types.  You'll have to use your knowledgeof the Activity Mode being played to get more specific information about what the user is playing.

        :return: The activity_type_hash of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: int
        """
        return self._activity_type_hash

    @activity_type_hash.setter
    def activity_type_hash(self, activity_type_hash):
        """
        Sets the activity_type_hash of this DestinyDefinitionsDestinyActivityDefinition.
        The hash identifier for the Activity Type of this Activity.  You may use it to look upthe DestinyActivityTypeDefinition for human readable info, but be forewarned: Playlists andmany PVP Map Activities will map to generic Activity Types.  You'll have to use your knowledgeof the Activity Mode being played to get more specific information about what the user is playing.

        :param activity_type_hash: The activity_type_hash of this DestinyDefinitionsDestinyActivityDefinition.
        :type: int
        """

        self._activity_type_hash = activity_type_hash

    @property
    def tier(self):
        """
        Gets the tier of this DestinyDefinitionsDestinyActivityDefinition.
        The difficulty tier of the activity.

        :return: The tier of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: int
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """
        Sets the tier of this DestinyDefinitionsDestinyActivityDefinition.
        The difficulty tier of the activity.

        :param tier: The tier of this DestinyDefinitionsDestinyActivityDefinition.
        :type: int
        """

        self._tier = tier

    @property
    def pgcr_image(self):
        """
        Gets the pgcr_image of this DestinyDefinitionsDestinyActivityDefinition.
        When Activities are completed, we generate a \"Post-Game Carnage Report\", or PGCR, with details aboutwhat happened in that activity (how many kills someone got, which team won, etc...)  We use this imageas the background when displaying PGCR information, and often use it when we refer to the Activity in general.

        :return: The pgcr_image of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: str
        """
        return self._pgcr_image

    @pgcr_image.setter
    def pgcr_image(self, pgcr_image):
        """
        Sets the pgcr_image of this DestinyDefinitionsDestinyActivityDefinition.
        When Activities are completed, we generate a \"Post-Game Carnage Report\", or PGCR, with details aboutwhat happened in that activity (how many kills someone got, which team won, etc...)  We use this imageas the background when displaying PGCR information, and often use it when we refer to the Activity in general.

        :param pgcr_image: The pgcr_image of this DestinyDefinitionsDestinyActivityDefinition.
        :type: str
        """

        self._pgcr_image = pgcr_image

    @property
    def rewards(self):
        """
        Gets the rewards of this DestinyDefinitionsDestinyActivityDefinition.
        The expected possible rewards for the activity.  These rewards may or may not be accessible for an individual playerbased on their character state, the account state, and even the game's state overall.  But it is a useful referencefor possible rewards you can earn in the activity.  These match up to rewards displayed when you hover overthe Activity in the in-game Director, and often refer to Placeholder or \"Dummy\" items: items that tell you what you can earn in vague terms rather than what you'll specifically be earning (partly because the gamedoesn't even know what you'll earn specifically until you roll for it at the end)

        :return: The rewards of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDestinyActivityRewardDefinition]
        """
        return self._rewards

    @rewards.setter
    def rewards(self, rewards):
        """
        Sets the rewards of this DestinyDefinitionsDestinyActivityDefinition.
        The expected possible rewards for the activity.  These rewards may or may not be accessible for an individual playerbased on their character state, the account state, and even the game's state overall.  But it is a useful referencefor possible rewards you can earn in the activity.  These match up to rewards displayed when you hover overthe Activity in the in-game Director, and often refer to Placeholder or \"Dummy\" items: items that tell you what you can earn in vague terms rather than what you'll specifically be earning (partly because the gamedoesn't even know what you'll earn specifically until you roll for it at the end)

        :param rewards: The rewards of this DestinyDefinitionsDestinyActivityDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDestinyActivityRewardDefinition]
        """

        self._rewards = rewards

    @property
    def modifiers(self):
        """
        Gets the modifiers of this DestinyDefinitionsDestinyActivityDefinition.
        Activities can have Modifiers, as defined in DestinyActivityModifierDefinition.  These are referencesto the modifiers that *can* be applied to that activity, along with data that we use to determine ifthat modifier is actually active at any given point in time.

        :return: The modifiers of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDestinyActivityModifierReferenceDefinition]
        """
        return self._modifiers

    @modifiers.setter
    def modifiers(self, modifiers):
        """
        Sets the modifiers of this DestinyDefinitionsDestinyActivityDefinition.
        Activities can have Modifiers, as defined in DestinyActivityModifierDefinition.  These are referencesto the modifiers that *can* be applied to that activity, along with data that we use to determine ifthat modifier is actually active at any given point in time.

        :param modifiers: The modifiers of this DestinyDefinitionsDestinyActivityDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDestinyActivityModifierReferenceDefinition]
        """

        self._modifiers = modifiers

    @property
    def is_playlist(self):
        """
        Gets the is_playlist of this DestinyDefinitionsDestinyActivityDefinition.
        If True, this Activity is actually a Playlist that refers to multiple possible specific Activities and ActivityModes.  For instance, a Crucible Playlist may have references to multiple Activities (Maps) with multiple Activity Modes(specific PvP gameplay modes).  If this is true, refer to the playlistItems property for the specific entriesin the playlist.

        :return: The is_playlist of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: bool
        """
        return self._is_playlist

    @is_playlist.setter
    def is_playlist(self, is_playlist):
        """
        Sets the is_playlist of this DestinyDefinitionsDestinyActivityDefinition.
        If True, this Activity is actually a Playlist that refers to multiple possible specific Activities and ActivityModes.  For instance, a Crucible Playlist may have references to multiple Activities (Maps) with multiple Activity Modes(specific PvP gameplay modes).  If this is true, refer to the playlistItems property for the specific entriesin the playlist.

        :param is_playlist: The is_playlist of this DestinyDefinitionsDestinyActivityDefinition.
        :type: bool
        """

        self._is_playlist = is_playlist

    @property
    def challenges(self):
        """
        Gets the challenges of this DestinyDefinitionsDestinyActivityDefinition.
        An activity can have many Challenges, of which any subset of them may be active for playat any given period of time.  This gives the information about the challenges and datathat we use to understand when they're active and what rewards they provide.Sadly, at the moment there's no central definition for challenges: much like \"Skulls\" werein Destiny 1, these are defined on individual activities and there can be many duplicates/near duplicatesacross the Destiny 2 ecosystem.  I have it in mind to centralize these in a future revision of the API, butwe are out of time.

        :return: The challenges of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDestinyActivityChallengeDefinition]
        """
        return self._challenges

    @challenges.setter
    def challenges(self, challenges):
        """
        Sets the challenges of this DestinyDefinitionsDestinyActivityDefinition.
        An activity can have many Challenges, of which any subset of them may be active for playat any given period of time.  This gives the information about the challenges and datathat we use to understand when they're active and what rewards they provide.Sadly, at the moment there's no central definition for challenges: much like \"Skulls\" werein Destiny 1, these are defined on individual activities and there can be many duplicates/near duplicatesacross the Destiny 2 ecosystem.  I have it in mind to centralize these in a future revision of the API, butwe are out of time.

        :param challenges: The challenges of this DestinyDefinitionsDestinyActivityDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDestinyActivityChallengeDefinition]
        """

        self._challenges = challenges

    @property
    def optional_unlock_strings(self):
        """
        Gets the optional_unlock_strings of this DestinyDefinitionsDestinyActivityDefinition.
        If there are status strings related to the activity and based on internal state of the game, account, or character,then this will be the definition of those strings and the states needed in order for the strings to be shown.

        :return: The optional_unlock_strings of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDestinyActivityUnlockStringDefinition]
        """
        return self._optional_unlock_strings

    @optional_unlock_strings.setter
    def optional_unlock_strings(self, optional_unlock_strings):
        """
        Sets the optional_unlock_strings of this DestinyDefinitionsDestinyActivityDefinition.
        If there are status strings related to the activity and based on internal state of the game, account, or character,then this will be the definition of those strings and the states needed in order for the strings to be shown.

        :param optional_unlock_strings: The optional_unlock_strings of this DestinyDefinitionsDestinyActivityDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDestinyActivityUnlockStringDefinition]
        """

        self._optional_unlock_strings = optional_unlock_strings

    @property
    def activity_graph_list(self):
        """
        Gets the activity_graph_list of this DestinyDefinitionsDestinyActivityDefinition.
        Unfortunately, in practice this is almost never populated.  In theory, this is supposed to tellwhich Activity Graph to show if you bring up the director while in this activity.

        :return: The activity_graph_list of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDestinyActivityGraphListEntryDefinition]
        """
        return self._activity_graph_list

    @activity_graph_list.setter
    def activity_graph_list(self, activity_graph_list):
        """
        Sets the activity_graph_list of this DestinyDefinitionsDestinyActivityDefinition.
        Unfortunately, in practice this is almost never populated.  In theory, this is supposed to tellwhich Activity Graph to show if you bring up the director while in this activity.

        :param activity_graph_list: The activity_graph_list of this DestinyDefinitionsDestinyActivityDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDestinyActivityGraphListEntryDefinition]
        """

        self._activity_graph_list = activity_graph_list

    @property
    def activity_mode_hash(self):
        """
        Gets the activity_mode_hash of this DestinyDefinitionsDestinyActivityDefinition.
        The Activity Mode for this activity.  Note that if this is a playlist, the specific playlist entry chosenwill determine the actual activity mode that ends up being played.

        :return: The activity_mode_hash of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: int
        """
        return self._activity_mode_hash

    @activity_mode_hash.setter
    def activity_mode_hash(self, activity_mode_hash):
        """
        Sets the activity_mode_hash of this DestinyDefinitionsDestinyActivityDefinition.
        The Activity Mode for this activity.  Note that if this is a playlist, the specific playlist entry chosenwill determine the actual activity mode that ends up being played.

        :param activity_mode_hash: The activity_mode_hash of this DestinyDefinitionsDestinyActivityDefinition.
        :type: int
        """

        self._activity_mode_hash = activity_mode_hash

    @property
    def is_pv_p(self):
        """
        Gets the is_pv_p of this DestinyDefinitionsDestinyActivityDefinition.
        If true, this activity is a PVP activity or playlist.

        :return: The is_pv_p of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: bool
        """
        return self._is_pv_p

    @is_pv_p.setter
    def is_pv_p(self, is_pv_p):
        """
        Sets the is_pv_p of this DestinyDefinitionsDestinyActivityDefinition.
        If true, this activity is a PVP activity or playlist.

        :param is_pv_p: The is_pv_p of this DestinyDefinitionsDestinyActivityDefinition.
        :type: bool
        """

        self._is_pv_p = is_pv_p

    @property
    def hash(self):
        """
        Gets the hash of this DestinyDefinitionsDestinyActivityDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :return: The hash of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this DestinyDefinitionsDestinyActivityDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :param hash: The hash of this DestinyDefinitionsDestinyActivityDefinition.
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """
        Gets the index of this DestinyDefinitionsDestinyActivityDefinition.
        The index of the entity as it was found in the investment tables.

        :return: The index of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this DestinyDefinitionsDestinyActivityDefinition.
        The index of the entity as it was found in the investment tables.

        :param index: The index of this DestinyDefinitionsDestinyActivityDefinition.
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """
        Gets the redacted of this DestinyDefinitionsDestinyActivityDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :return: The redacted of this DestinyDefinitionsDestinyActivityDefinition.
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """
        Sets the redacted of this DestinyDefinitionsDestinyActivityDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :param redacted: The redacted of this DestinyDefinitionsDestinyActivityDefinition.
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
        if not isinstance(other, DestinyDefinitionsDestinyActivityDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other