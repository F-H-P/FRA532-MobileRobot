// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from msg_interfaces:srv/CommandGUI.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__STRUCT_H_
#define MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'command'
#include "std_msgs/msg/detail/string__struct.h"

/// Struct defined in srv/CommandGUI in the package msg_interfaces.
typedef struct msg_interfaces__srv__CommandGUI_Request
{
  std_msgs__msg__String command;
} msg_interfaces__srv__CommandGUI_Request;

// Struct for a sequence of msg_interfaces__srv__CommandGUI_Request.
typedef struct msg_interfaces__srv__CommandGUI_Request__Sequence
{
  msg_interfaces__srv__CommandGUI_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_interfaces__srv__CommandGUI_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'res'
#include "std_msgs/msg/detail/int64__struct.h"

/// Struct defined in srv/CommandGUI in the package msg_interfaces.
typedef struct msg_interfaces__srv__CommandGUI_Response
{
  std_msgs__msg__Int64 res;
} msg_interfaces__srv__CommandGUI_Response;

// Struct for a sequence of msg_interfaces__srv__CommandGUI_Response.
typedef struct msg_interfaces__srv__CommandGUI_Response__Sequence
{
  msg_interfaces__srv__CommandGUI_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_interfaces__srv__CommandGUI_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__STRUCT_H_
