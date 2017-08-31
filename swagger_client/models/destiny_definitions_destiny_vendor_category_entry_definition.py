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


class DestinyDefinitionsDestinyVendorCategoryEntryDefinition(object):
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
        'category_index': 'int',
        'category_id': 'str',
        'category_hash': 'int',
        'quantity_available': 'int',
        'show_unavailable_items': 'bool',
        'hide_if_no_currency': 'bool',
        'hide_from_regular_purchase': 'bool',
        'buy_string_override': 'str',
        'disabled_description': 'str',
        'display_title': 'str'
    }

    attribute_map = {
        'category_index': 'categoryIndex',
        'category_id': 'categoryId',
        'category_hash': 'categoryHash',
        'quantity_available': 'quantityAvailable',
        'show_unavailable_items': 'showUnavailableItems',
        'hide_if_no_currency': 'hideIfNoCurrency',
        'hide_from_regular_purchase': 'hideFromRegularPurchase',
        'buy_string_override': 'buyStringOverride',
        'disabled_description': 'disabledDescription',
        'display_title': 'displayTitle'
    }

    def __init__(self, category_index=None, category_id=None, category_hash=None, quantity_available=None, show_unavailable_items=None, hide_if_no_currency=None, hide_from_regular_purchase=None, buy_string_override=None, disabled_description=None, display_title=None):
        """
        DestinyDefinitionsDestinyVendorCategoryEntryDefinition - a model defined in Swagger
        """

        self._category_index = None
        self._category_id = None
        self._category_hash = None
        self._quantity_available = None
        self._show_unavailable_items = None
        self._hide_if_no_currency = None
        self._hide_from_regular_purchase = None
        self._buy_string_override = None
        self._disabled_description = None
        self._display_title = None
        self.discriminator = None

        if category_index is not None:
          self.category_index = category_index
        if category_id is not None:
          self.category_id = category_id
        if category_hash is not None:
          self.category_hash = category_hash
        if quantity_available is not None:
          self.quantity_available = quantity_available
        if show_unavailable_items is not None:
          self.show_unavailable_items = show_unavailable_items
        if hide_if_no_currency is not None:
          self.hide_if_no_currency = hide_if_no_currency
        if hide_from_regular_purchase is not None:
          self.hide_from_regular_purchase = hide_from_regular_purchase
        if buy_string_override is not None:
          self.buy_string_override = buy_string_override
        if disabled_description is not None:
          self.disabled_description = disabled_description
        if display_title is not None:
          self.display_title = display_title

    @property
    def category_index(self):
        """
        Gets the category_index of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The index of the category in the original category definitions for the vendor.

        :return: The category_index of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :rtype: int
        """
        return self._category_index

    @category_index.setter
    def category_index(self, category_index):
        """
        Sets the category_index of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The index of the category in the original category definitions for the vendor.

        :param category_index: The category_index of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :type: int
        """

        self._category_index = category_index

    @property
    def category_id(self):
        """
        Gets the category_id of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The string identifier of the category.

        :return: The category_id of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The string identifier of the category.

        :param category_id: The category_id of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :type: str
        """

        self._category_id = category_id

    @property
    def category_hash(self):
        """
        Gets the category_hash of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The hashed identifier for the category.  (note that this is NOT pointing to a DestinyVendorCategoryDefinition,it's confusing but this is a sale item category in a vendor, not a categorization of vendors themselves)

        :return: The category_hash of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :rtype: int
        """
        return self._category_hash

    @category_hash.setter
    def category_hash(self, category_hash):
        """
        Sets the category_hash of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The hashed identifier for the category.  (note that this is NOT pointing to a DestinyVendorCategoryDefinition,it's confusing but this is a sale item category in a vendor, not a categorization of vendors themselves)

        :param category_hash: The category_hash of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :type: int
        """

        self._category_hash = category_hash

    @property
    def quantity_available(self):
        """
        Gets the quantity_available of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The amount of items that will be available when this category is shown.

        :return: The quantity_available of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :rtype: int
        """
        return self._quantity_available

    @quantity_available.setter
    def quantity_available(self, quantity_available):
        """
        Sets the quantity_available of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The amount of items that will be available when this category is shown.

        :param quantity_available: The quantity_available of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :type: int
        """

        self._quantity_available = quantity_available

    @property
    def show_unavailable_items(self):
        """
        Gets the show_unavailable_items of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        If items aren't up for sale in this category, should we still show them (greyed out)?

        :return: The show_unavailable_items of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :rtype: bool
        """
        return self._show_unavailable_items

    @show_unavailable_items.setter
    def show_unavailable_items(self, show_unavailable_items):
        """
        Sets the show_unavailable_items of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        If items aren't up for sale in this category, should we still show them (greyed out)?

        :param show_unavailable_items: The show_unavailable_items of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :type: bool
        """

        self._show_unavailable_items = show_unavailable_items

    @property
    def hide_if_no_currency(self):
        """
        Gets the hide_if_no_currency of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        If you don't have the currency required to buy items from this category, should the items be hidden?

        :return: The hide_if_no_currency of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :rtype: bool
        """
        return self._hide_if_no_currency

    @hide_if_no_currency.setter
    def hide_if_no_currency(self, hide_if_no_currency):
        """
        Sets the hide_if_no_currency of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        If you don't have the currency required to buy items from this category, should the items be hidden?

        :param hide_if_no_currency: The hide_if_no_currency of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :type: bool
        """

        self._hide_if_no_currency = hide_if_no_currency

    @property
    def hide_from_regular_purchase(self):
        """
        Gets the hide_from_regular_purchase of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        True if this category doesn't allow purchases.

        :return: The hide_from_regular_purchase of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :rtype: bool
        """
        return self._hide_from_regular_purchase

    @hide_from_regular_purchase.setter
    def hide_from_regular_purchase(self, hide_from_regular_purchase):
        """
        Sets the hide_from_regular_purchase of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        True if this category doesn't allow purchases.

        :param hide_from_regular_purchase: The hide_from_regular_purchase of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :type: bool
        """

        self._hide_from_regular_purchase = hide_from_regular_purchase

    @property
    def buy_string_override(self):
        """
        Gets the buy_string_override of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The localized string for making purchases from this category, if it is different from the vendor's string for purchasing.

        :return: The buy_string_override of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :rtype: str
        """
        return self._buy_string_override

    @buy_string_override.setter
    def buy_string_override(self, buy_string_override):
        """
        Sets the buy_string_override of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The localized string for making purchases from this category, if it is different from the vendor's string for purchasing.

        :param buy_string_override: The buy_string_override of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :type: str
        """

        self._buy_string_override = buy_string_override

    @property
    def disabled_description(self):
        """
        Gets the disabled_description of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        If the category is disabled, this is the localized description to show.

        :return: The disabled_description of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :rtype: str
        """
        return self._disabled_description

    @disabled_description.setter
    def disabled_description(self, disabled_description):
        """
        Sets the disabled_description of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        If the category is disabled, this is the localized description to show.

        :param disabled_description: The disabled_description of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :type: str
        """

        self._disabled_description = disabled_description

    @property
    def display_title(self):
        """
        Gets the display_title of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The localized title of the category.

        :return: The display_title of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :rtype: str
        """
        return self._display_title

    @display_title.setter
    def display_title(self, display_title):
        """
        Sets the display_title of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        The localized title of the category.

        :param display_title: The display_title of this DestinyDefinitionsDestinyVendorCategoryEntryDefinition.
        :type: str
        """

        self._display_title = display_title

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
        if not isinstance(other, DestinyDefinitionsDestinyVendorCategoryEntryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
