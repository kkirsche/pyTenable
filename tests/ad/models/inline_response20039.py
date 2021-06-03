# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint
import re

import six

class InlineResponse20039(object):
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
        'id': 'int',
        'ip': 'str',
        'port': 'int',
        'protocol': 'str',
        'tls': 'bool',
        'criticity_threshold': 'int',
        'description': 'str',
        'filter_expression': 'object',
        'input_type': 'str',
        'directories': 'list[int]',
        'checkers': 'list[int]',
        'attack_types': 'list[int]',
        'profiles': 'list[int]',
        'should_notify_on_initial_full_security_check': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'ip': 'ip',
        'port': 'port',
        'protocol': 'protocol',
        'tls': 'tls',
        'criticity_threshold': 'criticityThreshold',
        'description': 'description',
        'filter_expression': 'filterExpression',
        'input_type': 'inputType',
        'directories': 'directories',
        'checkers': 'checkers',
        'attack_types': 'attackTypes',
        'profiles': 'profiles',
        'should_notify_on_initial_full_security_check': 'shouldNotifyOnInitialFullSecurityCheck'
    }

    def __init__(self, id=None, ip=None, port=None, protocol=None, tls=None, criticity_threshold=None, description=None, filter_expression=None, input_type=None, directories=None, checkers=None, attack_types=None, profiles=None, should_notify_on_initial_full_security_check=None):   
        """InlineResponse20039 - a model defined in Swagger"""   
        self._id = None
        self._ip = None
        self._port = None
        self._protocol = None
        self._tls = None
        self._criticity_threshold = None
        self._description = None
        self._filter_expression = None
        self._input_type = None
        self._directories = None
        self._checkers = None
        self._attack_types = None
        self._profiles = None
        self._should_notify_on_initial_full_security_check = None
        self.discriminator = None
        self.id = id
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.tls = tls
        self.criticity_threshold = criticity_threshold
        if description is not None:
            self.description = description
        if filter_expression is not None:
            self.filter_expression = filter_expression
        if input_type is not None:
            self.input_type = input_type
        self.directories = directories
        self.checkers = checkers
        self.attack_types = attack_types
        self.profiles = profiles
        self.should_notify_on_initial_full_security_check = should_notify_on_initial_full_security_check

    @property
    def id(self):
        """Gets the id of this InlineResponse20039.   


        :return: The id of this InlineResponse20039.   
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20039.


        :param id: The id of this InlineResponse20039.   
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")   

        self._id = id

    @property
    def ip(self):
        """Gets the ip of this InlineResponse20039.   


        :return: The ip of this InlineResponse20039.   
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this InlineResponse20039.


        :param ip: The ip of this InlineResponse20039.   
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")   

        self._ip = ip

    @property
    def port(self):
        """Gets the port of this InlineResponse20039.   


        :return: The port of this InlineResponse20039.   
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this InlineResponse20039.


        :param port: The port of this InlineResponse20039.   
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")   

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this InlineResponse20039.   


        :return: The protocol of this InlineResponse20039.   
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this InlineResponse20039.


        :param protocol: The protocol of this InlineResponse20039.   
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")   
        allowed_values = ["UDP", "TCP"]   
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"   
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def tls(self):
        """Gets the tls of this InlineResponse20039.   


        :return: The tls of this InlineResponse20039.   
        :rtype: bool
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this InlineResponse20039.


        :param tls: The tls of this InlineResponse20039.   
        :type: bool
        """
        if tls is None:
            raise ValueError("Invalid value for `tls`, must not be `None`")   

        self._tls = tls

    @property
    def criticity_threshold(self):
        """Gets the criticity_threshold of this InlineResponse20039.   


        :return: The criticity_threshold of this InlineResponse20039.   
        :rtype: int
        """
        return self._criticity_threshold

    @criticity_threshold.setter
    def criticity_threshold(self, criticity_threshold):
        """Sets the criticity_threshold of this InlineResponse20039.


        :param criticity_threshold: The criticity_threshold of this InlineResponse20039.   
        :type: int
        """
        if criticity_threshold is None:
            raise ValueError("Invalid value for `criticity_threshold`, must not be `None`")   

        self._criticity_threshold = criticity_threshold

    @property
    def description(self):
        """Gets the description of this InlineResponse20039.   


        :return: The description of this InlineResponse20039.   
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20039.


        :param description: The description of this InlineResponse20039.   
        :type: str
        """

        self._description = description

    @property
    def filter_expression(self):
        """Gets the filter_expression of this InlineResponse20039.   


        :return: The filter_expression of this InlineResponse20039.   
        :rtype: object
        """
        return self._filter_expression

    @filter_expression.setter
    def filter_expression(self, filter_expression):
        """Sets the filter_expression of this InlineResponse20039.


        :param filter_expression: The filter_expression of this InlineResponse20039.   
        :type: object
        """

        self._filter_expression = filter_expression

    @property
    def input_type(self):
        """Gets the input_type of this InlineResponse20039.   


        :return: The input_type of this InlineResponse20039.   
        :rtype: str
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        """Sets the input_type of this InlineResponse20039.


        :param input_type: The input_type of this InlineResponse20039.   
        :type: str
        """
        allowed_values = ["deviances", "adObjectChanges", "attacks"]   
        if input_type not in allowed_values:
            raise ValueError(
                "Invalid value for `input_type` ({0}), must be one of {1}"   
                .format(input_type, allowed_values)
            )

        self._input_type = input_type

    @property
    def directories(self):
        """Gets the directories of this InlineResponse20039.   


        :return: The directories of this InlineResponse20039.   
        :rtype: list[int]
        """
        return self._directories

    @directories.setter
    def directories(self, directories):
        """Sets the directories of this InlineResponse20039.


        :param directories: The directories of this InlineResponse20039.   
        :type: list[int]
        """
        if directories is None:
            raise ValueError("Invalid value for `directories`, must not be `None`")   

        self._directories = directories

    @property
    def checkers(self):
        """Gets the checkers of this InlineResponse20039.   


        :return: The checkers of this InlineResponse20039.   
        :rtype: list[int]
        """
        return self._checkers

    @checkers.setter
    def checkers(self, checkers):
        """Sets the checkers of this InlineResponse20039.


        :param checkers: The checkers of this InlineResponse20039.   
        :type: list[int]
        """
        if checkers is None:
            raise ValueError("Invalid value for `checkers`, must not be `None`")   

        self._checkers = checkers

    @property
    def attack_types(self):
        """Gets the attack_types of this InlineResponse20039.   


        :return: The attack_types of this InlineResponse20039.   
        :rtype: list[int]
        """
        return self._attack_types

    @attack_types.setter
    def attack_types(self, attack_types):
        """Sets the attack_types of this InlineResponse20039.


        :param attack_types: The attack_types of this InlineResponse20039.   
        :type: list[int]
        """
        if attack_types is None:
            raise ValueError("Invalid value for `attack_types`, must not be `None`")   

        self._attack_types = attack_types

    @property
    def profiles(self):
        """Gets the profiles of this InlineResponse20039.   


        :return: The profiles of this InlineResponse20039.   
        :rtype: list[int]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this InlineResponse20039.


        :param profiles: The profiles of this InlineResponse20039.   
        :type: list[int]
        """
        if profiles is None:
            raise ValueError("Invalid value for `profiles`, must not be `None`")   

        self._profiles = profiles

    @property
    def should_notify_on_initial_full_security_check(self):
        """Gets the should_notify_on_initial_full_security_check of this InlineResponse20039.   


        :return: The should_notify_on_initial_full_security_check of this InlineResponse20039.   
        :rtype: bool
        """
        return self._should_notify_on_initial_full_security_check

    @should_notify_on_initial_full_security_check.setter
    def should_notify_on_initial_full_security_check(self, should_notify_on_initial_full_security_check):
        """Sets the should_notify_on_initial_full_security_check of this InlineResponse20039.


        :param should_notify_on_initial_full_security_check: The should_notify_on_initial_full_security_check of this InlineResponse20039.   
        :type: bool
        """
        if should_notify_on_initial_full_security_check is None:
            raise ValueError("Invalid value for `should_notify_on_initial_full_security_check`, must not be `None`")   

        self._should_notify_on_initial_full_security_check = should_notify_on_initial_full_security_check

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
        if issubclass(InlineResponse20039, dict):
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
        if not isinstance(other, InlineResponse20039):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
