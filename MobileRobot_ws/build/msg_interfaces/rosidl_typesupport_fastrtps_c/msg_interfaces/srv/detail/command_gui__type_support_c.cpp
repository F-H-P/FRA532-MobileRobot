// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from msg_interfaces:srv/CommandGUI.idl
// generated code does not contain a copyright notice
#include "msg_interfaces/srv/detail/command_gui__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "msg_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "msg_interfaces/srv/detail/command_gui__struct.h"
#include "msg_interfaces/srv/detail/command_gui__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "std_msgs/msg/detail/string__functions.h"  // command

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_msg_interfaces
size_t get_serialized_size_std_msgs__msg__String(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_msg_interfaces
size_t max_serialized_size_std_msgs__msg__String(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_msg_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, String)();


using _CommandGUI_Request__ros_msg_type = msg_interfaces__srv__CommandGUI_Request;

static bool _CommandGUI_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _CommandGUI_Request__ros_msg_type * ros_message = static_cast<const _CommandGUI_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: command
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->command, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _CommandGUI_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _CommandGUI_Request__ros_msg_type * ros_message = static_cast<_CommandGUI_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: command
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->command))
    {
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_msg_interfaces
size_t get_serialized_size_msg_interfaces__srv__CommandGUI_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _CommandGUI_Request__ros_msg_type * ros_message = static_cast<const _CommandGUI_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name command

  current_alignment += get_serialized_size_std_msgs__msg__String(
    &(ros_message->command), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _CommandGUI_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_msg_interfaces__srv__CommandGUI_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_msg_interfaces
size_t max_serialized_size_msg_interfaces__srv__CommandGUI_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: command
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      current_alignment +=
        max_serialized_size_std_msgs__msg__String(
        inner_full_bounded, inner_is_plain, current_alignment);
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _CommandGUI_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_msg_interfaces__srv__CommandGUI_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_CommandGUI_Request = {
  "msg_interfaces::srv",
  "CommandGUI_Request",
  _CommandGUI_Request__cdr_serialize,
  _CommandGUI_Request__cdr_deserialize,
  _CommandGUI_Request__get_serialized_size,
  _CommandGUI_Request__max_serialized_size
};

static rosidl_message_type_support_t _CommandGUI_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_CommandGUI_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, msg_interfaces, srv, CommandGUI_Request)() {
  return &_CommandGUI_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "msg_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "msg_interfaces/srv/detail/command_gui__struct.h"
// already included above
// #include "msg_interfaces/srv/detail/command_gui__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "std_msgs/msg/detail/int64__functions.h"  // res

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_msg_interfaces
size_t get_serialized_size_std_msgs__msg__Int64(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_msg_interfaces
size_t max_serialized_size_std_msgs__msg__Int64(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_msg_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, Int64)();


using _CommandGUI_Response__ros_msg_type = msg_interfaces__srv__CommandGUI_Response;

static bool _CommandGUI_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _CommandGUI_Response__ros_msg_type * ros_message = static_cast<const _CommandGUI_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: res
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Int64
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->res, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _CommandGUI_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _CommandGUI_Response__ros_msg_type * ros_message = static_cast<_CommandGUI_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: res
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Int64
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->res))
    {
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_msg_interfaces
size_t get_serialized_size_msg_interfaces__srv__CommandGUI_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _CommandGUI_Response__ros_msg_type * ros_message = static_cast<const _CommandGUI_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name res

  current_alignment += get_serialized_size_std_msgs__msg__Int64(
    &(ros_message->res), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _CommandGUI_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_msg_interfaces__srv__CommandGUI_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_msg_interfaces
size_t max_serialized_size_msg_interfaces__srv__CommandGUI_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: res
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      current_alignment +=
        max_serialized_size_std_msgs__msg__Int64(
        inner_full_bounded, inner_is_plain, current_alignment);
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _CommandGUI_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_msg_interfaces__srv__CommandGUI_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_CommandGUI_Response = {
  "msg_interfaces::srv",
  "CommandGUI_Response",
  _CommandGUI_Response__cdr_serialize,
  _CommandGUI_Response__cdr_deserialize,
  _CommandGUI_Response__get_serialized_size,
  _CommandGUI_Response__max_serialized_size
};

static rosidl_message_type_support_t _CommandGUI_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_CommandGUI_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, msg_interfaces, srv, CommandGUI_Response)() {
  return &_CommandGUI_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "msg_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "msg_interfaces/srv/command_gui.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t CommandGUI__callbacks = {
  "msg_interfaces::srv",
  "CommandGUI",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, msg_interfaces, srv, CommandGUI_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, msg_interfaces, srv, CommandGUI_Response)(),
};

static rosidl_service_type_support_t CommandGUI__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &CommandGUI__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, msg_interfaces, srv, CommandGUI)() {
  return &CommandGUI__handle;
}

#if defined(__cplusplus)
}
#endif
