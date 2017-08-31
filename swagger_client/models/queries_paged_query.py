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


class QueriesPagedQuery(object):
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
        'items_per_page': 'int',
        'current_page': 'int',
        'request_continuation_token': 'str'
    }

    attribute_map = {
        'items_per_page': 'itemsPerPage',
        'current_page': 'currentPage',
        'request_continuation_token': 'requestContinuationToken'
    }

    def __init__(self, items_per_page=None, current_page=None, request_continuation_token=None):
        """
        QueriesPagedQuery - a model defined in Swagger
        """

        self._items_per_page = None
        self._current_page = None
        self._request_continuation_token = None
        self.discriminator = None

        if items_per_page is not None:
          self.items_per_page = items_per_page
        if current_page is not None:
          self.current_page = current_page
        if request_continuation_token is not None:
          self.request_continuation_token = request_continuation_token

    @property
    def items_per_page(self):
        """
        Gets the items_per_page of this QueriesPagedQuery.

        :return: The items_per_page of this QueriesPagedQuery.
        :rtype: int
        """
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, items_per_page):
        """
        Sets the items_per_page of this QueriesPagedQuery.

        :param items_per_page: The items_per_page of this QueriesPagedQuery.
        :type: int
        """

        self._items_per_page = items_per_page

    @property
    def current_page(self):
        """
        Gets the current_page of this QueriesPagedQuery.

        :return: The current_page of this QueriesPagedQuery.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """
        Sets the current_page of this QueriesPagedQuery.

        :param current_page: The current_page of this QueriesPagedQuery.
        :type: int
        """

        self._current_page = current_page

    @property
    def request_continuation_token(self):
        """
        Gets the request_continuation_token of this QueriesPagedQuery.

        :return: The request_continuation_token of this QueriesPagedQuery.
        :rtype: str
        """
        return self._request_continuation_token

    @request_continuation_token.setter
    def request_continuation_token(self, request_continuation_token):
        """
        Sets the request_continuation_token of this QueriesPagedQuery.

        :param request_continuation_token: The request_continuation_token of this QueriesPagedQuery.
        :type: str
        """

        self._request_continuation_token = request_continuation_token

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
        if not isinstance(other, QueriesPagedQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
