// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from msg_interfaces:srv/CommandGUI.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__TRAITS_HPP_
#define MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "msg_interfaces/srv/detail/command_gui__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'command'
#include "std_msgs/msg/detail/string__traits.hpp"

namespace msg_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const CommandGUI_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: command
  {
    out << "command: ";
    to_flow_style_yaml(msg.command, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CommandGUI_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "command:\n";
    to_block_style_yaml(msg.command, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CommandGUI_Request & msg, bool use_flow_style = false)
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
  const msg_interfaces::srv::CommandGUI_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  msg_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use msg_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const msg_interfaces::srv::CommandGUI_Request & msg)
{
  return msg_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<msg_interfaces::srv::CommandGUI_Request>()
{
  return "msg_interfaces::srv::CommandGUI_Request";
}

template<>
inline const char * name<msg_interfaces::srv::CommandGUI_Request>()
{
  return "msg_interfaces/srv/CommandGUI_Request";
}

template<>
struct has_fixed_size<msg_interfaces::srv::CommandGUI_Request>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::String>::value> {};

template<>
struct has_bounded_size<msg_interfaces::srv::CommandGUI_Request>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::String>::value> {};

template<>
struct is_message<msg_interfaces::srv::CommandGUI_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'res'
#include "std_msgs/msg/detail/int64__traits.hpp"

namespace msg_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const CommandGUI_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: res
  {
    out << "res: ";
    to_flow_style_yaml(msg.res, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CommandGUI_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: res
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "res:\n";
    to_block_style_yaml(msg.res, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CommandGUI_Response & msg, bool use_flow_style = false)
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
  const msg_interfaces::srv::CommandGUI_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  msg_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use msg_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const msg_interfaces::srv::CommandGUI_Response & msg)
{
  return msg_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<msg_interfaces::srv::CommandGUI_Response>()
{
  return "msg_interfaces::srv::CommandGUI_Response";
}

template<>
inline const char * name<msg_interfaces::srv::CommandGUI_Response>()
{
  return "msg_interfaces/srv/CommandGUI_Response";
}

template<>
struct has_fixed_size<msg_interfaces::srv::CommandGUI_Response>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Int64>::value> {};

template<>
struct has_bounded_size<msg_interfaces::srv::CommandGUI_Response>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Int64>::value> {};

template<>
struct is_message<msg_interfaces::srv::CommandGUI_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<msg_interfaces::srv::CommandGUI>()
{
  return "msg_interfaces::srv::CommandGUI";
}

template<>
inline const char * name<msg_interfaces::srv::CommandGUI>()
{
  return "msg_interfaces/srv/CommandGUI";
}

template<>
struct has_fixed_size<msg_interfaces::srv::CommandGUI>
  : std::integral_constant<
    bool,
    has_fixed_size<msg_interfaces::srv::CommandGUI_Request>::value &&
    has_fixed_size<msg_interfaces::srv::CommandGUI_Response>::value
  >
{
};

template<>
struct has_bounded_size<msg_interfaces::srv::CommandGUI>
  : std::integral_constant<
    bool,
    has_bounded_size<msg_interfaces::srv::CommandGUI_Request>::value &&
    has_bounded_size<msg_interfaces::srv::CommandGUI_Response>::value
  >
{
};

template<>
struct is_service<msg_interfaces::srv::CommandGUI>
  : std::true_type
{
};

template<>
struct is_service_request<msg_interfaces::srv::CommandGUI_Request>
  : std::true_type
{
};

template<>
struct is_service_response<msg_interfaces::srv::CommandGUI_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__TRAITS_HPP_
