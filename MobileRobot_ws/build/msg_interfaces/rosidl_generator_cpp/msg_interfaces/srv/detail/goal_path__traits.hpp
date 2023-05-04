// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from msg_interfaces:srv/GoalPath.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__GOAL_PATH__TRAITS_HPP_
#define MSG_INTERFACES__SRV__DETAIL__GOAL_PATH__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "msg_interfaces/srv/detail/goal_path__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'x_path'
// Member 'y_path'
#include "std_msgs/msg/detail/float64_multi_array__traits.hpp"

namespace msg_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const GoalPath_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: x_path
  {
    out << "x_path: ";
    to_flow_style_yaml(msg.x_path, out);
    out << ", ";
  }

  // member: y_path
  {
    out << "y_path: ";
    to_flow_style_yaml(msg.y_path, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GoalPath_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: x_path
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_path:\n";
    to_block_style_yaml(msg.x_path, out, indentation + 2);
  }

  // member: y_path
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_path:\n";
    to_block_style_yaml(msg.y_path, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GoalPath_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace msg_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use msg_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const msg_interfaces::srv::GoalPath_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  msg_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use msg_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const msg_interfaces::srv::GoalPath_Request & msg)
{
  return msg_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<msg_interfaces::srv::GoalPath_Request>()
{
  return "msg_interfaces::srv::GoalPath_Request";
}

template<>
inline const char * name<msg_interfaces::srv::GoalPath_Request>()
{
  return "msg_interfaces/srv/GoalPath_Request";
}

template<>
struct has_fixed_size<msg_interfaces::srv::GoalPath_Request>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Float64MultiArray>::value> {};

template<>
struct has_bounded_size<msg_interfaces::srv::GoalPath_Request>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Float64MultiArray>::value> {};

template<>
struct is_message<msg_interfaces::srv::GoalPath_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace msg_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const GoalPath_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GoalPath_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GoalPath_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace msg_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use msg_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const msg_interfaces::srv::GoalPath_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  msg_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use msg_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const msg_interfaces::srv::GoalPath_Response & msg)
{
  return msg_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<msg_interfaces::srv::GoalPath_Response>()
{
  return "msg_interfaces::srv::GoalPath_Response";
}

template<>
inline const char * name<msg_interfaces::srv::GoalPath_Response>()
{
  return "msg_interfaces/srv/GoalPath_Response";
}

template<>
struct has_fixed_size<msg_interfaces::srv::GoalPath_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<msg_interfaces::srv::GoalPath_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<msg_interfaces::srv::GoalPath_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<msg_interfaces::srv::GoalPath>()
{
  return "msg_interfaces::srv::GoalPath";
}

template<>
inline const char * name<msg_interfaces::srv::GoalPath>()
{
  return "msg_interfaces/srv/GoalPath";
}

template<>
struct has_fixed_size<msg_interfaces::srv::GoalPath>
  : std::integral_constant<
    bool,
    has_fixed_size<msg_interfaces::srv::GoalPath_Request>::value &&
    has_fixed_size<msg_interfaces::srv::GoalPath_Response>::value
  >
{
};

template<>
struct has_bounded_size<msg_interfaces::srv::GoalPath>
  : std::integral_constant<
    bool,
    has_bounded_size<msg_interfaces::srv::GoalPath_Request>::value &&
    has_bounded_size<msg_interfaces::srv::GoalPath_Response>::value
  >
{
};

template<>
struct is_service<msg_interfaces::srv::GoalPath>
  : std::true_type
{
};

template<>
struct is_service_request<msg_interfaces::srv::GoalPath_Request>
  : std::true_type
{
};

template<>
struct is_service_response<msg_interfaces::srv::GoalPath_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MSG_INTERFACES__SRV__DETAIL__GOAL_PATH__TRAITS_HPP_
