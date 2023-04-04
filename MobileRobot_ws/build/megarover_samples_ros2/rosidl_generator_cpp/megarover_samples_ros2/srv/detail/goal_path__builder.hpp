// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from megarover_samples_ros2:srv/GoalPath.idl
// generated code does not contain a copyright notice

#ifndef MEGAROVER_SAMPLES_ROS2__SRV__DETAIL__GOAL_PATH__BUILDER_HPP_
#define MEGAROVER_SAMPLES_ROS2__SRV__DETAIL__GOAL_PATH__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "megarover_samples_ros2/srv/detail/goal_path__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace megarover_samples_ros2
{

namespace srv
{

namespace builder
{

class Init_GoalPath_Request_y_path
{
public:
  explicit Init_GoalPath_Request_y_path(::megarover_samples_ros2::srv::GoalPath_Request & msg)
  : msg_(msg)
  {}
  ::megarover_samples_ros2::srv::GoalPath_Request y_path(::megarover_samples_ros2::srv::GoalPath_Request::_y_path_type arg)
  {
    msg_.y_path = std::move(arg);
    return std::move(msg_);
  }

private:
  ::megarover_samples_ros2::srv::GoalPath_Request msg_;
};

class Init_GoalPath_Request_x_path
{
public:
  Init_GoalPath_Request_x_path()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoalPath_Request_y_path x_path(::megarover_samples_ros2::srv::GoalPath_Request::_x_path_type arg)
  {
    msg_.x_path = std::move(arg);
    return Init_GoalPath_Request_y_path(msg_);
  }

private:
  ::megarover_samples_ros2::srv::GoalPath_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::megarover_samples_ros2::srv::GoalPath_Request>()
{
  return megarover_samples_ros2::srv::builder::Init_GoalPath_Request_x_path();
}

}  // namespace megarover_samples_ros2


namespace megarover_samples_ros2
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::megarover_samples_ros2::srv::GoalPath_Response>()
{
  return ::megarover_samples_ros2::srv::GoalPath_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace megarover_samples_ros2

#endif  // MEGAROVER_SAMPLES_ROS2__SRV__DETAIL__GOAL_PATH__BUILDER_HPP_
