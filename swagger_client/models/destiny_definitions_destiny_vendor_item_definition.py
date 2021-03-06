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


class DestinyDefinitionsDestinyVendorItemDefinition(object):
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
        'vendor_item_index': 'int',
        'item_hash': 'int',
        'quantity': 'int',
        'failure_indexes': 'list[int]',
        'currencies': 'list[ComponentsschemasDestinyDestinyItemQuantity]',
        'refund_time_limit': 'int',
        'creation_levels': 'list[ComponentsschemasDestinyDefinitionsDestinyItemCreationEntryLevelDefinition]',
        'display_category_index': 'int',
        'category_index': 'int',
        'original_category_index': 'int',
        'minimum_level': 'int',
        'maximum_level': 'int',
        'display_category': 'str',
        'inventory_bucket_hash': 'int'
    }

    attribute_map = {
        'vendor_item_index': 'vendorItemIndex',
        'item_hash': 'itemHash',
        'quantity': 'quantity',
        'failure_indexes': 'failureIndexes',
        'currencies': 'currencies',
        'refund_time_limit': 'refundTimeLimit',
        'creation_levels': 'creationLevels',
        'display_category_index': 'displayCategoryIndex',
        'category_index': 'categoryIndex',
        'original_category_index': 'originalCategoryIndex',
        'minimum_level': 'minimumLevel',
        'maximum_level': 'maximumLevel',
        'display_category': 'displayCategory',
        'inventory_bucket_hash': 'inventoryBucketHash'
    }

    def __init__(self, vendor_item_index=None, item_hash=None, quantity=None, failure_indexes=None, currencies=None, refund_time_limit=None, creation_levels=None, display_category_index=None, category_index=None, original_category_index=None, minimum_level=None, maximum_level=None, display_category=None, inventory_bucket_hash=None):
        """
        DestinyDefinitionsDestinyVendorItemDefinition - a model defined in Swagger
        """

        self._vendor_item_index = None
        self._item_hash = None
        self._quantity = None
        self._failure_indexes = None
        self._currencies = None
        self._refund_time_limit = None
        self._creation_levels = None
        self._display_category_index = None
        self._category_index = None
        self._original_category_index = None
        self._minimum_level = None
        self._maximum_level = None
        self._display_category = None
        self._inventory_bucket_hash = None
        self.discriminator = None

        if vendor_item_index is not None:
          self.vendor_item_index = vendor_item_index
        if item_hash is not None:
          self.item_hash = item_hash
        if quantity is not None:
          self.quantity = quantity
        if failure_indexes is not None:
          self.failure_indexes = failure_indexes
        if currencies is not None:
          self.currencies = currencies
        if refund_time_limit is not None:
          self.refund_time_limit = refund_time_limit
        if creation_levels is not None:
          self.creation_levels = creation_levels
        if display_category_index is not None:
          self.display_category_index = display_category_index
        if category_index is not None:
          self.category_index = category_index
        if original_category_index is not None:
          self.original_category_index = original_category_index
        if minimum_level is not None:
          self.minimum_level = minimum_level
        if maximum_level is not None:
          self.maximum_level = maximum_level
        if display_category is not None:
          self.display_category = display_category
        if inventory_bucket_hash is not None:
          self.inventory_bucket_hash = inventory_bucket_hash

    @property
    def vendor_item_index(self):
        """
        Gets the vendor_item_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        The index into the DestinyVendorDefinition.saleList.  This is what we use to refer to itemsbeing sold throughout live and definition data.

        :return: The vendor_item_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: int
        """
        return self._vendor_item_index

    @vendor_item_index.setter
    def vendor_item_index(self, vendor_item_index):
        """
        Sets the vendor_item_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        The index into the DestinyVendorDefinition.saleList.  This is what we use to refer to itemsbeing sold throughout live and definition data.

        :param vendor_item_index: The vendor_item_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: int
        """

        self._vendor_item_index = vendor_item_index

    @property
    def item_hash(self):
        """
        Gets the item_hash of this DestinyDefinitionsDestinyVendorItemDefinition.
        The hash identifier of the item being sold (DestinyInventoryItemDefinition).  Note that a vendor can sell the same item in multiple ways, so don't assume that itemHash isa unique identifier for this entity.

        :return: The item_hash of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: int
        """
        return self._item_hash

    @item_hash.setter
    def item_hash(self, item_hash):
        """
        Sets the item_hash of this DestinyDefinitionsDestinyVendorItemDefinition.
        The hash identifier of the item being sold (DestinyInventoryItemDefinition).  Note that a vendor can sell the same item in multiple ways, so don't assume that itemHash isa unique identifier for this entity.

        :param item_hash: The item_hash of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: int
        """

        self._item_hash = item_hash

    @property
    def quantity(self):
        """
        Gets the quantity of this DestinyDefinitionsDestinyVendorItemDefinition.
        The amount you will recieve of the item described in itemHash if you make the purchase.

        :return: The quantity of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this DestinyDefinitionsDestinyVendorItemDefinition.
        The amount you will recieve of the item described in itemHash if you make the purchase.

        :param quantity: The quantity of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: int
        """

        self._quantity = quantity

    @property
    def failure_indexes(self):
        """
        Gets the failure_indexes of this DestinyDefinitionsDestinyVendorItemDefinition.
        An list of indexes into the DestinyVendorDefinition.failureStrings array, indicatingthe possible failure strings that can be relevant for this item.

        :return: The failure_indexes of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: list[int]
        """
        return self._failure_indexes

    @failure_indexes.setter
    def failure_indexes(self, failure_indexes):
        """
        Sets the failure_indexes of this DestinyDefinitionsDestinyVendorItemDefinition.
        An list of indexes into the DestinyVendorDefinition.failureStrings array, indicatingthe possible failure strings that can be relevant for this item.

        :param failure_indexes: The failure_indexes of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: list[int]
        """

        self._failure_indexes = failure_indexes

    @property
    def currencies(self):
        """
        Gets the currencies of this DestinyDefinitionsDestinyVendorItemDefinition.
        This is a pre-compiled aggregation of item value and priceOverrideList, so that we have one placeto check for what the purchaser must pay for the item.  Use this instead of trying to piece togetherthe price separately.

        :return: The currencies of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: list[ComponentsschemasDestinyDestinyItemQuantity]
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        """
        Sets the currencies of this DestinyDefinitionsDestinyVendorItemDefinition.
        This is a pre-compiled aggregation of item value and priceOverrideList, so that we have one placeto check for what the purchaser must pay for the item.  Use this instead of trying to piece togetherthe price separately.

        :param currencies: The currencies of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: list[ComponentsschemasDestinyDestinyItemQuantity]
        """

        self._currencies = currencies

    @property
    def refund_time_limit(self):
        """
        Gets the refund_time_limit of this DestinyDefinitionsDestinyVendorItemDefinition.
        The amount of time before refundability of the newly purchased item will expire.

        :return: The refund_time_limit of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: int
        """
        return self._refund_time_limit

    @refund_time_limit.setter
    def refund_time_limit(self, refund_time_limit):
        """
        Sets the refund_time_limit of this DestinyDefinitionsDestinyVendorItemDefinition.
        The amount of time before refundability of the newly purchased item will expire.

        :param refund_time_limit: The refund_time_limit of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: int
        """

        self._refund_time_limit = refund_time_limit

    @property
    def creation_levels(self):
        """
        Gets the creation_levels of this DestinyDefinitionsDestinyVendorItemDefinition.
        The Default level at which the item will spawn.  Almost always driven by an adjusto these days.Ideally should be singular.  It's a long story how this ended up as a list, but there is always eithergoing to be 0:1 of these entities.

        :return: The creation_levels of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDestinyItemCreationEntryLevelDefinition]
        """
        return self._creation_levels

    @creation_levels.setter
    def creation_levels(self, creation_levels):
        """
        Sets the creation_levels of this DestinyDefinitionsDestinyVendorItemDefinition.
        The Default level at which the item will spawn.  Almost always driven by an adjusto these days.Ideally should be singular.  It's a long story how this ended up as a list, but there is always eithergoing to be 0:1 of these entities.

        :param creation_levels: The creation_levels of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDestinyItemCreationEntryLevelDefinition]
        """

        self._creation_levels = creation_levels

    @property
    def display_category_index(self):
        """
        Gets the display_category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        This is an index specifically into the display category, as opposed to the server-side Categories(which do not need to match or pair with each other in any way: server side categories are really juststructures for common validation.  Display Category will let us more easily categorize items visually)

        :return: The display_category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: int
        """
        return self._display_category_index

    @display_category_index.setter
    def display_category_index(self, display_category_index):
        """
        Sets the display_category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        This is an index specifically into the display category, as opposed to the server-side Categories(which do not need to match or pair with each other in any way: server side categories are really juststructures for common validation.  Display Category will let us more easily categorize items visually)

        :param display_category_index: The display_category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: int
        """

        self._display_category_index = display_category_index

    @property
    def category_index(self):
        """
        Gets the category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        The index into the DestinyVendorDefinition.categories array, so you can find the category associated withthis item.

        :return: The category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: int
        """
        return self._category_index

    @category_index.setter
    def category_index(self, category_index):
        """
        Sets the category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        The index into the DestinyVendorDefinition.categories array, so you can find the category associated withthis item.

        :param category_index: The category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: int
        """

        self._category_index = category_index

    @property
    def original_category_index(self):
        """
        Gets the original_category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        Same as above, but for the original category indexes.

        :return: The original_category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: int
        """
        return self._original_category_index

    @original_category_index.setter
    def original_category_index(self, original_category_index):
        """
        Sets the original_category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        Same as above, but for the original category indexes.

        :param original_category_index: The original_category_index of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: int
        """

        self._original_category_index = original_category_index

    @property
    def minimum_level(self):
        """
        Gets the minimum_level of this DestinyDefinitionsDestinyVendorItemDefinition.
        The minimum character level at which this item is available for sale.

        :return: The minimum_level of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: int
        """
        return self._minimum_level

    @minimum_level.setter
    def minimum_level(self, minimum_level):
        """
        Sets the minimum_level of this DestinyDefinitionsDestinyVendorItemDefinition.
        The minimum character level at which this item is available for sale.

        :param minimum_level: The minimum_level of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: int
        """

        self._minimum_level = minimum_level

    @property
    def maximum_level(self):
        """
        Gets the maximum_level of this DestinyDefinitionsDestinyVendorItemDefinition.
        The maximum character level at which this item is available for sale.

        :return: The maximum_level of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: int
        """
        return self._maximum_level

    @maximum_level.setter
    def maximum_level(self, maximum_level):
        """
        Sets the maximum_level of this DestinyDefinitionsDestinyVendorItemDefinition.
        The maximum character level at which this item is available for sale.

        :param maximum_level: The maximum_level of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: int
        """

        self._maximum_level = maximum_level

    @property
    def display_category(self):
        """
        Gets the display_category of this DestinyDefinitionsDestinyVendorItemDefinition.
        The string identifier for the category selling this item.

        :return: The display_category of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: str
        """
        return self._display_category

    @display_category.setter
    def display_category(self, display_category):
        """
        Sets the display_category of this DestinyDefinitionsDestinyVendorItemDefinition.
        The string identifier for the category selling this item.

        :param display_category: The display_category of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: str
        """

        self._display_category = display_category

    @property
    def inventory_bucket_hash(self):
        """
        Gets the inventory_bucket_hash of this DestinyDefinitionsDestinyVendorItemDefinition.
        The inventory bucket into which this item will be placed upon purchase.

        :return: The inventory_bucket_hash of this DestinyDefinitionsDestinyVendorItemDefinition.
        :rtype: int
        """
        return self._inventory_bucket_hash

    @inventory_bucket_hash.setter
    def inventory_bucket_hash(self, inventory_bucket_hash):
        """
        Sets the inventory_bucket_hash of this DestinyDefinitionsDestinyVendorItemDefinition.
        The inventory bucket into which this item will be placed upon purchase.

        :param inventory_bucket_hash: The inventory_bucket_hash of this DestinyDefinitionsDestinyVendorItemDefinition.
        :type: int
        """

        self._inventory_bucket_hash = inventory_bucket_hash

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
        if not isinstance(other, DestinyDefinitionsDestinyVendorItemDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
