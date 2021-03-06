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


class DestinyDefinitionsDestinyItemTalentGridBlockDefinition(object):
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
        'talent_grid_hash': 'int',
        'item_detail_string': 'str',
        'build_name': 'str',
        'hud_icon': 'str'
    }

    attribute_map = {
        'talent_grid_hash': 'talentGridHash',
        'item_detail_string': 'itemDetailString',
        'build_name': 'buildName',
        'hud_icon': 'hudIcon'
    }

    def __init__(self, talent_grid_hash=None, item_detail_string=None, build_name=None, hud_icon=None):
        """
        DestinyDefinitionsDestinyItemTalentGridBlockDefinition - a model defined in Swagger
        """

        self._talent_grid_hash = None
        self._item_detail_string = None
        self._build_name = None
        self._hud_icon = None
        self.discriminator = None

        if talent_grid_hash is not None:
          self.talent_grid_hash = talent_grid_hash
        if item_detail_string is not None:
          self.item_detail_string = item_detail_string
        if build_name is not None:
          self.build_name = build_name
        if hud_icon is not None:
          self.hud_icon = hud_icon

    @property
    def talent_grid_hash(self):
        """
        Gets the talent_grid_hash of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        The hash identifier of the DestinyTalentGridDefinition attached to this item.

        :return: The talent_grid_hash of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        :rtype: int
        """
        return self._talent_grid_hash

    @talent_grid_hash.setter
    def talent_grid_hash(self, talent_grid_hash):
        """
        Sets the talent_grid_hash of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        The hash identifier of the DestinyTalentGridDefinition attached to this item.

        :param talent_grid_hash: The talent_grid_hash of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        :type: int
        """

        self._talent_grid_hash = talent_grid_hash

    @property
    def item_detail_string(self):
        """
        Gets the item_detail_string of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        This is meant to be a subtitle for looking at the talent grid.In practice, somewhat frustratingly, this always merely says the localized wordfor \"Details\".  Great.  Maybe it'll have more if talent grids ever get usedfor more than builds and subclasses again.

        :return: The item_detail_string of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        :rtype: str
        """
        return self._item_detail_string

    @item_detail_string.setter
    def item_detail_string(self, item_detail_string):
        """
        Sets the item_detail_string of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        This is meant to be a subtitle for looking at the talent grid.In practice, somewhat frustratingly, this always merely says the localized wordfor \"Details\".  Great.  Maybe it'll have more if talent grids ever get usedfor more than builds and subclasses again.

        :param item_detail_string: The item_detail_string of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        :type: str
        """

        self._item_detail_string = item_detail_string

    @property
    def build_name(self):
        """
        Gets the build_name of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        A shortcut string identifier for the \"build\" in question, if this talent gridhas an associated build.  Doesn't map to anything we can expose at the moment.

        :return: The build_name of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        :rtype: str
        """
        return self._build_name

    @build_name.setter
    def build_name(self, build_name):
        """
        Sets the build_name of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        A shortcut string identifier for the \"build\" in question, if this talent gridhas an associated build.  Doesn't map to anything we can expose at the moment.

        :param build_name: The build_name of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        :type: str
        """

        self._build_name = build_name

    @property
    def hud_icon(self):
        """
        Gets the hud_icon of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        If the talent grid has a special icon that's shown in the game UI (like builds, funny that),this is the identifier for that icon.Sadly, we don't actually get that icon right now.  I'll be looking to replace thiswith a path to the actual icon itself.

        :return: The hud_icon of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        :rtype: str
        """
        return self._hud_icon

    @hud_icon.setter
    def hud_icon(self, hud_icon):
        """
        Sets the hud_icon of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        If the talent grid has a special icon that's shown in the game UI (like builds, funny that),this is the identifier for that icon.Sadly, we don't actually get that icon right now.  I'll be looking to replace thiswith a path to the actual icon itself.

        :param hud_icon: The hud_icon of this DestinyDefinitionsDestinyItemTalentGridBlockDefinition.
        :type: str
        """

        self._hud_icon = hud_icon

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
        if not isinstance(other, DestinyDefinitionsDestinyItemTalentGridBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
