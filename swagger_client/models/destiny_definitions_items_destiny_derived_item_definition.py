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


class DestinyDefinitionsItemsDestinyDerivedItemDefinition(object):
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
        'item_name': 'str',
        'item_detail': 'str',
        'item_description': 'str',
        'icon_path': 'str',
        'vendor_item_index': 'int'
    }

    attribute_map = {
        'item_hash': 'itemHash',
        'item_name': 'itemName',
        'item_detail': 'itemDetail',
        'item_description': 'itemDescription',
        'icon_path': 'iconPath',
        'vendor_item_index': 'vendorItemIndex'
    }

    def __init__(self, item_hash=None, item_name=None, item_detail=None, item_description=None, icon_path=None, vendor_item_index=None):
        """
        DestinyDefinitionsItemsDestinyDerivedItemDefinition - a model defined in Swagger
        """

        self._item_hash = None
        self._item_name = None
        self._item_detail = None
        self._item_description = None
        self._icon_path = None
        self._vendor_item_index = None
        self.discriminator = None

        if item_hash is not None:
          self.item_hash = item_hash
        if item_name is not None:
          self.item_name = item_name
        if item_detail is not None:
          self.item_detail = item_detail
        if item_description is not None:
          self.item_description = item_description
        if icon_path is not None:
          self.icon_path = icon_path
        if vendor_item_index is not None:
          self.vendor_item_index = vendor_item_index

    @property
    def item_hash(self):
        """
        Gets the item_hash of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        The hash for the DestinyInventoryItemDefinition of this derived item, if there is one.Sometimes we are given this information as a manual override, in which case there won't bean actual DestinyInventoryItemDefinition for what we display, but you can still show the stringsfrom this object itself.

        :return: The item_hash of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :rtype: int
        """
        return self._item_hash

    @item_hash.setter
    def item_hash(self, item_hash):
        """
        Sets the item_hash of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        The hash for the DestinyInventoryItemDefinition of this derived item, if there is one.Sometimes we are given this information as a manual override, in which case there won't bean actual DestinyInventoryItemDefinition for what we display, but you can still show the stringsfrom this object itself.

        :param item_hash: The item_hash of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :type: int
        """

        self._item_hash = item_hash

    @property
    def item_name(self):
        """
        Gets the item_name of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        The name of the derived item.

        :return: The item_name of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """
        Sets the item_name of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        The name of the derived item.

        :param item_name: The item_name of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :type: str
        """

        self._item_name = item_name

    @property
    def item_detail(self):
        """
        Gets the item_detail of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        Additional details about the derived item, in addition to the description.

        :return: The item_detail of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :rtype: str
        """
        return self._item_detail

    @item_detail.setter
    def item_detail(self, item_detail):
        """
        Sets the item_detail of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        Additional details about the derived item, in addition to the description.

        :param item_detail: The item_detail of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :type: str
        """

        self._item_detail = item_detail

    @property
    def item_description(self):
        """
        Gets the item_description of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        A brief description of the item.

        :return: The item_description of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :rtype: str
        """
        return self._item_description

    @item_description.setter
    def item_description(self, item_description):
        """
        Sets the item_description of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        A brief description of the item.

        :param item_description: The item_description of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :type: str
        """

        self._item_description = item_description

    @property
    def icon_path(self):
        """
        Gets the icon_path of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        An icon for the item.

        :return: The icon_path of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :rtype: str
        """
        return self._icon_path

    @icon_path.setter
    def icon_path(self, icon_path):
        """
        Sets the icon_path of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        An icon for the item.

        :param icon_path: The icon_path of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :type: str
        """

        self._icon_path = icon_path

    @property
    def vendor_item_index(self):
        """
        Gets the vendor_item_index of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        If the item was derived from a \"Preview Vendor\", this will be an index intothe DestinyVendorDefinition's itemList property.  Otherwise, -1.

        :return: The vendor_item_index of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :rtype: int
        """
        return self._vendor_item_index

    @vendor_item_index.setter
    def vendor_item_index(self, vendor_item_index):
        """
        Sets the vendor_item_index of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        If the item was derived from a \"Preview Vendor\", this will be an index intothe DestinyVendorDefinition's itemList property.  Otherwise, -1.

        :param vendor_item_index: The vendor_item_index of this DestinyDefinitionsItemsDestinyDerivedItemDefinition.
        :type: int
        """

        self._vendor_item_index = vendor_item_index

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
        if not isinstance(other, DestinyDefinitionsItemsDestinyDerivedItemDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
