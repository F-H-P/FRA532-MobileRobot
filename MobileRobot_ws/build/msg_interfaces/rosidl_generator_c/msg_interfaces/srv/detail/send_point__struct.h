// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from msg_interfaces:srv/SendPoint.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__SEND_POINT__STRUCT_H_
#define MSG_INTERFACES__SRV__DETAIL__SEND_POINT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'start_x'
// Member 'start_y'
// Member 'goal_x'
// Member 'goal_y'
#include "std_msgs/msg/detail/float64__struct.h"

/// Struct defined in srv/SendPoint in the package msg_interfaces.
typedef struct msg_interfaces__srv__SendPoint_Request
{
  std_msgs__msg__Float64 start_x;
  std_msgs__msg__Float64 start_y;
  std_msgs__msg__Float64 goal_x;
  std_msgs__msg__Float64 goal_y;
} msg_interfaces__srv__SendPoint_Request;

// Struct for a sequence of msg_interfaces__srv__SendPoint_Request.
typedef struct msg_interfaces__srv__SendPoint_Request__Sequence
{
  msg_interfaces__srv__SendPoint_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_interfaces__srv__SendPoint_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SendPoint in the package msg_interfaces.
typedef struct msg_interfaces__srv__SendPoint_Response
{
  uint8_t structure_needs_at_least_one_member;
} msg_interfaces__srv__SendPoint_Response;

// Struct for a sequence of msg_interfaces__srv__SendPoint_Response.
typedef struct msg_interfaces__srv__SendPoint_Response__Sequence
{
  msg_interfaces__srv__SendPoint_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_interfaces__srv__SendPoint_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MSG_INTERFACES__SRV__DETAIL__SEND_POINT__STRUCT_H_
