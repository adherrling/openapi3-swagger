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


class DestinyDefinitionsDirectorDestinyActivityGraphDefinition(object):
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
        'nodes': 'list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition]',
        'art_elements': 'list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphArtElementDefinition]',
        'connections': 'list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphConnectionDefinition]',
        'display_objectives': 'list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition]',
        'display_progressions': 'list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphDisplayProgressionDefinition]',
        'linked_graphs': 'list[ComponentsschemasDestinyDefinitionsDirectorDestinyLinkedGraphDefinition]',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'nodes': 'nodes',
        'art_elements': 'artElements',
        'connections': 'connections',
        'display_objectives': 'displayObjectives',
        'display_progressions': 'displayProgressions',
        'linked_graphs': 'linkedGraphs',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, nodes=None, art_elements=None, connections=None, display_objectives=None, display_progressions=None, linked_graphs=None, hash=None, index=None, redacted=None):
        """
        DestinyDefinitionsDirectorDestinyActivityGraphDefinition - a model defined in Swagger
        """

        self._nodes = None
        self._art_elements = None
        self._connections = None
        self._display_objectives = None
        self._display_progressions = None
        self._linked_graphs = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if nodes is not None:
          self.nodes = nodes
        if art_elements is not None:
          self.art_elements = art_elements
        if connections is not None:
          self.connections = connections
        if display_objectives is not None:
          self.display_objectives = display_objectives
        if display_progressions is not None:
          self.display_progressions = display_progressions
        if linked_graphs is not None:
          self.linked_graphs = linked_graphs
        if hash is not None:
          self.hash = hash
        if index is not None:
          self.index = index
        if redacted is not None:
          self.redacted = redacted

    @property
    def nodes(self):
        """
        Gets the nodes of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        These represent the visual \"nodes\" on the map's view.  These are the activities youcan click on in the map.

        :return: The nodes of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        These represent the visual \"nodes\" on the map's view.  These are the activities youcan click on in the map.

        :param nodes: The nodes of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition]
        """

        self._nodes = nodes

    @property
    def art_elements(self):
        """
        Gets the art_elements of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        Represents one-off/special UI elements that appear on the map.

        :return: The art_elements of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphArtElementDefinition]
        """
        return self._art_elements

    @art_elements.setter
    def art_elements(self, art_elements):
        """
        Sets the art_elements of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        Represents one-off/special UI elements that appear on the map.

        :param art_elements: The art_elements of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphArtElementDefinition]
        """

        self._art_elements = art_elements

    @property
    def connections(self):
        """
        Gets the connections of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        Represents connections between graph nodes.  However, it lacks context that we'd need to make good use of it.

        :return: The connections of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphConnectionDefinition]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """
        Sets the connections of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        Represents connections between graph nodes.  However, it lacks context that we'd need to make good use of it.

        :param connections: The connections of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphConnectionDefinition]
        """

        self._connections = connections

    @property
    def display_objectives(self):
        """
        Gets the display_objectives of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        Objectives can display on maps, and this is supposedly metadata for that.  I have not had the time toanalyze the details of what is useful within however: we could be missing important data to make this work.Expect this property to be expanded on later if possible.

        :return: The display_objectives of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition]
        """
        return self._display_objectives

    @display_objectives.setter
    def display_objectives(self, display_objectives):
        """
        Sets the display_objectives of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        Objectives can display on maps, and this is supposedly metadata for that.  I have not had the time toanalyze the details of what is useful within however: we could be missing important data to make this work.Expect this property to be expanded on later if possible.

        :param display_objectives: The display_objectives of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition]
        """

        self._display_objectives = display_objectives

    @property
    def display_progressions(self):
        """
        Gets the display_progressions of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        Progressions can also display on maps, but similarly to displayObjectives we appear to lack some requiredinformation and context right now.  We will have to look into it later and add more data if possible.

        :return: The display_progressions of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphDisplayProgressionDefinition]
        """
        return self._display_progressions

    @display_progressions.setter
    def display_progressions(self, display_progressions):
        """
        Sets the display_progressions of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        Progressions can also display on maps, but similarly to displayObjectives we appear to lack some requiredinformation and context right now.  We will have to look into it later and add more data if possible.

        :param display_progressions: The display_progressions of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDirectorDestinyActivityGraphDisplayProgressionDefinition]
        """

        self._display_progressions = display_progressions

    @property
    def linked_graphs(self):
        """
        Gets the linked_graphs of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        Represents links between this Activity Graph and other ones.

        :return: The linked_graphs of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDirectorDestinyLinkedGraphDefinition]
        """
        return self._linked_graphs

    @linked_graphs.setter
    def linked_graphs(self, linked_graphs):
        """
        Sets the linked_graphs of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        Represents links between this Activity Graph and other ones.

        :param linked_graphs: The linked_graphs of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDirectorDestinyLinkedGraphDefinition]
        """

        self._linked_graphs = linked_graphs

    @property
    def hash(self):
        """
        Gets the hash of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :return: The hash of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :param hash: The hash of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """
        Gets the index of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        The index of the entity as it was found in the investment tables.

        :return: The index of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        The index of the entity as it was found in the investment tables.

        :param index: The index of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """
        Gets the redacted of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :return: The redacted of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """
        Sets the redacted of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :param redacted: The redacted of this DestinyDefinitionsDirectorDestinyActivityGraphDefinition.
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
        if not isinstance(other, DestinyDefinitionsDirectorDestinyActivityGraphDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
