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


class DestinyDefinitionsDestinyInventoryBucketDefinition(object):
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
        'display_properties': 'ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition',
        'bucket_order': 'int',
        'item_count': 'int',
        'has_transfer_destination': 'bool',
        'enabled': 'bool',
        'fifo': 'bool',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'bucket_order': 'bucketOrder',
        'item_count': 'itemCount',
        'has_transfer_destination': 'hasTransferDestination',
        'enabled': 'enabled',
        'fifo': 'fifo',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, bucket_order=None, item_count=None, has_transfer_destination=None, enabled=None, fifo=None, hash=None, index=None, redacted=None):
        """
        DestinyDefinitionsDestinyInventoryBucketDefinition - a model defined in Swagger
        """

        self._display_properties = None
        self._bucket_order = None
        self._item_count = None
        self._has_transfer_destination = None
        self._enabled = None
        self._fifo = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
          self.display_properties = display_properties
        if bucket_order is not None:
          self.bucket_order = bucket_order
        if item_count is not None:
          self.item_count = item_count
        if has_transfer_destination is not None:
          self.has_transfer_destination = has_transfer_destination
        if enabled is not None:
          self.enabled = enabled
        if fifo is not None:
          self.fifo = fifo
        if hash is not None:
          self.hash = hash
        if index is not None:
          self.index = index
        if redacted is not None:
          self.redacted = redacted

    @property
    def display_properties(self):
        """
        Gets the display_properties of this DestinyDefinitionsDestinyInventoryBucketDefinition.

        :return: The display_properties of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :rtype: ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """
        Sets the display_properties of this DestinyDefinitionsDestinyInventoryBucketDefinition.

        :param display_properties: The display_properties of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :type: ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def bucket_order(self):
        """
        Gets the bucket_order of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        Use this property to provide a quick-and-dirty recommended ordering for buckets in the UI.Most UIs will likely want to forsake this for something more custom and manual.

        :return: The bucket_order of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :rtype: int
        """
        return self._bucket_order

    @bucket_order.setter
    def bucket_order(self, bucket_order):
        """
        Sets the bucket_order of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        Use this property to provide a quick-and-dirty recommended ordering for buckets in the UI.Most UIs will likely want to forsake this for something more custom and manual.

        :param bucket_order: The bucket_order of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :type: int
        """

        self._bucket_order = bucket_order

    @property
    def item_count(self):
        """
        Gets the item_count of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        The maximum # of item \"slots\" in a bucket.  A slot is a given combination of item + quantity.  For instance, a Weapon will always take up a single slot, and always have a quantity of 1.But a material could take up only a single slot with hundreds of quantity.

        :return: The item_count of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """
        Sets the item_count of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        The maximum # of item \"slots\" in a bucket.  A slot is a given combination of item + quantity.  For instance, a Weapon will always take up a single slot, and always have a quantity of 1.But a material could take up only a single slot with hundreds of quantity.

        :param item_count: The item_count of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :type: int
        """

        self._item_count = item_count

    @property
    def has_transfer_destination(self):
        """
        Gets the has_transfer_destination of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        If TRUE, there is at least one Vendor that can transfer items to/from this bucket.  See the DestinyVendorDefinition'sacceptedItems property for more information on how transferring works.

        :return: The has_transfer_destination of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :rtype: bool
        """
        return self._has_transfer_destination

    @has_transfer_destination.setter
    def has_transfer_destination(self, has_transfer_destination):
        """
        Sets the has_transfer_destination of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        If TRUE, there is at least one Vendor that can transfer items to/from this bucket.  See the DestinyVendorDefinition'sacceptedItems property for more information on how transferring works.

        :param has_transfer_destination: The has_transfer_destination of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :type: bool
        """

        self._has_transfer_destination = has_transfer_destination

    @property
    def enabled(self):
        """
        Gets the enabled of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        If True, this bucket is enabled.  Disabled buckets may include buckets that were included for test purposes, orthat were going to be used but then were abandoned but never removed from content *cough*.

        :return: The enabled of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        If True, this bucket is enabled.  Disabled buckets may include buckets that were included for test purposes, orthat were going to be used but then were abandoned but never removed from content *cough*.

        :param enabled: The enabled of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :type: bool
        """

        self._enabled = enabled

    @property
    def fifo(self):
        """
        Gets the fifo of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        if a FIFO bucket fills up, it will delete the oldest item from said bucket when a new item tries to be addedto it.  If this is FALSE, the bucket will not allow new items to be placed in it until room is made by the usermanually deleting items from it.  You can see an example of this with the Postmaster's bucket.

        :return: The fifo of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :rtype: bool
        """
        return self._fifo

    @fifo.setter
    def fifo(self, fifo):
        """
        Sets the fifo of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        if a FIFO bucket fills up, it will delete the oldest item from said bucket when a new item tries to be addedto it.  If this is FALSE, the bucket will not allow new items to be placed in it until room is made by the usermanually deleting items from it.  You can see an example of this with the Postmaster's bucket.

        :param fifo: The fifo of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :type: bool
        """

        self._fifo = fifo

    @property
    def hash(self):
        """
        Gets the hash of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :return: The hash of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :param hash: The hash of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """
        Gets the index of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        The index of the entity as it was found in the investment tables.

        :return: The index of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        The index of the entity as it was found in the investment tables.

        :param index: The index of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """
        Gets the redacted of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :return: The redacted of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """
        Sets the redacted of this DestinyDefinitionsDestinyInventoryBucketDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :param redacted: The redacted of this DestinyDefinitionsDestinyInventoryBucketDefinition.
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
        if not isinstance(other, DestinyDefinitionsDestinyInventoryBucketDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
