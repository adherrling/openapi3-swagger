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


class DestinyDefinitionsDestinyItemSummaryBlockDefinition(object):
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
        'sort_priority': 'int'
    }

    attribute_map = {
        'sort_priority': 'sortPriority'
    }

    def __init__(self, sort_priority=None):
        """
        DestinyDefinitionsDestinyItemSummaryBlockDefinition - a model defined in Swagger
        """

        self._sort_priority = None
        self.discriminator = None

        if sort_priority is not None:
          self.sort_priority = sort_priority

    @property
    def sort_priority(self):
        """
        Gets the sort_priority of this DestinyDefinitionsDestinyItemSummaryBlockDefinition.
        Apparently when rendering an item in a reward, this should be used as a sort priority.We're not doing it presently.

        :return: The sort_priority of this DestinyDefinitionsDestinyItemSummaryBlockDefinition.
        :rtype: int
        """
        return self._sort_priority

    @sort_priority.setter
    def sort_priority(self, sort_priority):
        """
        Sets the sort_priority of this DestinyDefinitionsDestinyItemSummaryBlockDefinition.
        Apparently when rendering an item in a reward, this should be used as a sort priority.We're not doing it presently.

        :param sort_priority: The sort_priority of this DestinyDefinitionsDestinyItemSummaryBlockDefinition.
        :type: int
        """

        self._sort_priority = sort_priority

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
        if not isinstance(other, DestinyDefinitionsDestinyItemSummaryBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
