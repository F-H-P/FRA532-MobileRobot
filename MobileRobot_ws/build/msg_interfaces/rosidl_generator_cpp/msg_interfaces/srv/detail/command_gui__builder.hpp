// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from msg_interfaces:srv/CommandGUI.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__BUILDER_HPP_
#define MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "msg_interfaces/srv/detail/command_gui__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace msg_interfaces
{

namespace srv
{

namespace builder
{

class Init_CommandGUI_Request_command
{
public:
  Init_CommandGUI_Request_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::msg_interfaces::srv::CommandGUI_Request command(::msg_interfaces::srv::CommandGUI_Request::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_interfaces::srv::CommandGUI_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_interfaces::srv::CommandGUI_Request>()
{
  return msg_interfaces::srv::builder::Init_CommandGUI_Request_command();
}

}  // namespace msg_interfaces


namespace msg_interfaces
{

namespace srv
{

namespace builder
{

class Init_CommandGUI_Response_res
{
public:
  Init_CommandGUI_Response_res()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::msg_interfaces::srv::CommandGUI_Response res(::msg_interfaces::srv::CommandGUI_Response::_res_type arg)
  {
    msg_.res = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_interfaces::srv::CommandGUI_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_interfaces::srv::CommandGUI_Response>()
{
  return msg_interfaces::srv::builder::Init_CommandGUI_Response_res();
}

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__BUILDER_HPP_
