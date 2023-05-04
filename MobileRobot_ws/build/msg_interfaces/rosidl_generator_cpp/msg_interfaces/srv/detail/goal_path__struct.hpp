// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from msg_interfaces:srv/GoalPath.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__GOAL_PATH__STRUCT_HPP_
#define MSG_INTERFACES__SRV__DETAIL__GOAL_PATH__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'x_path'
// Member 'y_path'
#include "std_msgs/msg/detail/float64_multi_array__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__msg_interfaces__srv__GoalPath_Request __attribute__((deprecated))
#else
# define DEPRECATED__msg_interfaces__srv__GoalPath_Request __declspec(deprecated)
#endif

namespace msg_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GoalPath_Request_
{
  using Type = GoalPath_Request_<ContainerAllocator>;

  explicit GoalPath_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : x_path(_init),
    y_path(_init)
  {
    (void)_init;
  }

  explicit GoalPath_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : x_path(_alloc, _init),
    y_path(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _x_path_type =
    std_msgs::msg::Float64MultiArray_<ContainerAllocator>;
  _x_path_type x_path;
  using _y_path_type =
    std_msgs::msg::Float64MultiArray_<ContainerAllocator>;
  _y_path_type y_path;

  // setters for named parameter idiom
  Type & set__x_path(
    const std_msgs::msg::Float64MultiArray_<ContainerAllocator> & _arg)
  {
    this->x_path = _arg;
    return *this;
  }
  Type & set__y_path(
    const std_msgs::msg::Float64MultiArray_<ContainerAllocator> & _arg)
  {
    this->y_path = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    msg_interfaces::srv::GoalPath_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const msg_interfaces::srv::GoalPath_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<msg_interfaces::srv::GoalPath_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<msg_interfaces::srv::GoalPath_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::GoalPath_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::GoalPath_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::GoalPath_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::GoalPath_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<msg_interfaces::srv::GoalPath_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<msg_interfaces::srv::GoalPath_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__msg_interfaces__srv__GoalPath_Request
    std::shared_ptr<msg_interfaces::srv::GoalPath_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__msg_interfaces__srv__GoalPath_Request
    std::shared_ptr<msg_interfaces::srv::GoalPath_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GoalPath_Request_ & other) const
  {
    if (this->x_path != other.x_path) {
      return false;
    }
    if (this->y_path != other.y_path) {
      return false;
    }
    return true;
  }
  bool operator!=(const GoalPath_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GoalPath_Request_

// alias to use template instance with default allocator
using GoalPath_Request =
  msg_interfaces::srv::GoalPath_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace msg_interfaces


#ifndef _WIN32
# define DEPRECATED__msg_interfaces__srv__GoalPath_Response __attribute__((deprecated))
#else
# define DEPRECATED__msg_interfaces__srv__GoalPath_Response __declspec(deprecated)
#endif

namespace msg_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GoalPath_Response_
{
  using Type = GoalPath_Response_<ContainerAllocator>;

  explicit GoalPath_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit GoalPath_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    msg_interfaces::srv::GoalPath_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const msg_interfaces::srv::GoalPath_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<msg_interfaces::srv::GoalPath_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<msg_interfaces::srv::GoalPath_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::GoalPath_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::GoalPath_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::GoalPath_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::GoalPath_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<msg_interfaces::srv::GoalPath_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<msg_interfaces::srv::GoalPath_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__msg_interfaces__srv__GoalPath_Response
    std::shared_ptr<msg_interfaces::srv::GoalPath_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__msg_interfaces__srv__GoalPath_Response
    std::shared_ptr<msg_interfaces::srv::GoalPath_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GoalPath_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const GoalPath_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GoalPath_Response_

// alias to use template instance with default allocator
using GoalPath_Response =
  msg_interfaces::srv::GoalPath_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace msg_interfaces

namespace msg_interfaces
{

namespace srv
{

struct GoalPath
{
  using Request = msg_interfaces::srv::GoalPath_Request;
  using Response = msg_interfaces::srv::GoalPath_Response;
};

}  // namespace srv

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__SRV__DETAIL__GOAL_PATH__STRUCT_HPP_
