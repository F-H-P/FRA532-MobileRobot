// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from megarover_samples_ros2:srv/GoalPath.idl
// generated code does not contain a copyright notice

#ifndef MEGAROVER_SAMPLES_ROS2__SRV__DETAIL__GOAL_PATH__TRAITS_HPP_
#define MEGAROVER_SAMPLES_ROS2__SRV__DETAIL__GOAL_PATH__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "megarover_samples_ros2/srv/detail/goal_path__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'x_path'
// Member 'y_path'
#include "std_msgs/msg/detail/float64_multi_array__traits.hpp"

namespace megarover_samples_ros2
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

}  // namespace megarover_samples_ros2

namespace rosidl_generator_traits
{

[[deprecated("use megarover_samples_ros2::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const megarover_samples_ros2::srv::GoalPath_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  megarover_samples_ros2::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use megarover_samples_ros2::srv::to_yaml() instead")]]
inline std::string to_yaml(const megarover_samples_ros2::srv::GoalPath_Request & msg)
{
  return megarover_samples_ros2::srv::to_yaml(msg);
}

template<>
inline const char * data_type<megarover_samples_ros2::srv::GoalPath_Request>()
{
  return "megarover_samples_ros2::srv::GoalPath_Request";
}

template<>
inline const char * name<megarover_samples_ros2::srv::GoalPath_Request>()
{
  return "megarover_samples_ros2/srv/GoalPath_Request";
}

template<>
struct has_fixed_size<megarover_samples_ros2::srv::GoalPath_Request>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Float64MultiArray>::value> {};

template<>
struct has_bounded_size<megarover_samples_ros2::srv::GoalPath_Request>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Float64MultiArray>::value> {};

template<>
struct is_message<megarover_samples_ros2::srv::GoalPath_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace megarover_samples_ros2
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

}  // namespace megarover_samples_ros2

namespace rosidl_generator_traits
{

[[deprecated("use megarover_samples_ros2::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const megarover_samples_ros2::srv::GoalPath_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  megarover_samples_ros2::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use megarover_samples_ros2::srv::to_yaml() instead")]]
inline std::string to_yaml(const megarover_samples_ros2::srv::GoalPath_Response & msg)
{
  return megarover_samples_ros2::srv::to_yaml(msg);
}

template<>
inline const char * data_type<megarover_samples_ros2::srv::GoalPath_Response>()
{
  return "megarover_samples_ros2::srv::GoalPath_Response";
}

template<>
inline const char * name<megarover_samples_ros2::srv::GoalPath_Response>()
{
  return "megarover_samples_ros2/srv/GoalPath_Response";
}

template<>
struct has_fixed_size<megarover_samples_ros2::srv::GoalPath_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<megarover_samples_ros2::srv::GoalPath_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<megarover_samples_ros2::srv::GoalPath_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<megarover_samples_ros2::srv::GoalPath>()
{
  return "megarover_samples_ros2::srv::GoalPath";
}

template<>
inline const char * name<megarover_samples_ros2::srv::GoalPath>()
{
  return "megarover_samples_ros2/srv/GoalPath";
}

template<>
struct has_fixed_size<megarover_samples_ros2::srv::GoalPath>
  : std::integral_constant<
    bool,
    has_fixed_size<megarover_samples_ros2::srv::GoalPath_Request>::value &&
    has_fixed_size<megarover_samples_ros2::srv::GoalPath_Response>::value
  >
{
};

template<>
struct has_bounded_size<megarover_samples_ros2::srv::GoalPath>
  : std::integral_constant<
    bool,
    has_bounded_size<megarover_samples_ros2::srv::GoalPath_Request>::value &&
    has_bounded_size<megarover_samples_ros2::srv::GoalPath_Response>::value
  >
{
};

template<>
struct is_service<megarover_samples_ros2::srv::GoalPath>
  : std::true_type
{
};

template<>
struct is_service_request<megarover_samples_ros2::srv::GoalPath_Request>
  : std::true_type
{
};

template<>
struct is_service_response<megarover_samples_ros2::srv::GoalPath_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MEGAROVER_SAMPLES_ROS2__SRV__DETAIL__GOAL_PATH__TRAITS_HPP_
