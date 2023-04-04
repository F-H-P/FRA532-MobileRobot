// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from msg_interfaces:srv/SendPoint.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__SEND_POINT__STRUCT_HPP_
#define MSG_INTERFACES__SRV__DETAIL__SEND_POINT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'start_x'
// Member 'start_y'
// Member 'goal_x'
// Member 'goal_y'
#include "std_msgs/msg/detail/float64__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__msg_interfaces__srv__SendPoint_Request __attribute__((deprecated))
#else
# define DEPRECATED__msg_interfaces__srv__SendPoint_Request __declspec(deprecated)
#endif

namespace msg_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SendPoint_Request_
{
  using Type = SendPoint_Request_<ContainerAllocator>;

  explicit SendPoint_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : start_x(_init),
    start_y(_init),
    goal_x(_init),
    goal_y(_init)
  {
    (void)_init;
  }

  explicit SendPoint_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : start_x(_alloc, _init),
    start_y(_alloc, _init),
    goal_x(_alloc, _init),
    goal_y(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _start_x_type =
    std_msgs::msg::Float64_<ContainerAllocator>;
  _start_x_type start_x;
  using _start_y_type =
    std_msgs::msg::Float64_<ContainerAllocator>;
  _start_y_type start_y;
  using _goal_x_type =
    std_msgs::msg::Float64_<ContainerAllocator>;
  _goal_x_type goal_x;
  using _goal_y_type =
    std_msgs::msg::Float64_<ContainerAllocator>;
  _goal_y_type goal_y;

  // setters for named parameter idiom
  Type & set__start_x(
    const std_msgs::msg::Float64_<ContainerAllocator> & _arg)
  {
    this->start_x = _arg;
    return *this;
  }
  Type & set__start_y(
    const std_msgs::msg::Float64_<ContainerAllocator> & _arg)
  {
    this->start_y = _arg;
    return *this;
  }
  Type & set__goal_x(
    const std_msgs::msg::Float64_<ContainerAllocator> & _arg)
  {
    this->goal_x = _arg;
    return *this;
  }
  Type & set__goal_y(
    const std_msgs::msg::Float64_<ContainerAllocator> & _arg)
  {
    this->goal_y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    msg_interfaces::srv::SendPoint_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const msg_interfaces::srv::SendPoint_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<msg_interfaces::srv::SendPoint_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<msg_interfaces::srv::SendPoint_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::SendPoint_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::SendPoint_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::SendPoint_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::SendPoint_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<msg_interfaces::srv::SendPoint_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<msg_interfaces::srv::SendPoint_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__msg_interfaces__srv__SendPoint_Request
    std::shared_ptr<msg_interfaces::srv::SendPoint_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__msg_interfaces__srv__SendPoint_Request
    std::shared_ptr<msg_interfaces::srv::SendPoint_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SendPoint_Request_ & other) const
  {
    if (this->start_x != other.start_x) {
      return false;
    }
    if (this->start_y != other.start_y) {
      return false;
    }
    if (this->goal_x != other.goal_x) {
      return false;
    }
    if (this->goal_y != other.goal_y) {
      return false;
    }
    return true;
  }
  bool operator!=(const SendPoint_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SendPoint_Request_

// alias to use template instance with default allocator
using SendPoint_Request =
  msg_interfaces::srv::SendPoint_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace msg_interfaces


#ifndef _WIN32
# define DEPRECATED__msg_interfaces__srv__SendPoint_Response __attribute__((deprecated))
#else
# define DEPRECATED__msg_interfaces__srv__SendPoint_Response __declspec(deprecated)
#endif

namespace msg_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SendPoint_Response_
{
  using Type = SendPoint_Response_<ContainerAllocator>;

  explicit SendPoint_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit SendPoint_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    msg_interfaces::srv::SendPoint_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const msg_interfaces::srv::SendPoint_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<msg_interfaces::srv::SendPoint_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<msg_interfaces::srv::SendPoint_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::SendPoint_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::SendPoint_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::SendPoint_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::SendPoint_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<msg_interfaces::srv::SendPoint_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<msg_interfaces::srv::SendPoint_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__msg_interfaces__srv__SendPoint_Response
    std::shared_ptr<msg_interfaces::srv::SendPoint_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__msg_interfaces__srv__SendPoint_Response
    std::shared_ptr<msg_interfaces::srv::SendPoint_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SendPoint_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const SendPoint_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SendPoint_Response_

// alias to use template instance with default allocator
using SendPoint_Response =
  msg_interfaces::srv::SendPoint_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace msg_interfaces

namespace msg_interfaces
{

namespace srv
{

struct SendPoint
{
  using Request = msg_interfaces::srv::SendPoint_Request;
  using Response = msg_interfaces::srv::SendPoint_Response;
};

}  // namespace srv

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__SRV__DETAIL__SEND_POINT__STRUCT_HPP_
