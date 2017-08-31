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


class SearchResultOfPostResponse(object):
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
        'results': 'list[ComponentsschemasForumPostResponse]',
        'total_results': 'int',
        'has_more': 'bool',
        'query': 'ComponentsschemasQueriesPagedQuery',
        'replacement_continuation_token': 'str',
        'use_total_results': 'bool'
    }

    attribute_map = {
        'results': 'results',
        'total_results': 'totalResults',
        'has_more': 'hasMore',
        'query': 'query',
        'replacement_continuation_token': 'replacementContinuationToken',
        'use_total_results': 'useTotalResults'
    }

    def __init__(self, results=None, total_results=None, has_more=None, query=None, replacement_continuation_token=None, use_total_results=None):
        """
        SearchResultOfPostResponse - a model defined in Swagger
        """

        self._results = None
        self._total_results = None
        self._has_more = None
        self._query = None
        self._replacement_continuation_token = None
        self._use_total_results = None
        self.discriminator = None

        if results is not None:
          self.results = results
        if total_results is not None:
          self.total_results = total_results
        if has_more is not None:
          self.has_more = has_more
        if query is not None:
          self.query = query
        if replacement_continuation_token is not None:
          self.replacement_continuation_token = replacement_continuation_token
        if use_total_results is not None:
          self.use_total_results = use_total_results

    @property
    def results(self):
        """
        Gets the results of this SearchResultOfPostResponse.

        :return: The results of this SearchResultOfPostResponse.
        :rtype: list[ComponentsschemasForumPostResponse]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this SearchResultOfPostResponse.

        :param results: The results of this SearchResultOfPostResponse.
        :type: list[ComponentsschemasForumPostResponse]
        """

        self._results = results

    @property
    def total_results(self):
        """
        Gets the total_results of this SearchResultOfPostResponse.

        :return: The total_results of this SearchResultOfPostResponse.
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """
        Sets the total_results of this SearchResultOfPostResponse.

        :param total_results: The total_results of this SearchResultOfPostResponse.
        :type: int
        """

        self._total_results = total_results

    @property
    def has_more(self):
        """
        Gets the has_more of this SearchResultOfPostResponse.

        :return: The has_more of this SearchResultOfPostResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this SearchResultOfPostResponse.

        :param has_more: The has_more of this SearchResultOfPostResponse.
        :type: bool
        """

        self._has_more = has_more

    @property
    def query(self):
        """
        Gets the query of this SearchResultOfPostResponse.

        :return: The query of this SearchResultOfPostResponse.
        :rtype: ComponentsschemasQueriesPagedQuery
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this SearchResultOfPostResponse.

        :param query: The query of this SearchResultOfPostResponse.
        :type: ComponentsschemasQueriesPagedQuery
        """

        self._query = query

    @property
    def replacement_continuation_token(self):
        """
        Gets the replacement_continuation_token of this SearchResultOfPostResponse.

        :return: The replacement_continuation_token of this SearchResultOfPostResponse.
        :rtype: str
        """
        return self._replacement_continuation_token

    @replacement_continuation_token.setter
    def replacement_continuation_token(self, replacement_continuation_token):
        """
        Sets the replacement_continuation_token of this SearchResultOfPostResponse.

        :param replacement_continuation_token: The replacement_continuation_token of this SearchResultOfPostResponse.
        :type: str
        """

        self._replacement_continuation_token = replacement_continuation_token

    @property
    def use_total_results(self):
        """
        Gets the use_total_results of this SearchResultOfPostResponse.
        If useTotalResults is true, then totalResults represents an accurate count.  If False, it does not, and may be estimated/only the size of the current page.  Either way, you should probably always only trust hasMore.  This is a long-held historical throwback to when we used to do paging with known total results.Those queries toasted our database, and we were left to hastily alter our endpoints and create backward-compatible shims, of which useTotalResults is one.

        :return: The use_total_results of this SearchResultOfPostResponse.
        :rtype: bool
        """
        return self._use_total_results

    @use_total_results.setter
    def use_total_results(self, use_total_results):
        """
        Sets the use_total_results of this SearchResultOfPostResponse.
        If useTotalResults is true, then totalResults represents an accurate count.  If False, it does not, and may be estimated/only the size of the current page.  Either way, you should probably always only trust hasMore.  This is a long-held historical throwback to when we used to do paging with known total results.Those queries toasted our database, and we were left to hastily alter our endpoints and create backward-compatible shims, of which useTotalResults is one.

        :param use_total_results: The use_total_results of this SearchResultOfPostResponse.
        :type: bool
        """

        self._use_total_results = use_total_results

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
        if not isinstance(other, SearchResultOfPostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
