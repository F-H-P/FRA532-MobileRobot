// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from msg_interfaces:srv/GoalPath.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__GOAL_PATH__BUILDER_HPP_
#define MSG_INTERFACES__SRV__DETAIL__GOAL_PATH__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "msg_interfaces/srv/detail/goal_path__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace msg_interfaces
{

namespace srv
{

namespace builder
{

class Init_GoalPath_Request_y_path
{
public:
  explicit Init_GoalPath_Request_y_path(::msg_interfaces::srv::GoalPath_Request & msg)
  : msg_(msg)
  {}
  ::msg_interfaces::srv::GoalPath_Request y_path(::msg_interfaces::srv::GoalPath_Request::_y_path_type arg)
  {
    msg_.y_path = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_interfaces::srv::GoalPath_Request msg_;
};

class Init_GoalPath_Request_x_path
{
public:
  Init_GoalPath_Request_x_path()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoalPath_Request_y_path x_path(::msg_interfaces::srv::GoalPath_Request::_x_path_type arg)
  {
    msg_.x_path = std::move(arg);
    return Init_GoalPath_Request_y_path(msg_);
  }

private:
  ::msg_interfaces::srv::GoalPath_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_interfaces::srv::GoalPath_Request>()
{
  return msg_interfaces::srv::builder::Init_GoalPath_Request_x_path();
}

}  // namespace msg_interfaces


namespace msg_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_interfaces::srv::GoalPath_Response>()
{
  return ::msg_interfaces::srv::GoalPath_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__SRV__DETAIL__GOAL_PATH__BUILDER_HPP_
