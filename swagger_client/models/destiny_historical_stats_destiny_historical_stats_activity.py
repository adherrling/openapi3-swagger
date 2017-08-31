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


class DestinyHistoricalStatsDestinyHistoricalStatsActivity(object):
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
        'reference_id': 'int',
        'instance_id': 'int',
        'activity_type_hash_override': 'int',
        'is_private': 'bool'
    }

    attribute_map = {
        'reference_id': 'referenceId',
        'instance_id': 'instanceId',
        'activity_type_hash_override': 'activityTypeHashOverride',
        'is_private': 'isPrivate'
    }

    def __init__(self, reference_id=None, instance_id=None, activity_type_hash_override=None, is_private=None):
        """
        DestinyHistoricalStatsDestinyHistoricalStatsActivity - a model defined in Swagger
        """

        self._reference_id = None
        self._instance_id = None
        self._activity_type_hash_override = None
        self._is_private = None
        self.discriminator = None

        if reference_id is not None:
          self.reference_id = reference_id
        if instance_id is not None:
          self.instance_id = instance_id
        if activity_type_hash_override is not None:
          self.activity_type_hash_override = activity_type_hash_override
        if is_private is not None:
          self.is_private = is_private

    @property
    def reference_id(self):
        """
        Gets the reference_id of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        Hash ID that can be looked up in the DestinyActivityTable.

        :return: The reference_id of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        :rtype: int
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """
        Sets the reference_id of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        Hash ID that can be looked up in the DestinyActivityTable.

        :param reference_id: The reference_id of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        :type: int
        """

        self._reference_id = reference_id

    @property
    def instance_id(self):
        """
        Gets the instance_id of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        This value can be used to get additional data about this activity such as who else was playing.

        :return: The instance_id of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        This value can be used to get additional data about this activity such as who else was playing.

        :param instance_id: The instance_id of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        :type: int
        """

        self._instance_id = instance_id

    @property
    def activity_type_hash_override(self):
        """
        Gets the activity_type_hash_override of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        Hash ID that can be looked up in the DestinyActivityTypeTable. Prefer this value over the type used by the activity if it is specified.

        :return: The activity_type_hash_override of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        :rtype: int
        """
        return self._activity_type_hash_override

    @activity_type_hash_override.setter
    def activity_type_hash_override(self, activity_type_hash_override):
        """
        Sets the activity_type_hash_override of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        Hash ID that can be looked up in the DestinyActivityTypeTable. Prefer this value over the type used by the activity if it is specified.

        :param activity_type_hash_override: The activity_type_hash_override of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        :type: int
        """

        self._activity_type_hash_override = activity_type_hash_override

    @property
    def is_private(self):
        """
        Gets the is_private of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        Whether or not the match was a private match.

        :return: The is_private of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """
        Sets the is_private of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        Whether or not the match was a private match.

        :param is_private: The is_private of this DestinyHistoricalStatsDestinyHistoricalStatsActivity.
        :type: bool
        """

        self._is_private = is_private

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
        if not isinstance(other, DestinyHistoricalStatsDestinyHistoricalStatsActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
