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


class DestinyDefinitionsDestinyTalentNodeStepGroups(object):
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
        'weapon_performance': 'ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepWeaponPerformances',
        'impact_effects': 'ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepImpactEffects',
        'guardian_attributes': 'ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepGuardianAttributes',
        'light_abilities': 'ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepLightAbilities',
        'damage_types': 'ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepDamageTypes'
    }

    attribute_map = {
        'weapon_performance': 'weaponPerformance',
        'impact_effects': 'impactEffects',
        'guardian_attributes': 'guardianAttributes',
        'light_abilities': 'lightAbilities',
        'damage_types': 'damageTypes'
    }

    def __init__(self, weapon_performance=None, impact_effects=None, guardian_attributes=None, light_abilities=None, damage_types=None):
        """
        DestinyDefinitionsDestinyTalentNodeStepGroups - a model defined in Swagger
        """

        self._weapon_performance = None
        self._impact_effects = None
        self._guardian_attributes = None
        self._light_abilities = None
        self._damage_types = None
        self.discriminator = None

        if weapon_performance is not None:
          self.weapon_performance = weapon_performance
        if impact_effects is not None:
          self.impact_effects = impact_effects
        if guardian_attributes is not None:
          self.guardian_attributes = guardian_attributes
        if light_abilities is not None:
          self.light_abilities = light_abilities
        if damage_types is not None:
          self.damage_types = damage_types

    @property
    def weapon_performance(self):
        """
        Gets the weapon_performance of this DestinyDefinitionsDestinyTalentNodeStepGroups.

        :return: The weapon_performance of this DestinyDefinitionsDestinyTalentNodeStepGroups.
        :rtype: ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepWeaponPerformances
        """
        return self._weapon_performance

    @weapon_performance.setter
    def weapon_performance(self, weapon_performance):
        """
        Sets the weapon_performance of this DestinyDefinitionsDestinyTalentNodeStepGroups.

        :param weapon_performance: The weapon_performance of this DestinyDefinitionsDestinyTalentNodeStepGroups.
        :type: ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepWeaponPerformances
        """

        self._weapon_performance = weapon_performance

    @property
    def impact_effects(self):
        """
        Gets the impact_effects of this DestinyDefinitionsDestinyTalentNodeStepGroups.

        :return: The impact_effects of this DestinyDefinitionsDestinyTalentNodeStepGroups.
        :rtype: ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepImpactEffects
        """
        return self._impact_effects

    @impact_effects.setter
    def impact_effects(self, impact_effects):
        """
        Sets the impact_effects of this DestinyDefinitionsDestinyTalentNodeStepGroups.

        :param impact_effects: The impact_effects of this DestinyDefinitionsDestinyTalentNodeStepGroups.
        :type: ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepImpactEffects
        """

        self._impact_effects = impact_effects

    @property
    def guardian_attributes(self):
        """
        Gets the guardian_attributes of this DestinyDefinitionsDestinyTalentNodeStepGroups.

        :return: The guardian_attributes of this DestinyDefinitionsDestinyTalentNodeStepGroups.
        :rtype: ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepGuardianAttributes
        """
        return self._guardian_attributes

    @guardian_attributes.setter
    def guardian_attributes(self, guardian_attributes):
        """
        Sets the guardian_attributes of this DestinyDefinitionsDestinyTalentNodeStepGroups.

        :param guardian_attributes: The guardian_attributes of this DestinyDefinitionsDestinyTalentNodeStepGroups.
        :type: ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepGuardianAttributes
        """

        self._guardian_attributes = guardian_attributes

    @property
    def light_abilities(self):
        """
        Gets the light_abilities of this DestinyDefinitionsDestinyTalentNodeStepGroups.

        :return: The light_abilities of this DestinyDefinitionsDestinyTalentNodeStepGroups.
        :rtype: ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepLightAbilities
        """
        return self._light_abilities

    @light_abilities.setter
    def light_abilities(self, light_abilities):
        """
        Sets the light_abilities of this DestinyDefinitionsDestinyTalentNodeStepGroups.

        :param light_abilities: The light_abilities of this DestinyDefinitionsDestinyTalentNodeStepGroups.
        :type: ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepLightAbilities
        """

        self._light_abilities = light_abilities

    @property
    def damage_types(self):
        """
        Gets the damage_types of this DestinyDefinitionsDestinyTalentNodeStepGroups.

        :return: The damage_types of this DestinyDefinitionsDestinyTalentNodeStepGroups.
        :rtype: ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepDamageTypes
        """
        return self._damage_types

    @damage_types.setter
    def damage_types(self, damage_types):
        """
        Sets the damage_types of this DestinyDefinitionsDestinyTalentNodeStepGroups.

        :param damage_types: The damage_types of this DestinyDefinitionsDestinyTalentNodeStepGroups.
        :type: ComponentsschemasDestinyDefinitionsDestinyTalentNodeStepDamageTypes
        """

        self._damage_types = damage_types

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
        if not isinstance(other, DestinyDefinitionsDestinyTalentNodeStepGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
