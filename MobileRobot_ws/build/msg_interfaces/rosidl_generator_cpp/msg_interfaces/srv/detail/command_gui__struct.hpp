// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from msg_interfaces:srv/CommandGUI.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__STRUCT_HPP_
#define MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'command'
#include "std_msgs/msg/detail/string__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__msg_interfaces__srv__CommandGUI_Request __attribute__((deprecated))
#else
# define DEPRECATED__msg_interfaces__srv__CommandGUI_Request __declspec(deprecated)
#endif

namespace msg_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct CommandGUI_Request_
{
  using Type = CommandGUI_Request_<ContainerAllocator>;

  explicit CommandGUI_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : command(_init)
  {
    (void)_init;
  }

  explicit CommandGUI_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : command(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _command_type =
    std_msgs::msg::String_<ContainerAllocator>;
  _command_type command;

  // setters for named parameter idiom
  Type & set__command(
    const std_msgs::msg::String_<ContainerAllocator> & _arg)
  {
    this->command = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__msg_interfaces__srv__CommandGUI_Request
    std::shared_ptr<msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__msg_interfaces__srv__CommandGUI_Request
    std::shared_ptr<msg_interfaces::srv::CommandGUI_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CommandGUI_Request_ & other) const
  {
    if (this->command != other.command) {
      return false;
    }
    return true;
  }
  bool operator!=(const CommandGUI_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CommandGUI_Request_

// alias to use template instance with default allocator
using CommandGUI_Request =
  msg_interfaces::srv::CommandGUI_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace msg_interfaces


// Include directives for member types
// Member 'res'
#include "std_msgs/msg/detail/int64__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__msg_interfaces__srv__CommandGUI_Response __attribute__((deprecated))
#else
# define DEPRECATED__msg_interfaces__srv__CommandGUI_Response __declspec(deprecated)
#endif

namespace msg_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct CommandGUI_Response_
{
  using Type = CommandGUI_Response_<ContainerAllocator>;

  explicit CommandGUI_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : res(_init)
  {
    (void)_init;
  }

  explicit CommandGUI_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : res(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _res_type =
    std_msgs::msg::Int64_<ContainerAllocator>;
  _res_type res;

  // setters for named parameter idiom
  Type & set__res(
    const std_msgs::msg::Int64_<ContainerAllocator> & _arg)
  {
    this->res = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__msg_interfaces__srv__CommandGUI_Response
    std::shared_ptr<msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__msg_interfaces__srv__CommandGUI_Response
    std::shared_ptr<msg_interfaces::srv::CommandGUI_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CommandGUI_Response_ & other) const
  {
    if (this->res != other.res) {
      return false;
    }
    return true;
  }
  bool operator!=(const CommandGUI_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CommandGUI_Response_

// alias to use template instance with default allocator
using CommandGUI_Response =
  msg_interfaces::srv::CommandGUI_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace msg_interfaces

namespace msg_interfaces
{

namespace srv
{

struct CommandGUI
{
  using Request = msg_interfaces::srv::CommandGUI_Request;
  using Response = msg_interfaces::srv::CommandGUI_Response;
};

}  // namespace srv

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__SRV__DETAIL__COMMAND_GUI__STRUCT_HPP_
