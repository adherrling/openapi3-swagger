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


class DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition(object):
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
        'node_activity_id': 'int',
        'activity_hash': 'int'
    }

    attribute_map = {
        'node_activity_id': 'nodeActivityId',
        'activity_hash': 'activityHash'
    }

    def __init__(self, node_activity_id=None, activity_hash=None):
        """
        DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition - a model defined in Swagger
        """

        self._node_activity_id = None
        self._activity_hash = None
        self.discriminator = None

        if node_activity_id is not None:
          self.node_activity_id = node_activity_id
        if activity_hash is not None:
          self.activity_hash = activity_hash

    @property
    def node_activity_id(self):
        """
        Gets the node_activity_id of this DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition.
        An identifier for this node activity.  It is only guaranteed to be unique within the Activity Graph.

        :return: The node_activity_id of this DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition.
        :rtype: int
        """
        return self._node_activity_id

    @node_activity_id.setter
    def node_activity_id(self, node_activity_id):
        """
        Sets the node_activity_id of this DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition.
        An identifier for this node activity.  It is only guaranteed to be unique within the Activity Graph.

        :param node_activity_id: The node_activity_id of this DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition.
        :type: int
        """

        self._node_activity_id = node_activity_id

    @property
    def activity_hash(self):
        """
        Gets the activity_hash of this DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition.
        The activity that will be activated if the user clicks on this node.  Controls all activity-relatedinformation displayed on the node if it is active (the text shown in the tooltip etc)

        :return: The activity_hash of this DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition.
        :rtype: int
        """
        return self._activity_hash

    @activity_hash.setter
    def activity_hash(self, activity_hash):
        """
        Sets the activity_hash of this DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition.
        The activity that will be activated if the user clicks on this node.  Controls all activity-relatedinformation displayed on the node if it is active (the text shown in the tooltip etc)

        :param activity_hash: The activity_hash of this DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition.
        :type: int
        """

        self._activity_hash = activity_hash

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
        if not isinstance(other, DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
