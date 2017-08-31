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


class DestinyDestinyActivity(object):
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
        'activity_hash': 'int',
        'is_new': 'bool',
        'can_lead': 'bool',
        'can_join': 'bool',
        'is_completed': 'bool',
        'is_visible': 'bool',
        'display_level': 'int',
        'recommended_light': 'int'
    }

    attribute_map = {
        'activity_hash': 'activityHash',
        'is_new': 'isNew',
        'can_lead': 'canLead',
        'can_join': 'canJoin',
        'is_completed': 'isCompleted',
        'is_visible': 'isVisible',
        'display_level': 'displayLevel',
        'recommended_light': 'recommendedLight'
    }

    def __init__(self, activity_hash=None, is_new=None, can_lead=None, can_join=None, is_completed=None, is_visible=None, display_level=None, recommended_light=None):
        """
        DestinyDestinyActivity - a model defined in Swagger
        """

        self._activity_hash = None
        self._is_new = None
        self._can_lead = None
        self._can_join = None
        self._is_completed = None
        self._is_visible = None
        self._display_level = None
        self._recommended_light = None
        self.discriminator = None

        if activity_hash is not None:
          self.activity_hash = activity_hash
        if is_new is not None:
          self.is_new = is_new
        if can_lead is not None:
          self.can_lead = can_lead
        if can_join is not None:
          self.can_join = can_join
        if is_completed is not None:
          self.is_completed = is_completed
        if is_visible is not None:
          self.is_visible = is_visible
        if display_level is not None:
          self.display_level = display_level
        if recommended_light is not None:
          self.recommended_light = recommended_light

    @property
    def activity_hash(self):
        """
        Gets the activity_hash of this DestinyDestinyActivity.
        The hash identifier of the Activity.  Use this to look up the DestinyActivityDefinition of the activity.

        :return: The activity_hash of this DestinyDestinyActivity.
        :rtype: int
        """
        return self._activity_hash

    @activity_hash.setter
    def activity_hash(self, activity_hash):
        """
        Sets the activity_hash of this DestinyDestinyActivity.
        The hash identifier of the Activity.  Use this to look up the DestinyActivityDefinition of the activity.

        :param activity_hash: The activity_hash of this DestinyDestinyActivity.
        :type: int
        """

        self._activity_hash = activity_hash

    @property
    def is_new(self):
        """
        Gets the is_new of this DestinyDestinyActivity.
        If true, then the activity should have a \"new\" indicator in the Director UI.

        :return: The is_new of this DestinyDestinyActivity.
        :rtype: bool
        """
        return self._is_new

    @is_new.setter
    def is_new(self, is_new):
        """
        Sets the is_new of this DestinyDestinyActivity.
        If true, then the activity should have a \"new\" indicator in the Director UI.

        :param is_new: The is_new of this DestinyDestinyActivity.
        :type: bool
        """

        self._is_new = is_new

    @property
    def can_lead(self):
        """
        Gets the can_lead of this DestinyDestinyActivity.
        If true, the user is allowed to lead a Fireteam into this activity.

        :return: The can_lead of this DestinyDestinyActivity.
        :rtype: bool
        """
        return self._can_lead

    @can_lead.setter
    def can_lead(self, can_lead):
        """
        Sets the can_lead of this DestinyDestinyActivity.
        If true, the user is allowed to lead a Fireteam into this activity.

        :param can_lead: The can_lead of this DestinyDestinyActivity.
        :type: bool
        """

        self._can_lead = can_lead

    @property
    def can_join(self):
        """
        Gets the can_join of this DestinyDestinyActivity.
        If true, the user is allowed to join with another Fireteam in this activity.

        :return: The can_join of this DestinyDestinyActivity.
        :rtype: bool
        """
        return self._can_join

    @can_join.setter
    def can_join(self, can_join):
        """
        Sets the can_join of this DestinyDestinyActivity.
        If true, the user is allowed to join with another Fireteam in this activity.

        :param can_join: The can_join of this DestinyDestinyActivity.
        :type: bool
        """

        self._can_join = can_join

    @property
    def is_completed(self):
        """
        Gets the is_completed of this DestinyDestinyActivity.
        If true, we both have the ability to know that the user has completed this activity andthey have completed it.  Unfortunately, we can't necessarily know this for all activities.  As such,this should probably only be used if you already know in advance which specific activities you wish to check.

        :return: The is_completed of this DestinyDestinyActivity.
        :rtype: bool
        """
        return self._is_completed

    @is_completed.setter
    def is_completed(self, is_completed):
        """
        Sets the is_completed of this DestinyDestinyActivity.
        If true, we both have the ability to know that the user has completed this activity andthey have completed it.  Unfortunately, we can't necessarily know this for all activities.  As such,this should probably only be used if you already know in advance which specific activities you wish to check.

        :param is_completed: The is_completed of this DestinyDestinyActivity.
        :type: bool
        """

        self._is_completed = is_completed

    @property
    def is_visible(self):
        """
        Gets the is_visible of this DestinyDestinyActivity.
        If true, the user should be able to see this activity.

        :return: The is_visible of this DestinyDestinyActivity.
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """
        Sets the is_visible of this DestinyDestinyActivity.
        If true, the user should be able to see this activity.

        :param is_visible: The is_visible of this DestinyDestinyActivity.
        :type: bool
        """

        self._is_visible = is_visible

    @property
    def display_level(self):
        """
        Gets the display_level of this DestinyDestinyActivity.
        The difficulty level of the activity, if applicable.

        :return: The display_level of this DestinyDestinyActivity.
        :rtype: int
        """
        return self._display_level

    @display_level.setter
    def display_level(self, display_level):
        """
        Sets the display_level of this DestinyDestinyActivity.
        The difficulty level of the activity, if applicable.

        :param display_level: The display_level of this DestinyDestinyActivity.
        :type: int
        """

        self._display_level = display_level

    @property
    def recommended_light(self):
        """
        Gets the recommended_light of this DestinyDestinyActivity.
        The recommended light level for the activity, if applicable.

        :return: The recommended_light of this DestinyDestinyActivity.
        :rtype: int
        """
        return self._recommended_light

    @recommended_light.setter
    def recommended_light(self, recommended_light):
        """
        Sets the recommended_light of this DestinyDestinyActivity.
        The recommended light level for the activity, if applicable.

        :param recommended_light: The recommended_light of this DestinyDestinyActivity.
        :type: int
        """

        self._recommended_light = recommended_light

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
        if not isinstance(other, DestinyDestinyActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
