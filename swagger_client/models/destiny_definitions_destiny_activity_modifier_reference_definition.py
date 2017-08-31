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


class DestinyDefinitionsDestinyActivityModifierReferenceDefinition(object):
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
        'activity_modifier_hash': 'int'
    }

    attribute_map = {
        'activity_modifier_hash': 'activityModifierHash'
    }

    def __init__(self, activity_modifier_hash=None):
        """
        DestinyDefinitionsDestinyActivityModifierReferenceDefinition - a model defined in Swagger
        """

        self._activity_modifier_hash = None
        self.discriminator = None

        if activity_modifier_hash is not None:
          self.activity_modifier_hash = activity_modifier_hash

    @property
    def activity_modifier_hash(self):
        """
        Gets the activity_modifier_hash of this DestinyDefinitionsDestinyActivityModifierReferenceDefinition.
        The hash identifier for the DestinyActivityModifierDefinition referenced by this activity.

        :return: The activity_modifier_hash of this DestinyDefinitionsDestinyActivityModifierReferenceDefinition.
        :rtype: int
        """
        return self._activity_modifier_hash

    @activity_modifier_hash.setter
    def activity_modifier_hash(self, activity_modifier_hash):
        """
        Sets the activity_modifier_hash of this DestinyDefinitionsDestinyActivityModifierReferenceDefinition.
        The hash identifier for the DestinyActivityModifierDefinition referenced by this activity.

        :param activity_modifier_hash: The activity_modifier_hash of this DestinyDefinitionsDestinyActivityModifierReferenceDefinition.
        :type: int
        """

        self._activity_modifier_hash = activity_modifier_hash

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
        if not isinstance(other, DestinyDefinitionsDestinyActivityModifierReferenceDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
