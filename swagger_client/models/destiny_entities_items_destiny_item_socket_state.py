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


class DestinyEntitiesItemsDestinyItemSocketState(object):
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
        'plug_hash': 'int',
        'is_enabled': 'bool',
        'enable_fail_indexes': 'list[int]',
        'reusable_plug_hashes': 'list[int]'
    }

    attribute_map = {
        'plug_hash': 'plugHash',
        'is_enabled': 'isEnabled',
        'enable_fail_indexes': 'enableFailIndexes',
        'reusable_plug_hashes': 'reusablePlugHashes'
    }

    def __init__(self, plug_hash=None, is_enabled=None, enable_fail_indexes=None, reusable_plug_hashes=None):
        """
        DestinyEntitiesItemsDestinyItemSocketState - a model defined in Swagger
        """

        self._plug_hash = None
        self._is_enabled = None
        self._enable_fail_indexes = None
        self._reusable_plug_hashes = None
        self.discriminator = None

        if plug_hash is not None:
          self.plug_hash = plug_hash
        if is_enabled is not None:
          self.is_enabled = is_enabled
        if enable_fail_indexes is not None:
          self.enable_fail_indexes = enable_fail_indexes
        if reusable_plug_hashes is not None:
          self.reusable_plug_hashes = reusable_plug_hashes

    @property
    def plug_hash(self):
        """
        Gets the plug_hash of this DestinyEntitiesItemsDestinyItemSocketState.
        The currently active plug, if any.  Note that, because all plugs are statically defined, its effect on stats and perks can bestatically determined using the plug item's definition.  The stats and perks can be taken at facevalue on the plug item as the stats and perks it will provide to the user/item.

        :return: The plug_hash of this DestinyEntitiesItemsDestinyItemSocketState.
        :rtype: int
        """
        return self._plug_hash

    @plug_hash.setter
    def plug_hash(self, plug_hash):
        """
        Sets the plug_hash of this DestinyEntitiesItemsDestinyItemSocketState.
        The currently active plug, if any.  Note that, because all plugs are statically defined, its effect on stats and perks can bestatically determined using the plug item's definition.  The stats and perks can be taken at facevalue on the plug item as the stats and perks it will provide to the user/item.

        :param plug_hash: The plug_hash of this DestinyEntitiesItemsDestinyItemSocketState.
        :type: int
        """

        self._plug_hash = plug_hash

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this DestinyEntitiesItemsDestinyItemSocketState.
        Even if a plug is inserted, it doesn't mean it's enabled.  This flag indicates whether the plug is active and providing its benefits.

        :return: The is_enabled of this DestinyEntitiesItemsDestinyItemSocketState.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this DestinyEntitiesItemsDestinyItemSocketState.
        Even if a plug is inserted, it doesn't mean it's enabled.  This flag indicates whether the plug is active and providing its benefits.

        :param is_enabled: The is_enabled of this DestinyEntitiesItemsDestinyItemSocketState.
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def enable_fail_indexes(self):
        """
        Gets the enable_fail_indexes of this DestinyEntitiesItemsDestinyItemSocketState.
        If a plug is inserted but not enabled, this will be populated with indexes into the plug item definition's plug.enabledRulesproperty, so that you can show the reasons why it is not enabled.

        :return: The enable_fail_indexes of this DestinyEntitiesItemsDestinyItemSocketState.
        :rtype: list[int]
        """
        return self._enable_fail_indexes

    @enable_fail_indexes.setter
    def enable_fail_indexes(self, enable_fail_indexes):
        """
        Sets the enable_fail_indexes of this DestinyEntitiesItemsDestinyItemSocketState.
        If a plug is inserted but not enabled, this will be populated with indexes into the plug item definition's plug.enabledRulesproperty, so that you can show the reasons why it is not enabled.

        :param enable_fail_indexes: The enable_fail_indexes of this DestinyEntitiesItemsDestinyItemSocketState.
        :type: list[int]
        """

        self._enable_fail_indexes = enable_fail_indexes

    @property
    def reusable_plug_hashes(self):
        """
        Gets the reusable_plug_hashes of this DestinyEntitiesItemsDestinyItemSocketState.
        If the item supports reusable plugs, this is the list of plug item hashes that are currentlyallowed to be used for this socket.  (sometimes restrictions may cause reusable plugs defined on the item definition to not be valid, so you should trust the instanced reusablePlugHashes listrather than the definition's list)  A Reusable Plug is a plug that you can *always* insert into this socket, regardless of whether or notyou have the plug in your inventory.  In practice, a socket will *either* have reusable plugs *or*it will allow for plugs in your inventory to be inserted.  See DestinyInventoryItemDefinition.socketfor more info.

        :return: The reusable_plug_hashes of this DestinyEntitiesItemsDestinyItemSocketState.
        :rtype: list[int]
        """
        return self._reusable_plug_hashes

    @reusable_plug_hashes.setter
    def reusable_plug_hashes(self, reusable_plug_hashes):
        """
        Sets the reusable_plug_hashes of this DestinyEntitiesItemsDestinyItemSocketState.
        If the item supports reusable plugs, this is the list of plug item hashes that are currentlyallowed to be used for this socket.  (sometimes restrictions may cause reusable plugs defined on the item definition to not be valid, so you should trust the instanced reusablePlugHashes listrather than the definition's list)  A Reusable Plug is a plug that you can *always* insert into this socket, regardless of whether or notyou have the plug in your inventory.  In practice, a socket will *either* have reusable plugs *or*it will allow for plugs in your inventory to be inserted.  See DestinyInventoryItemDefinition.socketfor more info.

        :param reusable_plug_hashes: The reusable_plug_hashes of this DestinyEntitiesItemsDestinyItemSocketState.
        :type: list[int]
        """

        self._reusable_plug_hashes = reusable_plug_hashes

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
        if not isinstance(other, DestinyEntitiesItemsDestinyItemSocketState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
