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


class TrendingTrendingCategory(object):
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
        'category_name': 'str',
        'entries': 'ComponentsschemasSearchResultOfTrendingEntry',
        'category_id': 'str'
    }

    attribute_map = {
        'category_name': 'categoryName',
        'entries': 'entries',
        'category_id': 'categoryId'
    }

    def __init__(self, category_name=None, entries=None, category_id=None):
        """
        TrendingTrendingCategory - a model defined in Swagger
        """

        self._category_name = None
        self._entries = None
        self._category_id = None
        self.discriminator = None

        if category_name is not None:
          self.category_name = category_name
        if entries is not None:
          self.entries = entries
        if category_id is not None:
          self.category_id = category_id

    @property
    def category_name(self):
        """
        Gets the category_name of this TrendingTrendingCategory.

        :return: The category_name of this TrendingTrendingCategory.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """
        Sets the category_name of this TrendingTrendingCategory.

        :param category_name: The category_name of this TrendingTrendingCategory.
        :type: str
        """

        self._category_name = category_name

    @property
    def entries(self):
        """
        Gets the entries of this TrendingTrendingCategory.

        :return: The entries of this TrendingTrendingCategory.
        :rtype: ComponentsschemasSearchResultOfTrendingEntry
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """
        Sets the entries of this TrendingTrendingCategory.

        :param entries: The entries of this TrendingTrendingCategory.
        :type: ComponentsschemasSearchResultOfTrendingEntry
        """

        self._entries = entries

    @property
    def category_id(self):
        """
        Gets the category_id of this TrendingTrendingCategory.

        :return: The category_id of this TrendingTrendingCategory.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this TrendingTrendingCategory.

        :param category_id: The category_id of this TrendingTrendingCategory.
        :type: str
        """

        self._category_id = category_id

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
        if not isinstance(other, TrendingTrendingCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
