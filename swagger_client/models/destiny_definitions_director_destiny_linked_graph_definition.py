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


class DestinyDefinitionsDirectorDestinyLinkedGraphDefinition(object):
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
        'description': 'str',
        'name': 'str',
        'unlock_expression': 'ComponentsschemasDestinyDefinitionsDestinyUnlockExpressionDefinition',
        'linked_graph_id': 'int',
        'linked_graphs': 'list[ComponentsschemasDestinyDefinitionsDirectorDestinyLinkedGraphEntryDefinition]',
        'overview': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'unlock_expression': 'unlockExpression',
        'linked_graph_id': 'linkedGraphId',
        'linked_graphs': 'linkedGraphs',
        'overview': 'overview'
    }

    def __init__(self, description=None, name=None, unlock_expression=None, linked_graph_id=None, linked_graphs=None, overview=None):
        """
        DestinyDefinitionsDirectorDestinyLinkedGraphDefinition - a model defined in Swagger
        """

        self._description = None
        self._name = None
        self._unlock_expression = None
        self._linked_graph_id = None
        self._linked_graphs = None
        self._overview = None
        self.discriminator = None

        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if unlock_expression is not None:
          self.unlock_expression = unlock_expression
        if linked_graph_id is not None:
          self.linked_graph_id = linked_graph_id
        if linked_graphs is not None:
          self.linked_graphs = linked_graphs
        if overview is not None:
          self.overview = overview

    @property
    def description(self):
        """
        Gets the description of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :return: The description of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :param description: The description of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :return: The name of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :param name: The name of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :type: str
        """

        self._name = name

    @property
    def unlock_expression(self):
        """
        Gets the unlock_expression of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :return: The unlock_expression of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :rtype: ComponentsschemasDestinyDefinitionsDestinyUnlockExpressionDefinition
        """
        return self._unlock_expression

    @unlock_expression.setter
    def unlock_expression(self, unlock_expression):
        """
        Sets the unlock_expression of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :param unlock_expression: The unlock_expression of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :type: ComponentsschemasDestinyDefinitionsDestinyUnlockExpressionDefinition
        """

        self._unlock_expression = unlock_expression

    @property
    def linked_graph_id(self):
        """
        Gets the linked_graph_id of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :return: The linked_graph_id of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :rtype: int
        """
        return self._linked_graph_id

    @linked_graph_id.setter
    def linked_graph_id(self, linked_graph_id):
        """
        Sets the linked_graph_id of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :param linked_graph_id: The linked_graph_id of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :type: int
        """

        self._linked_graph_id = linked_graph_id

    @property
    def linked_graphs(self):
        """
        Gets the linked_graphs of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :return: The linked_graphs of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDirectorDestinyLinkedGraphEntryDefinition]
        """
        return self._linked_graphs

    @linked_graphs.setter
    def linked_graphs(self, linked_graphs):
        """
        Sets the linked_graphs of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :param linked_graphs: The linked_graphs of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDirectorDestinyLinkedGraphEntryDefinition]
        """

        self._linked_graphs = linked_graphs

    @property
    def overview(self):
        """
        Gets the overview of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :return: The overview of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :rtype: str
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """
        Sets the overview of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.

        :param overview: The overview of this DestinyDefinitionsDirectorDestinyLinkedGraphDefinition.
        :type: str
        """

        self._overview = overview

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
        if not isinstance(other, DestinyDefinitionsDirectorDestinyLinkedGraphDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
