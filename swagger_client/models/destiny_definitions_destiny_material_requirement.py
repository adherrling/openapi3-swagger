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


class DestinyDefinitionsDestinyMaterialRequirement(object):
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
        'item_hash': 'int',
        'delete_on_action': 'bool',
        'count': 'int',
        'omit_from_requirements': 'bool'
    }

    attribute_map = {
        'item_hash': 'itemHash',
        'delete_on_action': 'deleteOnAction',
        'count': 'count',
        'omit_from_requirements': 'omitFromRequirements'
    }

    def __init__(self, item_hash=None, delete_on_action=None, count=None, omit_from_requirements=None):
        """
        DestinyDefinitionsDestinyMaterialRequirement - a model defined in Swagger
        """

        self._item_hash = None
        self._delete_on_action = None
        self._count = None
        self._omit_from_requirements = None
        self.discriminator = None

        if item_hash is not None:
          self.item_hash = item_hash
        if delete_on_action is not None:
          self.delete_on_action = delete_on_action
        if count is not None:
          self.count = count
        if omit_from_requirements is not None:
          self.omit_from_requirements = omit_from_requirements

    @property
    def item_hash(self):
        """
        Gets the item_hash of this DestinyDefinitionsDestinyMaterialRequirement.
        The hash identifier of the material required.  Use it to look up the material's DestinyInventoryItemDefinition.

        :return: The item_hash of this DestinyDefinitionsDestinyMaterialRequirement.
        :rtype: int
        """
        return self._item_hash

    @item_hash.setter
    def item_hash(self, item_hash):
        """
        Sets the item_hash of this DestinyDefinitionsDestinyMaterialRequirement.
        The hash identifier of the material required.  Use it to look up the material's DestinyInventoryItemDefinition.

        :param item_hash: The item_hash of this DestinyDefinitionsDestinyMaterialRequirement.
        :type: int
        """

        self._item_hash = item_hash

    @property
    def delete_on_action(self):
        """
        Gets the delete_on_action of this DestinyDefinitionsDestinyMaterialRequirement.
        If True, the material will be removed from the character's inventory when the action is performed.

        :return: The delete_on_action of this DestinyDefinitionsDestinyMaterialRequirement.
        :rtype: bool
        """
        return self._delete_on_action

    @delete_on_action.setter
    def delete_on_action(self, delete_on_action):
        """
        Sets the delete_on_action of this DestinyDefinitionsDestinyMaterialRequirement.
        If True, the material will be removed from the character's inventory when the action is performed.

        :param delete_on_action: The delete_on_action of this DestinyDefinitionsDestinyMaterialRequirement.
        :type: bool
        """

        self._delete_on_action = delete_on_action

    @property
    def count(self):
        """
        Gets the count of this DestinyDefinitionsDestinyMaterialRequirement.
        The amount of the material required.

        :return: The count of this DestinyDefinitionsDestinyMaterialRequirement.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this DestinyDefinitionsDestinyMaterialRequirement.
        The amount of the material required.

        :param count: The count of this DestinyDefinitionsDestinyMaterialRequirement.
        :type: int
        """

        self._count = count

    @property
    def omit_from_requirements(self):
        """
        Gets the omit_from_requirements of this DestinyDefinitionsDestinyMaterialRequirement.
        If True, this requirement is \"silent\": don't bother showing it in a material requirements display.I mean, I'm not your mom: I'm not going to tell you you *can't* show it.  But we won't show it in our UI.

        :return: The omit_from_requirements of this DestinyDefinitionsDestinyMaterialRequirement.
        :rtype: bool
        """
        return self._omit_from_requirements

    @omit_from_requirements.setter
    def omit_from_requirements(self, omit_from_requirements):
        """
        Sets the omit_from_requirements of this DestinyDefinitionsDestinyMaterialRequirement.
        If True, this requirement is \"silent\": don't bother showing it in a material requirements display.I mean, I'm not your mom: I'm not going to tell you you *can't* show it.  But we won't show it in our UI.

        :param omit_from_requirements: The omit_from_requirements of this DestinyDefinitionsDestinyMaterialRequirement.
        :type: bool
        """

        self._omit_from_requirements = omit_from_requirements

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
        if not isinstance(other, DestinyDefinitionsDestinyMaterialRequirement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
