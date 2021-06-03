# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint
import re

import six

class ApicheckersAttackerKnownTools(object):
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
        'name': 'str',
        'url': 'str',
        'author': 'str'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url',
        'author': 'author'
    }

    def __init__(self, name=None, url=None, author=None):   
        """ApicheckersAttackerKnownTools - a model defined in Swagger"""   
        self._name = None
        self._url = None
        self._author = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if author is not None:
            self.author = author

    @property
    def name(self):
        """Gets the name of this ApicheckersAttackerKnownTools.   


        :return: The name of this ApicheckersAttackerKnownTools.   
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApicheckersAttackerKnownTools.


        :param name: The name of this ApicheckersAttackerKnownTools.   
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this ApicheckersAttackerKnownTools.   


        :return: The url of this ApicheckersAttackerKnownTools.   
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ApicheckersAttackerKnownTools.


        :param url: The url of this ApicheckersAttackerKnownTools.   
        :type: str
        """

        self._url = url

    @property
    def author(self):
        """Gets the author of this ApicheckersAttackerKnownTools.   


        :return: The author of this ApicheckersAttackerKnownTools.   
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ApicheckersAttackerKnownTools.


        :param author: The author of this ApicheckersAttackerKnownTools.   
        :type: str
        """

        self._author = author

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
        if issubclass(ApicheckersAttackerKnownTools, dict):
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
        if not isinstance(other, ApicheckersAttackerKnownTools):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
