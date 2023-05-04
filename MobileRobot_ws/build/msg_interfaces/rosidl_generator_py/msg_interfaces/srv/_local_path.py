# generated from rosidl_generator_py/resource/_idl.py.em
# with input from msg_interfaces:srv/LocalPath.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_LocalPath_Request(type):
    """Metaclass of message 'LocalPath_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('msg_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'msg_interfaces.srv.LocalPath_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__local_path__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__local_path__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__local_path__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__local_path__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__local_path__request

            from std_msgs.msg import Float64MultiArray
            if Float64MultiArray.__class__._TYPE_SUPPORT is None:
                Float64MultiArray.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class LocalPath_Request(metaclass=Metaclass_LocalPath_Request):
    """Message class 'LocalPath_Request'."""

    __slots__ = [
        '_x_path',
        '_y_path',
    ]

    _fields_and_field_types = {
        'x_path': 'std_msgs/Float64MultiArray',
        'y_path': 'std_msgs/Float64MultiArray',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float64MultiArray'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float64MultiArray'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Float64MultiArray
        self.x_path = kwargs.get('x_path', Float64MultiArray())
        from std_msgs.msg import Float64MultiArray
        self.y_path = kwargs.get('y_path', Float64MultiArray())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.x_path != other.x_path:
            return False
        if self.y_path != other.y_path:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def x_path(self):
        """Message field 'x_path'."""
        return self._x_path

    @x_path.setter
    def x_path(self, value):
        if __debug__:
            from std_msgs.msg import Float64MultiArray
            assert \
                isinstance(value, Float64MultiArray), \
                "The 'x_path' field must be a sub message of type 'Float64MultiArray'"
        self._x_path = value

    @builtins.property
    def y_path(self):
        """Message field 'y_path'."""
        return self._y_path

    @y_path.setter
    def y_path(self, value):
        if __debug__:
            from std_msgs.msg import Float64MultiArray
            assert \
                isinstance(value, Float64MultiArray), \
                "The 'y_path' field must be a sub message of type 'Float64MultiArray'"
        self._y_path = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_LocalPath_Response(type):
    """Metaclass of message 'LocalPath_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('msg_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'msg_interfaces.srv.LocalPath_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__local_path__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__local_path__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__local_path__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__local_path__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__local_path__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class LocalPath_Response(metaclass=Metaclass_LocalPath_Response):
    """Message class 'LocalPath_Response'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


class Metaclass_LocalPath(type):
    """Metaclass of service 'LocalPath'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('msg_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'msg_interfaces.srv.LocalPath')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__local_path

            from msg_interfaces.srv import _local_path
            if _local_path.Metaclass_LocalPath_Request._TYPE_SUPPORT is None:
                _local_path.Metaclass_LocalPath_Request.__import_type_support__()
            if _local_path.Metaclass_LocalPath_Response._TYPE_SUPPORT is None:
                _local_path.Metaclass_LocalPath_Response.__import_type_support__()


class LocalPath(metaclass=Metaclass_LocalPath):
    from msg_interfaces.srv._local_path import LocalPath_Request as Request
    from msg_interfaces.srv._local_path import LocalPath_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
