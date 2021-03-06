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


class DestinyDefinitionsDestinyActivityModeDefinition(object):
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
        'pgcr_image': 'str',
        'mode_type': 'ComponentsschemasDestinyHistoricalStatsDefinitionsDestinyActivityModeType',
        'activity_mode_category': 'ComponentsschemasDestinyDestinyActivityModeCategory',
        'parent_hashes': 'list[int]',
        'friendly_name': 'str',
        'activity_mode_mappings': 'dict(str, ComponentsschemasDestinyHistoricalStatsDefinitionsDestinyActivityModeType)',
        'display': 'bool',
        'order': 'int',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'pgcr_image': 'pgcrImage',
        'mode_type': 'modeType',
        'activity_mode_category': 'activityModeCategory',
        'parent_hashes': 'parentHashes',
        'friendly_name': 'friendlyName',
        'activity_mode_mappings': 'activityModeMappings',
        'display': 'display',
        'order': 'order',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, pgcr_image=None, mode_type=None, activity_mode_category=None, parent_hashes=None, friendly_name=None, activity_mode_mappings=None, display=None, order=None, hash=None, index=None, redacted=None):
        """
        DestinyDefinitionsDestinyActivityModeDefinition - a model defined in Swagger
        """

        self._display_properties = None
        self._pgcr_image = None
        self._mode_type = None
        self._activity_mode_category = None
        self._parent_hashes = None
        self._friendly_name = None
        self._activity_mode_mappings = None
        self._display = None
        self._order = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
          self.display_properties = display_properties
        if pgcr_image is not None:
          self.pgcr_image = pgcr_image
        if mode_type is not None:
          self.mode_type = mode_type
        if activity_mode_category is not None:
          self.activity_mode_category = activity_mode_category
        if parent_hashes is not None:
          self.parent_hashes = parent_hashes
        if friendly_name is not None:
          self.friendly_name = friendly_name
        if activity_mode_mappings is not None:
          self.activity_mode_mappings = activity_mode_mappings
        if display is not None:
          self.display = display
        if order is not None:
          self.order = order
        if hash is not None:
          self.hash = hash
        if index is not None:
          self.index = index
        if redacted is not None:
          self.redacted = redacted

    @property
    def display_properties(self):
        """
        Gets the display_properties of this DestinyDefinitionsDestinyActivityModeDefinition.

        :return: The display_properties of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """
        Sets the display_properties of this DestinyDefinitionsDestinyActivityModeDefinition.

        :param display_properties: The display_properties of this DestinyDefinitionsDestinyActivityModeDefinition.
        :type: ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def pgcr_image(self):
        """
        Gets the pgcr_image of this DestinyDefinitionsDestinyActivityModeDefinition.

        :return: The pgcr_image of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: str
        """
        return self._pgcr_image

    @pgcr_image.setter
    def pgcr_image(self, pgcr_image):
        """
        Sets the pgcr_image of this DestinyDefinitionsDestinyActivityModeDefinition.

        :param pgcr_image: The pgcr_image of this DestinyDefinitionsDestinyActivityModeDefinition.
        :type: str
        """

        self._pgcr_image = pgcr_image

    @property
    def mode_type(self):
        """
        Gets the mode_type of this DestinyDefinitionsDestinyActivityModeDefinition.

        :return: The mode_type of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: ComponentsschemasDestinyHistoricalStatsDefinitionsDestinyActivityModeType
        """
        return self._mode_type

    @mode_type.setter
    def mode_type(self, mode_type):
        """
        Sets the mode_type of this DestinyDefinitionsDestinyActivityModeDefinition.

        :param mode_type: The mode_type of this DestinyDefinitionsDestinyActivityModeDefinition.
        :type: ComponentsschemasDestinyHistoricalStatsDefinitionsDestinyActivityModeType
        """

        self._mode_type = mode_type

    @property
    def activity_mode_category(self):
        """
        Gets the activity_mode_category of this DestinyDefinitionsDestinyActivityModeDefinition.

        :return: The activity_mode_category of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: ComponentsschemasDestinyDestinyActivityModeCategory
        """
        return self._activity_mode_category

    @activity_mode_category.setter
    def activity_mode_category(self, activity_mode_category):
        """
        Sets the activity_mode_category of this DestinyDefinitionsDestinyActivityModeDefinition.

        :param activity_mode_category: The activity_mode_category of this DestinyDefinitionsDestinyActivityModeDefinition.
        :type: ComponentsschemasDestinyDestinyActivityModeCategory
        """

        self._activity_mode_category = activity_mode_category

    @property
    def parent_hashes(self):
        """
        Gets the parent_hashes of this DestinyDefinitionsDestinyActivityModeDefinition.

        :return: The parent_hashes of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: list[int]
        """
        return self._parent_hashes

    @parent_hashes.setter
    def parent_hashes(self, parent_hashes):
        """
        Sets the parent_hashes of this DestinyDefinitionsDestinyActivityModeDefinition.

        :param parent_hashes: The parent_hashes of this DestinyDefinitionsDestinyActivityModeDefinition.
        :type: list[int]
        """

        self._parent_hashes = parent_hashes

    @property
    def friendly_name(self):
        """
        Gets the friendly_name of this DestinyDefinitionsDestinyActivityModeDefinition.

        :return: The friendly_name of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """
        Sets the friendly_name of this DestinyDefinitionsDestinyActivityModeDefinition.

        :param friendly_name: The friendly_name of this DestinyDefinitionsDestinyActivityModeDefinition.
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def activity_mode_mappings(self):
        """
        Gets the activity_mode_mappings of this DestinyDefinitionsDestinyActivityModeDefinition.

        :return: The activity_mode_mappings of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: dict(str, ComponentsschemasDestinyHistoricalStatsDefinitionsDestinyActivityModeType)
        """
        return self._activity_mode_mappings

    @activity_mode_mappings.setter
    def activity_mode_mappings(self, activity_mode_mappings):
        """
        Sets the activity_mode_mappings of this DestinyDefinitionsDestinyActivityModeDefinition.

        :param activity_mode_mappings: The activity_mode_mappings of this DestinyDefinitionsDestinyActivityModeDefinition.
        :type: dict(str, ComponentsschemasDestinyHistoricalStatsDefinitionsDestinyActivityModeType)
        """

        self._activity_mode_mappings = activity_mode_mappings

    @property
    def display(self):
        """
        Gets the display of this DestinyDefinitionsDestinyActivityModeDefinition.
        If FALSE, we want to ignore this type when we're showing activity modes in BNet UI.  It will still be returned in case3rd parties want to use it for any purpose.

        :return: The display of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: bool
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this DestinyDefinitionsDestinyActivityModeDefinition.
        If FALSE, we want to ignore this type when we're showing activity modes in BNet UI.  It will still be returned in case3rd parties want to use it for any purpose.

        :param display: The display of this DestinyDefinitionsDestinyActivityModeDefinition.
        :type: bool
        """

        self._display = display

    @property
    def order(self):
        """
        Gets the order of this DestinyDefinitionsDestinyActivityModeDefinition.
        The relative ordering of activity modes.

        :return: The order of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this DestinyDefinitionsDestinyActivityModeDefinition.
        The relative ordering of activity modes.

        :param order: The order of this DestinyDefinitionsDestinyActivityModeDefinition.
        :type: int
        """

        self._order = order

    @property
    def hash(self):
        """
        Gets the hash of this DestinyDefinitionsDestinyActivityModeDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :return: The hash of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this DestinyDefinitionsDestinyActivityModeDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :param hash: The hash of this DestinyDefinitionsDestinyActivityModeDefinition.
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """
        Gets the index of this DestinyDefinitionsDestinyActivityModeDefinition.
        The index of the entity as it was found in the investment tables.

        :return: The index of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this DestinyDefinitionsDestinyActivityModeDefinition.
        The index of the entity as it was found in the investment tables.

        :param index: The index of this DestinyDefinitionsDestinyActivityModeDefinition.
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """
        Gets the redacted of this DestinyDefinitionsDestinyActivityModeDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :return: The redacted of this DestinyDefinitionsDestinyActivityModeDefinition.
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """
        Sets the redacted of this DestinyDefinitionsDestinyActivityModeDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :param redacted: The redacted of this DestinyDefinitionsDestinyActivityModeDefinition.
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
        if not isinstance(other, DestinyDefinitionsDestinyActivityModeDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
