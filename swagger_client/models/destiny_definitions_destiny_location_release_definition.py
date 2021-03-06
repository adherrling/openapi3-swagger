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


class DestinyDefinitionsDestinyLocationReleaseDefinition(object):
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
        'spawn_point': 'int',
        'destination_hash': 'int',
        'activity_hash': 'int',
        'activity_graph_hash': 'int',
        'activity_graph_node_hash': 'int',
        'activity_bubble_name': 'int',
        'activity_path_bundle': 'int',
        'activity_path_destination': 'int',
        'world_position': 'list[int]'
    }

    attribute_map = {
        'spawn_point': 'spawnPoint',
        'destination_hash': 'destinationHash',
        'activity_hash': 'activityHash',
        'activity_graph_hash': 'activityGraphHash',
        'activity_graph_node_hash': 'activityGraphNodeHash',
        'activity_bubble_name': 'activityBubbleName',
        'activity_path_bundle': 'activityPathBundle',
        'activity_path_destination': 'activityPathDestination',
        'world_position': 'worldPosition'
    }

    def __init__(self, spawn_point=None, destination_hash=None, activity_hash=None, activity_graph_hash=None, activity_graph_node_hash=None, activity_bubble_name=None, activity_path_bundle=None, activity_path_destination=None, world_position=None):
        """
        DestinyDefinitionsDestinyLocationReleaseDefinition - a model defined in Swagger
        """

        self._spawn_point = None
        self._destination_hash = None
        self._activity_hash = None
        self._activity_graph_hash = None
        self._activity_graph_node_hash = None
        self._activity_bubble_name = None
        self._activity_path_bundle = None
        self._activity_path_destination = None
        self._world_position = None
        self.discriminator = None

        if spawn_point is not None:
          self.spawn_point = spawn_point
        if destination_hash is not None:
          self.destination_hash = destination_hash
        if activity_hash is not None:
          self.activity_hash = activity_hash
        if activity_graph_hash is not None:
          self.activity_graph_hash = activity_graph_hash
        if activity_graph_node_hash is not None:
          self.activity_graph_node_hash = activity_graph_node_hash
        if activity_bubble_name is not None:
          self.activity_bubble_name = activity_bubble_name
        if activity_path_bundle is not None:
          self.activity_path_bundle = activity_path_bundle
        if activity_path_destination is not None:
          self.activity_path_destination = activity_path_destination
        if world_position is not None:
          self.world_position = world_position

    @property
    def spawn_point(self):
        """
        Gets the spawn_point of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        If we had map information, this spawnPoint would be interesting.  But sadly, we don't have that info.

        :return: The spawn_point of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :rtype: int
        """
        return self._spawn_point

    @spawn_point.setter
    def spawn_point(self, spawn_point):
        """
        Sets the spawn_point of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        If we had map information, this spawnPoint would be interesting.  But sadly, we don't have that info.

        :param spawn_point: The spawn_point of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :type: int
        """

        self._spawn_point = spawn_point

    @property
    def destination_hash(self):
        """
        Gets the destination_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        The Destination being pointed to by this location.

        :return: The destination_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :rtype: int
        """
        return self._destination_hash

    @destination_hash.setter
    def destination_hash(self, destination_hash):
        """
        Sets the destination_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        The Destination being pointed to by this location.

        :param destination_hash: The destination_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :type: int
        """

        self._destination_hash = destination_hash

    @property
    def activity_hash(self):
        """
        Gets the activity_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        The Activity being pointed to by this location.

        :return: The activity_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :rtype: int
        """
        return self._activity_hash

    @activity_hash.setter
    def activity_hash(self, activity_hash):
        """
        Sets the activity_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        The Activity being pointed to by this location.

        :param activity_hash: The activity_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :type: int
        """

        self._activity_hash = activity_hash

    @property
    def activity_graph_hash(self):
        """
        Gets the activity_graph_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        The Activity Graph being pointed to by this location.

        :return: The activity_graph_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :rtype: int
        """
        return self._activity_graph_hash

    @activity_graph_hash.setter
    def activity_graph_hash(self, activity_graph_hash):
        """
        Sets the activity_graph_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        The Activity Graph being pointed to by this location.

        :param activity_graph_hash: The activity_graph_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :type: int
        """

        self._activity_graph_hash = activity_graph_hash

    @property
    def activity_graph_node_hash(self):
        """
        Gets the activity_graph_node_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        The Activity Graph Node being pointed to by this location.  (Remember thatActivity Graph Node hashes are only unique within an Activity Graph: so use the combinationto find the node being spoken of)

        :return: The activity_graph_node_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :rtype: int
        """
        return self._activity_graph_node_hash

    @activity_graph_node_hash.setter
    def activity_graph_node_hash(self, activity_graph_node_hash):
        """
        Sets the activity_graph_node_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        The Activity Graph Node being pointed to by this location.  (Remember thatActivity Graph Node hashes are only unique within an Activity Graph: so use the combinationto find the node being spoken of)

        :param activity_graph_node_hash: The activity_graph_node_hash of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :type: int
        """

        self._activity_graph_node_hash = activity_graph_node_hash

    @property
    def activity_bubble_name(self):
        """
        Gets the activity_bubble_name of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        The Activity Bubble within the Destination.  Look this up in the DestinyDestinationDefinition'sbubbles and bubbleSettings properties.

        :return: The activity_bubble_name of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :rtype: int
        """
        return self._activity_bubble_name

    @activity_bubble_name.setter
    def activity_bubble_name(self, activity_bubble_name):
        """
        Sets the activity_bubble_name of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        The Activity Bubble within the Destination.  Look this up in the DestinyDestinationDefinition'sbubbles and bubbleSettings properties.

        :param activity_bubble_name: The activity_bubble_name of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :type: int
        """

        self._activity_bubble_name = activity_bubble_name

    @property
    def activity_path_bundle(self):
        """
        Gets the activity_path_bundle of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        If we had map information, this would tell us something cool about the path this location wantsyou to take.  I wish we had map information.

        :return: The activity_path_bundle of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :rtype: int
        """
        return self._activity_path_bundle

    @activity_path_bundle.setter
    def activity_path_bundle(self, activity_path_bundle):
        """
        Sets the activity_path_bundle of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        If we had map information, this would tell us something cool about the path this location wantsyou to take.  I wish we had map information.

        :param activity_path_bundle: The activity_path_bundle of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :type: int
        """

        self._activity_path_bundle = activity_path_bundle

    @property
    def activity_path_destination(self):
        """
        Gets the activity_path_destination of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        If we had map information, this would tell us about path information related to destinationon the map.  Sad.  Maybe you can do something cool with it.  Go to town man.

        :return: The activity_path_destination of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :rtype: int
        """
        return self._activity_path_destination

    @activity_path_destination.setter
    def activity_path_destination(self, activity_path_destination):
        """
        Sets the activity_path_destination of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        If we had map information, this would tell us about path information related to destinationon the map.  Sad.  Maybe you can do something cool with it.  Go to town man.

        :param activity_path_destination: The activity_path_destination of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :type: int
        """

        self._activity_path_destination = activity_path_destination

    @property
    def world_position(self):
        """
        Gets the world_position of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        Looks like it should be the position on the map, but sadly it does not look populated... yet?

        :return: The world_position of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :rtype: list[int]
        """
        return self._world_position

    @world_position.setter
    def world_position(self, world_position):
        """
        Sets the world_position of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        Looks like it should be the position on the map, but sadly it does not look populated... yet?

        :param world_position: The world_position of this DestinyDefinitionsDestinyLocationReleaseDefinition.
        :type: list[int]
        """

        self._world_position = world_position

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
        if not isinstance(other, DestinyDefinitionsDestinyLocationReleaseDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
