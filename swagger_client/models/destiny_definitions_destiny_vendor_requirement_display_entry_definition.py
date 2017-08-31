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


class DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition(object):
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
        'icon': 'str',
        'name': 'str',
        'source': 'str',
        'type': 'str'
    }

    attribute_map = {
        'icon': 'icon',
        'name': 'name',
        'source': 'source',
        'type': 'type'
    }

    def __init__(self, icon=None, name=None, source=None, type=None):
        """
        DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition - a model defined in Swagger
        """

        self._icon = None
        self._name = None
        self._source = None
        self._type = None
        self.discriminator = None

        if icon is not None:
          self.icon = icon
        if name is not None:
          self.name = name
        if source is not None:
          self.source = source
        if type is not None:
          self.type = type

    @property
    def icon(self):
        """
        Gets the icon of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.

        :return: The icon of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.

        :param icon: The icon of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.
        :type: str
        """

        self._icon = icon

    @property
    def name(self):
        """
        Gets the name of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.

        :return: The name of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.

        :param name: The name of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.
        :type: str
        """

        self._name = name

    @property
    def source(self):
        """
        Gets the source of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.

        :return: The source of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.

        :param source: The source of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.
        :type: str
        """

        self._source = source

    @property
    def type(self):
        """
        Gets the type of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.

        :return: The type of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.

        :param type: The type of this DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other