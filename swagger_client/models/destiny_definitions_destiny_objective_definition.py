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


class DestinyDefinitionsDestinyObjectiveDefinition(object):
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
        'completion_value': 'int',
        'location_hash': 'int',
        'allow_negative_value': 'bool',
        'allow_value_change_when_completed': 'bool',
        'is_counting_downward': 'bool',
        'progress_description': 'str',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'completion_value': 'completionValue',
        'location_hash': 'locationHash',
        'allow_negative_value': 'allowNegativeValue',
        'allow_value_change_when_completed': 'allowValueChangeWhenCompleted',
        'is_counting_downward': 'isCountingDownward',
        'progress_description': 'progressDescription',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, completion_value=None, location_hash=None, allow_negative_value=None, allow_value_change_when_completed=None, is_counting_downward=None, progress_description=None, hash=None, index=None, redacted=None):
        """
        DestinyDefinitionsDestinyObjectiveDefinition - a model defined in Swagger
        """

        self._completion_value = None
        self._location_hash = None
        self._allow_negative_value = None
        self._allow_value_change_when_completed = None
        self._is_counting_downward = None
        self._progress_description = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if completion_value is not None:
          self.completion_value = completion_value
        if location_hash is not None:
          self.location_hash = location_hash
        if allow_negative_value is not None:
          self.allow_negative_value = allow_negative_value
        if allow_value_change_when_completed is not None:
          self.allow_value_change_when_completed = allow_value_change_when_completed
        if is_counting_downward is not None:
          self.is_counting_downward = is_counting_downward
        if progress_description is not None:
          self.progress_description = progress_description
        if hash is not None:
          self.hash = hash
        if index is not None:
          self.index = index
        if redacted is not None:
          self.redacted = redacted

    @property
    def completion_value(self):
        """
        Gets the completion_value of this DestinyDefinitionsDestinyObjectiveDefinition.
        The value that the unlock value defined in unlockValueHash must reach in order forthe objective to be considered Completed.  Used in calculating progress and completion status.

        :return: The completion_value of this DestinyDefinitionsDestinyObjectiveDefinition.
        :rtype: int
        """
        return self._completion_value

    @completion_value.setter
    def completion_value(self, completion_value):
        """
        Sets the completion_value of this DestinyDefinitionsDestinyObjectiveDefinition.
        The value that the unlock value defined in unlockValueHash must reach in order forthe objective to be considered Completed.  Used in calculating progress and completion status.

        :param completion_value: The completion_value of this DestinyDefinitionsDestinyObjectiveDefinition.
        :type: int
        """

        self._completion_value = completion_value

    @property
    def location_hash(self):
        """
        Gets the location_hash of this DestinyDefinitionsDestinyObjectiveDefinition.
        OPTIONAL: a hash identifier for the location at which this objective must be accomplished,if there is a location defined.  Look up the DestinyLocationDefinition for this hash for thatadditional location info.

        :return: The location_hash of this DestinyDefinitionsDestinyObjectiveDefinition.
        :rtype: int
        """
        return self._location_hash

    @location_hash.setter
    def location_hash(self, location_hash):
        """
        Sets the location_hash of this DestinyDefinitionsDestinyObjectiveDefinition.
        OPTIONAL: a hash identifier for the location at which this objective must be accomplished,if there is a location defined.  Look up the DestinyLocationDefinition for this hash for thatadditional location info.

        :param location_hash: The location_hash of this DestinyDefinitionsDestinyObjectiveDefinition.
        :type: int
        """

        self._location_hash = location_hash

    @property
    def allow_negative_value(self):
        """
        Gets the allow_negative_value of this DestinyDefinitionsDestinyObjectiveDefinition.
        If true, the value is allowed to go negative.

        :return: The allow_negative_value of this DestinyDefinitionsDestinyObjectiveDefinition.
        :rtype: bool
        """
        return self._allow_negative_value

    @allow_negative_value.setter
    def allow_negative_value(self, allow_negative_value):
        """
        Sets the allow_negative_value of this DestinyDefinitionsDestinyObjectiveDefinition.
        If true, the value is allowed to go negative.

        :param allow_negative_value: The allow_negative_value of this DestinyDefinitionsDestinyObjectiveDefinition.
        :type: bool
        """

        self._allow_negative_value = allow_negative_value

    @property
    def allow_value_change_when_completed(self):
        """
        Gets the allow_value_change_when_completed of this DestinyDefinitionsDestinyObjectiveDefinition.
        If true, you can effectively \"un-complete\" this objective if you lose progress aftercrossing the completion threshold.    If False, once you complete the task it will remaincompleted forever by locking the value.

        :return: The allow_value_change_when_completed of this DestinyDefinitionsDestinyObjectiveDefinition.
        :rtype: bool
        """
        return self._allow_value_change_when_completed

    @allow_value_change_when_completed.setter
    def allow_value_change_when_completed(self, allow_value_change_when_completed):
        """
        Sets the allow_value_change_when_completed of this DestinyDefinitionsDestinyObjectiveDefinition.
        If true, you can effectively \"un-complete\" this objective if you lose progress aftercrossing the completion threshold.    If False, once you complete the task it will remaincompleted forever by locking the value.

        :param allow_value_change_when_completed: The allow_value_change_when_completed of this DestinyDefinitionsDestinyObjectiveDefinition.
        :type: bool
        """

        self._allow_value_change_when_completed = allow_value_change_when_completed

    @property
    def is_counting_downward(self):
        """
        Gets the is_counting_downward of this DestinyDefinitionsDestinyObjectiveDefinition.
        If true, completion means having an unlock value less than or equal to the completionValue.  If False, completion means having an unlock value greater than or equal to the completionValue.

        :return: The is_counting_downward of this DestinyDefinitionsDestinyObjectiveDefinition.
        :rtype: bool
        """
        return self._is_counting_downward

    @is_counting_downward.setter
    def is_counting_downward(self, is_counting_downward):
        """
        Sets the is_counting_downward of this DestinyDefinitionsDestinyObjectiveDefinition.
        If true, completion means having an unlock value less than or equal to the completionValue.  If False, completion means having an unlock value greater than or equal to the completionValue.

        :param is_counting_downward: The is_counting_downward of this DestinyDefinitionsDestinyObjectiveDefinition.
        :type: bool
        """

        self._is_counting_downward = is_counting_downward

    @property
    def progress_description(self):
        """
        Gets the progress_description of this DestinyDefinitionsDestinyObjectiveDefinition.
        Text to describe the progress bar.

        :return: The progress_description of this DestinyDefinitionsDestinyObjectiveDefinition.
        :rtype: str
        """
        return self._progress_description

    @progress_description.setter
    def progress_description(self, progress_description):
        """
        Sets the progress_description of this DestinyDefinitionsDestinyObjectiveDefinition.
        Text to describe the progress bar.

        :param progress_description: The progress_description of this DestinyDefinitionsDestinyObjectiveDefinition.
        :type: str
        """

        self._progress_description = progress_description

    @property
    def hash(self):
        """
        Gets the hash of this DestinyDefinitionsDestinyObjectiveDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :return: The hash of this DestinyDefinitionsDestinyObjectiveDefinition.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this DestinyDefinitionsDestinyObjectiveDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :param hash: The hash of this DestinyDefinitionsDestinyObjectiveDefinition.
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """
        Gets the index of this DestinyDefinitionsDestinyObjectiveDefinition.
        The index of the entity as it was found in the investment tables.

        :return: The index of this DestinyDefinitionsDestinyObjectiveDefinition.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this DestinyDefinitionsDestinyObjectiveDefinition.
        The index of the entity as it was found in the investment tables.

        :param index: The index of this DestinyDefinitionsDestinyObjectiveDefinition.
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """
        Gets the redacted of this DestinyDefinitionsDestinyObjectiveDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :return: The redacted of this DestinyDefinitionsDestinyObjectiveDefinition.
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """
        Sets the redacted of this DestinyDefinitionsDestinyObjectiveDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :param redacted: The redacted of this DestinyDefinitionsDestinyObjectiveDefinition.
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
        if not isinstance(other, DestinyDefinitionsDestinyObjectiveDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other