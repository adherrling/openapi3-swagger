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


class DestinyEntitiesProfilesDestinyVendorReceiptsComponent(object):
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
        'receipts': 'list[ComponentsschemasDestinyVendorsDestinyVendorReceipt]'
    }

    attribute_map = {
        'receipts': 'receipts'
    }

    def __init__(self, receipts=None):
        """
        DestinyEntitiesProfilesDestinyVendorReceiptsComponent - a model defined in Swagger
        """

        self._receipts = None
        self.discriminator = None

        if receipts is not None:
          self.receipts = receipts

    @property
    def receipts(self):
        """
        Gets the receipts of this DestinyEntitiesProfilesDestinyVendorReceiptsComponent.
        The receipts for refundable purchases made at a vendor.

        :return: The receipts of this DestinyEntitiesProfilesDestinyVendorReceiptsComponent.
        :rtype: list[ComponentsschemasDestinyVendorsDestinyVendorReceipt]
        """
        return self._receipts

    @receipts.setter
    def receipts(self, receipts):
        """
        Sets the receipts of this DestinyEntitiesProfilesDestinyVendorReceiptsComponent.
        The receipts for refundable purchases made at a vendor.

        :param receipts: The receipts of this DestinyEntitiesProfilesDestinyVendorReceiptsComponent.
        :type: list[ComponentsschemasDestinyVendorsDestinyVendorReceipt]
        """

        self._receipts = receipts

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
        if not isinstance(other, DestinyEntitiesProfilesDestinyVendorReceiptsComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
