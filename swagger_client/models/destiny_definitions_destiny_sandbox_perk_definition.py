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


class DestinyDefinitionsDestinySandboxPerkDefinition(object):
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
        'perk_identifier': 'str',
        'is_displayable': 'bool',
        'damage_type_hash': 'int',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'perk_identifier': 'perkIdentifier',
        'is_displayable': 'isDisplayable',
        'damage_type_hash': 'damageTypeHash',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, perk_identifier=None, is_displayable=None, damage_type_hash=None, hash=None, index=None, redacted=None):
        """
        DestinyDefinitionsDestinySandboxPerkDefinition - a model defined in Swagger
        """

        self._perk_identifier = None
        self._is_displayable = None
        self._damage_type_hash = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if perk_identifier is not None:
          self.perk_identifier = perk_identifier
        if is_displayable is not None:
          self.is_displayable = is_displayable
        if damage_type_hash is not None:
          self.damage_type_hash = damage_type_hash
        if hash is not None:
          self.hash = hash
        if index is not None:
          self.index = index
        if redacted is not None:
          self.redacted = redacted

    @property
    def perk_identifier(self):
        """
        Gets the perk_identifier of this DestinyDefinitionsDestinySandboxPerkDefinition.
        The string identifier for the perk.

        :return: The perk_identifier of this DestinyDefinitionsDestinySandboxPerkDefinition.
        :rtype: str
        """
        return self._perk_identifier

    @perk_identifier.setter
    def perk_identifier(self, perk_identifier):
        """
        Sets the perk_identifier of this DestinyDefinitionsDestinySandboxPerkDefinition.
        The string identifier for the perk.

        :param perk_identifier: The perk_identifier of this DestinyDefinitionsDestinySandboxPerkDefinition.
        :type: str
        """

        self._perk_identifier = perk_identifier

    @property
    def is_displayable(self):
        """
        Gets the is_displayable of this DestinyDefinitionsDestinySandboxPerkDefinition.
        If true, you can actually show the perk in the UI.  Otherwise, it doesn'thave useful player-facing information.

        :return: The is_displayable of this DestinyDefinitionsDestinySandboxPerkDefinition.
        :rtype: bool
        """
        return self._is_displayable

    @is_displayable.setter
    def is_displayable(self, is_displayable):
        """
        Sets the is_displayable of this DestinyDefinitionsDestinySandboxPerkDefinition.
        If true, you can actually show the perk in the UI.  Otherwise, it doesn'thave useful player-facing information.

        :param is_displayable: The is_displayable of this DestinyDefinitionsDestinySandboxPerkDefinition.
        :type: bool
        """

        self._is_displayable = is_displayable

    @property
    def damage_type_hash(self):
        """
        Gets the damage_type_hash of this DestinyDefinitionsDestinySandboxPerkDefinition.
        The hash identifier for looking up the DestinyDamageTypeDefinition, if this perk has a damage type.  This is preferred over using the damageType enumeration value, which has been left purely because it isoccasionally convenient.

        :return: The damage_type_hash of this DestinyDefinitionsDestinySandboxPerkDefinition.
        :rtype: int
        """
        return self._damage_type_hash

    @damage_type_hash.setter
    def damage_type_hash(self, damage_type_hash):
        """
        Sets the damage_type_hash of this DestinyDefinitionsDestinySandboxPerkDefinition.
        The hash identifier for looking up the DestinyDamageTypeDefinition, if this perk has a damage type.  This is preferred over using the damageType enumeration value, which has been left purely because it isoccasionally convenient.

        :param damage_type_hash: The damage_type_hash of this DestinyDefinitionsDestinySandboxPerkDefinition.
        :type: int
        """

        self._damage_type_hash = damage_type_hash

    @property
    def hash(self):
        """
        Gets the hash of this DestinyDefinitionsDestinySandboxPerkDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :return: The hash of this DestinyDefinitionsDestinySandboxPerkDefinition.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this DestinyDefinitionsDestinySandboxPerkDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :param hash: The hash of this DestinyDefinitionsDestinySandboxPerkDefinition.
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """
        Gets the index of this DestinyDefinitionsDestinySandboxPerkDefinition.
        The index of the entity as it was found in the investment tables.

        :return: The index of this DestinyDefinitionsDestinySandboxPerkDefinition.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this DestinyDefinitionsDestinySandboxPerkDefinition.
        The index of the entity as it was found in the investment tables.

        :param index: The index of this DestinyDefinitionsDestinySandboxPerkDefinition.
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """
        Gets the redacted of this DestinyDefinitionsDestinySandboxPerkDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :return: The redacted of this DestinyDefinitionsDestinySandboxPerkDefinition.
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """
        Sets the redacted of this DestinyDefinitionsDestinySandboxPerkDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :param redacted: The redacted of this DestinyDefinitionsDestinySandboxPerkDefinition.
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
        if not isinstance(other, DestinyDefinitionsDestinySandboxPerkDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
