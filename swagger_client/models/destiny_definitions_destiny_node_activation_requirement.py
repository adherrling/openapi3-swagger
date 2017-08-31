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


class DestinyDefinitionsDestinyNodeActivationRequirement(object):
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
        'grid_level': 'int',
        'material_requirement_hashes': 'list[int]'
    }

    attribute_map = {
        'grid_level': 'gridLevel',
        'material_requirement_hashes': 'materialRequirementHashes'
    }

    def __init__(self, grid_level=None, material_requirement_hashes=None):
        """
        DestinyDefinitionsDestinyNodeActivationRequirement - a model defined in Swagger
        """

        self._grid_level = None
        self._material_requirement_hashes = None
        self.discriminator = None

        if grid_level is not None:
          self.grid_level = grid_level
        if material_requirement_hashes is not None:
          self.material_requirement_hashes = material_requirement_hashes

    @property
    def grid_level(self):
        """
        Gets the grid_level of this DestinyDefinitionsDestinyNodeActivationRequirement.
        The Progression level on the Talent Grid required to activate this node.  See DestinyTalentGridDefinition.progressionHash for the related Progression, and readDestinyProgressionDefinition's documentation to learn more about Progressions.

        :return: The grid_level of this DestinyDefinitionsDestinyNodeActivationRequirement.
        :rtype: int
        """
        return self._grid_level

    @grid_level.setter
    def grid_level(self, grid_level):
        """
        Sets the grid_level of this DestinyDefinitionsDestinyNodeActivationRequirement.
        The Progression level on the Talent Grid required to activate this node.  See DestinyTalentGridDefinition.progressionHash for the related Progression, and readDestinyProgressionDefinition's documentation to learn more about Progressions.

        :param grid_level: The grid_level of this DestinyDefinitionsDestinyNodeActivationRequirement.
        :type: int
        """

        self._grid_level = grid_level

    @property
    def material_requirement_hashes(self):
        """
        Gets the material_requirement_hashes of this DestinyDefinitionsDestinyNodeActivationRequirement.
        The list of hash identifiers for material requirement sets: materials thatare required for the node to be activated.  See DestinyMaterialRequirementSetDefinition formore information about material requirements.  In this case, only a single DestinyMaterialRequirementSetDefinition will be chosenfrom this list, and we won't know which one will be chosen until an instance of the item is created.

        :return: The material_requirement_hashes of this DestinyDefinitionsDestinyNodeActivationRequirement.
        :rtype: list[int]
        """
        return self._material_requirement_hashes

    @material_requirement_hashes.setter
    def material_requirement_hashes(self, material_requirement_hashes):
        """
        Sets the material_requirement_hashes of this DestinyDefinitionsDestinyNodeActivationRequirement.
        The list of hash identifiers for material requirement sets: materials thatare required for the node to be activated.  See DestinyMaterialRequirementSetDefinition formore information about material requirements.  In this case, only a single DestinyMaterialRequirementSetDefinition will be chosenfrom this list, and we won't know which one will be chosen until an instance of the item is created.

        :param material_requirement_hashes: The material_requirement_hashes of this DestinyDefinitionsDestinyNodeActivationRequirement.
        :type: list[int]
        """

        self._material_requirement_hashes = material_requirement_hashes

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
        if not isinstance(other, DestinyDefinitionsDestinyNodeActivationRequirement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
