// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from msg_interfaces:srv/SendPoint.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__SEND_POINT__BUILDER_HPP_
#define MSG_INTERFACES__SRV__DETAIL__SEND_POINT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "msg_interfaces/srv/detail/send_point__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace msg_interfaces
{

namespace srv
{

namespace builder
{

class Init_SendPoint_Request_goal_y
{
public:
  explicit Init_SendPoint_Request_goal_y(::msg_interfaces::srv::SendPoint_Request & msg)
  : msg_(msg)
  {}
  ::msg_interfaces::srv::SendPoint_Request goal_y(::msg_interfaces::srv::SendPoint_Request::_goal_y_type arg)
  {
    msg_.goal_y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_interfaces::srv::SendPoint_Request msg_;
};

class Init_SendPoint_Request_goal_x
{
public:
  explicit Init_SendPoint_Request_goal_x(::msg_interfaces::srv::SendPoint_Request & msg)
  : msg_(msg)
  {}
  Init_SendPoint_Request_goal_y goal_x(::msg_interfaces::srv::SendPoint_Request::_goal_x_type arg)
  {
    msg_.goal_x = std::move(arg);
    return Init_SendPoint_Request_goal_y(msg_);
  }

private:
  ::msg_interfaces::srv::SendPoint_Request msg_;
};

class Init_SendPoint_Request_start_y
{
public:
  explicit Init_SendPoint_Request_start_y(::msg_interfaces::srv::SendPoint_Request & msg)
  : msg_(msg)
  {}
  Init_SendPoint_Request_goal_x start_y(::msg_interfaces::srv::SendPoint_Request::_start_y_type arg)
  {
    msg_.start_y = std::move(arg);
    return Init_SendPoint_Request_goal_x(msg_);
  }

private:
  ::msg_interfaces::srv::SendPoint_Request msg_;
};

class Init_SendPoint_Request_start_x
{
public:
  Init_SendPoint_Request_start_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SendPoint_Request_start_y start_x(::msg_interfaces::srv::SendPoint_Request::_start_x_type arg)
  {
    msg_.start_x = std::move(arg);
    return Init_SendPoint_Request_start_y(msg_);
  }

private:
  ::msg_interfaces::srv::SendPoint_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_interfaces::srv::SendPoint_Request>()
{
  return msg_interfaces::srv::builder::Init_SendPoint_Request_start_x();
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
auto build<::msg_interfaces::srv::SendPoint_Response>()
{
  return ::msg_interfaces::srv::SendPoint_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__SRV__DETAIL__SEND_POINT__BUILDER_HPP_
