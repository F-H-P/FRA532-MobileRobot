// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from msg_interfaces:srv/SendPoint.idl
// generated code does not contain a copyright notice
#include "msg_interfaces/srv/detail/send_point__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `start_x`
// Member `start_y`
// Member `goal_x`
// Member `goal_y`
#include "std_msgs/msg/detail/float64__functions.h"

bool
msg_interfaces__srv__SendPoint_Request__init(msg_interfaces__srv__SendPoint_Request * msg)
{
  if (!msg) {
    return false;
  }
  // start_x
  if (!std_msgs__msg__Float64__init(&msg->start_x)) {
    msg_interfaces__srv__SendPoint_Request__fini(msg);
    return false;
  }
  // start_y
  if (!std_msgs__msg__Float64__init(&msg->start_y)) {
    msg_interfaces__srv__SendPoint_Request__fini(msg);
    return false;
  }
  // goal_x
  if (!std_msgs__msg__Float64__init(&msg->goal_x)) {
    msg_interfaces__srv__SendPoint_Request__fini(msg);
    return false;
  }
  // goal_y
  if (!std_msgs__msg__Float64__init(&msg->goal_y)) {
    msg_interfaces__srv__SendPoint_Request__fini(msg);
    return false;
  }
  return true;
}

void
msg_interfaces__srv__SendPoint_Request__fini(msg_interfaces__srv__SendPoint_Request * msg)
{
  if (!msg) {
    return;
  }
  // start_x
  std_msgs__msg__Float64__fini(&msg->start_x);
  // start_y
  std_msgs__msg__Float64__fini(&msg->start_y);
  // goal_x
  std_msgs__msg__Float64__fini(&msg->goal_x);
  // goal_y
  std_msgs__msg__Float64__fini(&msg->goal_y);
}

bool
msg_interfaces__srv__SendPoint_Request__are_equal(const msg_interfaces__srv__SendPoint_Request * lhs, const msg_interfaces__srv__SendPoint_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // start_x
  if (!std_msgs__msg__Float64__are_equal(
      &(lhs->start_x), &(rhs->start_x)))
  {
    return false;
  }
  // start_y
  if (!std_msgs__msg__Float64__are_equal(
      &(lhs->start_y), &(rhs->start_y)))
  {
    return false;
  }
  // goal_x
  if (!std_msgs__msg__Float64__are_equal(
      &(lhs->goal_x), &(rhs->goal_x)))
  {
    return false;
  }
  // goal_y
  if (!std_msgs__msg__Float64__are_equal(
      &(lhs->goal_y), &(rhs->goal_y)))
  {
    return false;
  }
  return true;
}

bool
msg_interfaces__srv__SendPoint_Request__copy(
  const msg_interfaces__srv__SendPoint_Request * input,
  msg_interfaces__srv__SendPoint_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // start_x
  if (!std_msgs__msg__Float64__copy(
      &(input->start_x), &(output->start_x)))
  {
    return false;
  }
  // start_y
  if (!std_msgs__msg__Float64__copy(
      &(input->start_y), &(output->start_y)))
  {
    return false;
  }
  // goal_x
  if (!std_msgs__msg__Float64__copy(
      &(input->goal_x), &(output->goal_x)))
  {
    return false;
  }
  // goal_y
  if (!std_msgs__msg__Float64__copy(
      &(input->goal_y), &(output->goal_y)))
  {
    return false;
  }
  return true;
}

msg_interfaces__srv__SendPoint_Request *
msg_interfaces__srv__SendPoint_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__SendPoint_Request * msg = (msg_interfaces__srv__SendPoint_Request *)allocator.allocate(sizeof(msg_interfaces__srv__SendPoint_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(msg_interfaces__srv__SendPoint_Request));
  bool success = msg_interfaces__srv__SendPoint_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
msg_interfaces__srv__SendPoint_Request__destroy(msg_interfaces__srv__SendPoint_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    msg_interfaces__srv__SendPoint_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
msg_interfaces__srv__SendPoint_Request__Sequence__init(msg_interfaces__srv__SendPoint_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__SendPoint_Request * data = NULL;

  if (size) {
    data = (msg_interfaces__srv__SendPoint_Request *)allocator.zero_allocate(size, sizeof(msg_interfaces__srv__SendPoint_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = msg_interfaces__srv__SendPoint_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        msg_interfaces__srv__SendPoint_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
msg_interfaces__srv__SendPoint_Request__Sequence__fini(msg_interfaces__srv__SendPoint_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      msg_interfaces__srv__SendPoint_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

msg_interfaces__srv__SendPoint_Request__Sequence *
msg_interfaces__srv__SendPoint_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__SendPoint_Request__Sequence * array = (msg_interfaces__srv__SendPoint_Request__Sequence *)allocator.allocate(sizeof(msg_interfaces__srv__SendPoint_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = msg_interfaces__srv__SendPoint_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
msg_interfaces__srv__SendPoint_Request__Sequence__destroy(msg_interfaces__srv__SendPoint_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    msg_interfaces__srv__SendPoint_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
msg_interfaces__srv__SendPoint_Request__Sequence__are_equal(const msg_interfaces__srv__SendPoint_Request__Sequence * lhs, const msg_interfaces__srv__SendPoint_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!msg_interfaces__srv__SendPoint_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
msg_interfaces__srv__SendPoint_Request__Sequence__copy(
  const msg_interfaces__srv__SendPoint_Request__Sequence * input,
  msg_interfaces__srv__SendPoint_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(msg_interfaces__srv__SendPoint_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    msg_interfaces__srv__SendPoint_Request * data =
      (msg_interfaces__srv__SendPoint_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!msg_interfaces__srv__SendPoint_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          msg_interfaces__srv__SendPoint_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!msg_interfaces__srv__SendPoint_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
msg_interfaces__srv__SendPoint_Response__init(msg_interfaces__srv__SendPoint_Response * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
msg_interfaces__srv__SendPoint_Response__fini(msg_interfaces__srv__SendPoint_Response * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
msg_interfaces__srv__SendPoint_Response__are_equal(const msg_interfaces__srv__SendPoint_Response * lhs, const msg_interfaces__srv__SendPoint_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
msg_interfaces__srv__SendPoint_Response__copy(
  const msg_interfaces__srv__SendPoint_Response * input,
  msg_interfaces__srv__SendPoint_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

msg_interfaces__srv__SendPoint_Response *
msg_interfaces__srv__SendPoint_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__SendPoint_Response * msg = (msg_interfaces__srv__SendPoint_Response *)allocator.allocate(sizeof(msg_interfaces__srv__SendPoint_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(msg_interfaces__srv__SendPoint_Response));
  bool success = msg_interfaces__srv__SendPoint_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
msg_interfaces__srv__SendPoint_Response__destroy(msg_interfaces__srv__SendPoint_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    msg_interfaces__srv__SendPoint_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
msg_interfaces__srv__SendPoint_Response__Sequence__init(msg_interfaces__srv__SendPoint_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__SendPoint_Response * data = NULL;

  if (size) {
    data = (msg_interfaces__srv__SendPoint_Response *)allocator.zero_allocate(size, sizeof(msg_interfaces__srv__SendPoint_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = msg_interfaces__srv__SendPoint_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        msg_interfaces__srv__SendPoint_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
msg_interfaces__srv__SendPoint_Response__Sequence__fini(msg_interfaces__srv__SendPoint_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      msg_interfaces__srv__SendPoint_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

msg_interfaces__srv__SendPoint_Response__Sequence *
msg_interfaces__srv__SendPoint_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__SendPoint_Response__Sequence * array = (msg_interfaces__srv__SendPoint_Response__Sequence *)allocator.allocate(sizeof(msg_interfaces__srv__SendPoint_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = msg_interfaces__srv__SendPoint_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
msg_interfaces__srv__SendPoint_Response__Sequence__destroy(msg_interfaces__srv__SendPoint_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    msg_interfaces__srv__SendPoint_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
msg_interfaces__srv__SendPoint_Response__Sequence__are_equal(const msg_interfaces__srv__SendPoint_Response__Sequence * lhs, const msg_interfaces__srv__SendPoint_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!msg_interfaces__srv__SendPoint_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
msg_interfaces__srv__SendPoint_Response__Sequence__copy(
  const msg_interfaces__srv__SendPoint_Response__Sequence * input,
  msg_interfaces__srv__SendPoint_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(msg_interfaces__srv__SendPoint_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    msg_interfaces__srv__SendPoint_Response * data =
      (msg_interfaces__srv__SendPoint_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!msg_interfaces__srv__SendPoint_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          msg_interfaces__srv__SendPoint_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!msg_interfaces__srv__SendPoint_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
