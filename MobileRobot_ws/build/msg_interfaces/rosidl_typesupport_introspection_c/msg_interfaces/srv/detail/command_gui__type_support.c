// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from msg_interfaces:srv/CommandGUI.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "msg_interfaces/srv/detail/command_gui__rosidl_typesupport_introspection_c.h"
#include "msg_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "msg_interfaces/srv/detail/command_gui__functions.h"
#include "msg_interfaces/srv/detail/command_gui__struct.h"


// Include directives for member types
// Member `command`
#include "std_msgs/msg/string.h"
// Member `command`
#include "std_msgs/msg/detail/string__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  msg_interfaces__srv__CommandGUI_Request__init(message_memory);
}

void msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_fini_function(void * message_memory)
{
  msg_interfaces__srv__CommandGUI_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_message_member_array[1] = {
  {
    "command",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(msg_interfaces__srv__CommandGUI_Request, command),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_message_members = {
  "msg_interfaces__srv",  // message namespace
  "CommandGUI_Request",  // message name
  1,  // number of fields
  sizeof(msg_interfaces__srv__CommandGUI_Request),
  msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_message_member_array,  // message members
  msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_message_type_support_handle = {
  0,
  &msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_msg_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, msg_interfaces, srv, CommandGUI_Request)() {
  msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, String)();
  if (!msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_message_type_support_handle.typesupport_identifier) {
    msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &msg_interfaces__srv__CommandGUI_Request__rosidl_typesupport_introspection_c__CommandGUI_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "msg_interfaces/srv/detail/command_gui__rosidl_typesupport_introspection_c.h"
// already included above
// #include "msg_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "msg_interfaces/srv/detail/command_gui__functions.h"
// already included above
// #include "msg_interfaces/srv/detail/command_gui__struct.h"


// Include directives for member types
// Member `res`
#include "std_msgs/msg/int64.h"
// Member `res`
#include "std_msgs/msg/detail/int64__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  msg_interfaces__srv__CommandGUI_Response__init(message_memory);
}

void msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_fini_function(void * message_memory)
{
  msg_interfaces__srv__CommandGUI_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_message_member_array[1] = {
  {
    "res",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(msg_interfaces__srv__CommandGUI_Response, res),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_message_members = {
  "msg_interfaces__srv",  // message namespace
  "CommandGUI_Response",  // message name
  1,  // number of fields
  sizeof(msg_interfaces__srv__CommandGUI_Response),
  msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_message_member_array,  // message members
  msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_message_type_support_handle = {
  0,
  &msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_msg_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, msg_interfaces, srv, CommandGUI_Response)() {
  msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Int64)();
  if (!msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_message_type_support_handle.typesupport_identifier) {
    msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &msg_interfaces__srv__CommandGUI_Response__rosidl_typesupport_introspection_c__CommandGUI_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "msg_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "msg_interfaces/srv/detail/command_gui__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers msg_interfaces__srv__detail__command_gui__rosidl_typesupport_introspection_c__CommandGUI_service_members = {
  "msg_interfaces__srv",  // service namespace
  "CommandGUI",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // msg_interfaces__srv__detail__command_gui__rosidl_typesupport_introspection_c__CommandGUI_Request_message_type_support_handle,
  NULL  // response message
  // msg_interfaces__srv__detail__command_gui__rosidl_typesupport_introspection_c__CommandGUI_Response_message_type_support_handle
};

static rosidl_service_type_support_t msg_interfaces__srv__detail__command_gui__rosidl_typesupport_introspection_c__CommandGUI_service_type_support_handle = {
  0,
  &msg_interfaces__srv__detail__command_gui__rosidl_typesupport_introspection_c__CommandGUI_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, msg_interfaces, srv, CommandGUI_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, msg_interfaces, srv, CommandGUI_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_msg_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, msg_interfaces, srv, CommandGUI)() {
  if (!msg_interfaces__srv__detail__command_gui__rosidl_typesupport_introspection_c__CommandGUI_service_type_support_handle.typesupport_identifier) {
    msg_interfaces__srv__detail__command_gui__rosidl_typesupport_introspection_c__CommandGUI_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)msg_interfaces__srv__detail__command_gui__rosidl_typesupport_introspection_c__CommandGUI_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, msg_interfaces, srv, CommandGUI_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, msg_interfaces, srv, CommandGUI_Response)()->data;
  }

  return &msg_interfaces__srv__detail__command_gui__rosidl_typesupport_introspection_c__CommandGUI_service_type_support_handle;
}
