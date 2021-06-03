# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint
import re

import six

class CheckerIdDeviancesBody1(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'expression': 'object',
        'ignore_until': 'datetime'
    }

    attribute_map = {
        'expression': 'expression',
        'ignore_until': 'ignoreUntil'
    }

    def __init__(self, expression=None, ignore_until=None):   
        """CheckerIdDeviancesBody1 - a model defined in Swagger"""   
        self._expression = None
        self._ignore_until = None
        self.discriminator = None
        self.expression = expression
        self.ignore_until = ignore_until

    @property
    def expression(self):
        """Gets the expression of this CheckerIdDeviancesBody1.   


        :return: The expression of this CheckerIdDeviancesBody1.   
        :rtype: object
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this CheckerIdDeviancesBody1.


        :param expression: The expression of this CheckerIdDeviancesBody1.   
        :type: object
        """
        if expression is None:
            raise ValueError("Invalid value for `expression`, must not be `None`")   

        self._expression = expression

    @property
    def ignore_until(self):
        """Gets the ignore_until of this CheckerIdDeviancesBody1.   


        :return: The ignore_until of this CheckerIdDeviancesBody1.   
        :rtype: datetime
        """
        return self._ignore_until

    @ignore_until.setter
    def ignore_until(self, ignore_until):
        """Sets the ignore_until of this CheckerIdDeviancesBody1.


        :param ignore_until: The ignore_until of this CheckerIdDeviancesBody1.   
        :type: datetime
        """
        if ignore_until is None:
            raise ValueError("Invalid value for `ignore_until`, must not be `None`")   

        self._ignore_until = ignore_until

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CheckerIdDeviancesBody1, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CheckerIdDeviancesBody1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
