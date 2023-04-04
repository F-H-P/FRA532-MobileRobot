// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from msg_interfaces:srv/SendPoint.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__SEND_POINT__TRAITS_HPP_
#define MSG_INTERFACES__SRV__DETAIL__SEND_POINT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "msg_interfaces/srv/detail/send_point__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'start_x'
// Member 'start_y'
// Member 'goal_x'
// Member 'goal_y'
#include "std_msgs/msg/detail/float64__traits.hpp"

namespace msg_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SendPoint_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: start_x
  {
    out << "start_x: ";
    to_flow_style_yaml(msg.start_x, out);
    out << ", ";
  }

  // member: start_y
  {
    out << "start_y: ";
    to_flow_style_yaml(msg.start_y, out);
    out << ", ";
  }

  // member: goal_x
  {
    out << "goal_x: ";
    to_flow_style_yaml(msg.goal_x, out);
    out << ", ";
  }

  // member: goal_y
  {
    out << "goal_y: ";
    to_flow_style_yaml(msg.goal_y, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SendPoint_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: start_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "start_x:\n";
    to_block_style_yaml(msg.start_x, out, indentation + 2);
  }

  // member: start_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "start_y:\n";
    to_block_style_yaml(msg.start_y, out, indentation + 2);
  }

  // member: goal_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_x:\n";
    to_block_style_yaml(msg.goal_x, out, indentation + 2);
  }

  // member: goal_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_y:\n";
    to_block_style_yaml(msg.goal_y, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SendPoint_Request & msg, bool use_flow_style = false)
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
  const msg_interfaces::srv::SendPoint_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  msg_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use msg_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const msg_interfaces::srv::SendPoint_Request & msg)
{
  return msg_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<msg_interfaces::srv::SendPoint_Request>()
{
  return "msg_interfaces::srv::SendPoint_Request";
}

template<>
inline const char * name<msg_interfaces::srv::SendPoint_Request>()
{
  return "msg_interfaces/srv/SendPoint_Request";
}

template<>
struct has_fixed_size<msg_interfaces::srv::SendPoint_Request>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Float64>::value> {};

template<>
struct has_bounded_size<msg_interfaces::srv::SendPoint_Request>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Float64>::value> {};

template<>
struct is_message<msg_interfaces::srv::SendPoint_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace msg_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SendPoint_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SendPoint_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SendPoint_Response & msg, bool use_flow_style = false)
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
  const msg_interfaces::srv::SendPoint_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  msg_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use msg_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const msg_interfaces::srv::SendPoint_Response & msg)
{
  return msg_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<msg_interfaces::srv::SendPoint_Response>()
{
  return "msg_interfaces::srv::SendPoint_Response";
}

template<>
inline const char * name<msg_interfaces::srv::SendPoint_Response>()
{
  return "msg_interfaces/srv/SendPoint_Response";
}

template<>
struct has_fixed_size<msg_interfaces::srv::SendPoint_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<msg_interfaces::srv::SendPoint_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<msg_interfaces::srv::SendPoint_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<msg_interfaces::srv::SendPoint>()
{
  return "msg_interfaces::srv::SendPoint";
}

template<>
inline const char * name<msg_interfaces::srv::SendPoint>()
{
  return "msg_interfaces/srv/SendPoint";
}

template<>
struct has_fixed_size<msg_interfaces::srv::SendPoint>
  : std::integral_constant<
    bool,
    has_fixed_size<msg_interfaces::srv::SendPoint_Request>::value &&
    has_fixed_size<msg_interfaces::srv::SendPoint_Response>::value
  >
{
};

template<>
struct has_bounded_size<msg_interfaces::srv::SendPoint>
  : std::integral_constant<
    bool,
    has_bounded_size<msg_interfaces::srv::SendPoint_Request>::value &&
    has_bounded_size<msg_interfaces::srv::SendPoint_Response>::value
  >
{
};

template<>
struct is_service<msg_interfaces::srv::SendPoint>
  : std::true_type
{
};

template<>
struct is_service_request<msg_interfaces::srv::SendPoint_Request>
  : std::true_type
{
};

template<>
struct is_service_response<msg_interfaces::srv::SendPoint_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MSG_INTERFACES__SRV__DETAIL__SEND_POINT__TRAITS_HPP_
