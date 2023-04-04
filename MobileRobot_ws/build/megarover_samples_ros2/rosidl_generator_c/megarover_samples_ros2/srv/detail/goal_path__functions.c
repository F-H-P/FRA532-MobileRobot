// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from megarover_samples_ros2:srv/GoalPath.idl
// generated code does not contain a copyright notice
#include "megarover_samples_ros2/srv/detail/goal_path__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `x_path`
// Member `y_path`
#include "std_msgs/msg/detail/float64_multi_array__functions.h"

bool
megarover_samples_ros2__srv__GoalPath_Request__init(megarover_samples_ros2__srv__GoalPath_Request * msg)
{
  if (!msg) {
    return false;
  }
  // x_path
  if (!std_msgs__msg__Float64MultiArray__init(&msg->x_path)) {
    megarover_samples_ros2__srv__GoalPath_Request__fini(msg);
    return false;
  }
  // y_path
  if (!std_msgs__msg__Float64MultiArray__init(&msg->y_path)) {
    megarover_samples_ros2__srv__GoalPath_Request__fini(msg);
    return false;
  }
  return true;
}

void
megarover_samples_ros2__srv__GoalPath_Request__fini(megarover_samples_ros2__srv__GoalPath_Request * msg)
{
  if (!msg) {
    return;
  }
  // x_path
  std_msgs__msg__Float64MultiArray__fini(&msg->x_path);
  // y_path
  std_msgs__msg__Float64MultiArray__fini(&msg->y_path);
}

bool
megarover_samples_ros2__srv__GoalPath_Request__are_equal(const megarover_samples_ros2__srv__GoalPath_Request * lhs, const megarover_samples_ros2__srv__GoalPath_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // x_path
  if (!std_msgs__msg__Float64MultiArray__are_equal(
      &(lhs->x_path), &(rhs->x_path)))
  {
    return false;
  }
  // y_path
  if (!std_msgs__msg__Float64MultiArray__are_equal(
      &(lhs->y_path), &(rhs->y_path)))
  {
    return false;
  }
  return true;
}

bool
megarover_samples_ros2__srv__GoalPath_Request__copy(
  const megarover_samples_ros2__srv__GoalPath_Request * input,
  megarover_samples_ros2__srv__GoalPath_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // x_path
  if (!std_msgs__msg__Float64MultiArray__copy(
      &(input->x_path), &(output->x_path)))
  {
    return false;
  }
  // y_path
  if (!std_msgs__msg__Float64MultiArray__copy(
      &(input->y_path), &(output->y_path)))
  {
    return false;
  }
  return true;
}

megarover_samples_ros2__srv__GoalPath_Request *
megarover_samples_ros2__srv__GoalPath_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  megarover_samples_ros2__srv__GoalPath_Request * msg = (megarover_samples_ros2__srv__GoalPath_Request *)allocator.allocate(sizeof(megarover_samples_ros2__srv__GoalPath_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(megarover_samples_ros2__srv__GoalPath_Request));
  bool success = megarover_samples_ros2__srv__GoalPath_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
megarover_samples_ros2__srv__GoalPath_Request__destroy(megarover_samples_ros2__srv__GoalPath_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    megarover_samples_ros2__srv__GoalPath_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
megarover_samples_ros2__srv__GoalPath_Request__Sequence__init(megarover_samples_ros2__srv__GoalPath_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  megarover_samples_ros2__srv__GoalPath_Request * data = NULL;

  if (size) {
    data = (megarover_samples_ros2__srv__GoalPath_Request *)allocator.zero_allocate(size, sizeof(megarover_samples_ros2__srv__GoalPath_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = megarover_samples_ros2__srv__GoalPath_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        megarover_samples_ros2__srv__GoalPath_Request__fini(&data[i - 1]);
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
megarover_samples_ros2__srv__GoalPath_Request__Sequence__fini(megarover_samples_ros2__srv__GoalPath_Request__Sequence * array)
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
      megarover_samples_ros2__srv__GoalPath_Request__fini(&array->data[i]);
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

megarover_samples_ros2__srv__GoalPath_Request__Sequence *
megarover_samples_ros2__srv__GoalPath_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  megarover_samples_ros2__srv__GoalPath_Request__Sequence * array = (megarover_samples_ros2__srv__GoalPath_Request__Sequence *)allocator.allocate(sizeof(megarover_samples_ros2__srv__GoalPath_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = megarover_samples_ros2__srv__GoalPath_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
megarover_samples_ros2__srv__GoalPath_Request__Sequence__destroy(megarover_samples_ros2__srv__GoalPath_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    megarover_samples_ros2__srv__GoalPath_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
megarover_samples_ros2__srv__GoalPath_Request__Sequence__are_equal(const megarover_samples_ros2__srv__GoalPath_Request__Sequence * lhs, const megarover_samples_ros2__srv__GoalPath_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!megarover_samples_ros2__srv__GoalPath_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
megarover_samples_ros2__srv__GoalPath_Request__Sequence__copy(
  const megarover_samples_ros2__srv__GoalPath_Request__Sequence * input,
  megarover_samples_ros2__srv__GoalPath_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(megarover_samples_ros2__srv__GoalPath_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    megarover_samples_ros2__srv__GoalPath_Request * data =
      (megarover_samples_ros2__srv__GoalPath_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!megarover_samples_ros2__srv__GoalPath_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          megarover_samples_ros2__srv__GoalPath_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!megarover_samples_ros2__srv__GoalPath_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
megarover_samples_ros2__srv__GoalPath_Response__init(megarover_samples_ros2__srv__GoalPath_Response * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
megarover_samples_ros2__srv__GoalPath_Response__fini(megarover_samples_ros2__srv__GoalPath_Response * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
megarover_samples_ros2__srv__GoalPath_Response__are_equal(const megarover_samples_ros2__srv__GoalPath_Response * lhs, const megarover_samples_ros2__srv__GoalPath_Response * rhs)
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
megarover_samples_ros2__srv__GoalPath_Response__copy(
  const megarover_samples_ros2__srv__GoalPath_Response * input,
  megarover_samples_ros2__srv__GoalPath_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

megarover_samples_ros2__srv__GoalPath_Response *
megarover_samples_ros2__srv__GoalPath_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  megarover_samples_ros2__srv__GoalPath_Response * msg = (megarover_samples_ros2__srv__GoalPath_Response *)allocator.allocate(sizeof(megarover_samples_ros2__srv__GoalPath_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(megarover_samples_ros2__srv__GoalPath_Response));
  bool success = megarover_samples_ros2__srv__GoalPath_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
megarover_samples_ros2__srv__GoalPath_Response__destroy(megarover_samples_ros2__srv__GoalPath_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    megarover_samples_ros2__srv__GoalPath_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
megarover_samples_ros2__srv__GoalPath_Response__Sequence__init(megarover_samples_ros2__srv__GoalPath_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  megarover_samples_ros2__srv__GoalPath_Response * data = NULL;

  if (size) {
    data = (megarover_samples_ros2__srv__GoalPath_Response *)allocator.zero_allocate(size, sizeof(megarover_samples_ros2__srv__GoalPath_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = megarover_samples_ros2__srv__GoalPath_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        megarover_samples_ros2__srv__GoalPath_Response__fini(&data[i - 1]);
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
megarover_samples_ros2__srv__GoalPath_Response__Sequence__fini(megarover_samples_ros2__srv__GoalPath_Response__Sequence * array)
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
      megarover_samples_ros2__srv__GoalPath_Response__fini(&array->data[i]);
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

megarover_samples_ros2__srv__GoalPath_Response__Sequence *
megarover_samples_ros2__srv__GoalPath_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  megarover_samples_ros2__srv__GoalPath_Response__Sequence * array = (megarover_samples_ros2__srv__GoalPath_Response__Sequence *)allocator.allocate(sizeof(megarover_samples_ros2__srv__GoalPath_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = megarover_samples_ros2__srv__GoalPath_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
megarover_samples_ros2__srv__GoalPath_Response__Sequence__destroy(megarover_samples_ros2__srv__GoalPath_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    megarover_samples_ros2__srv__GoalPath_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
megarover_samples_ros2__srv__GoalPath_Response__Sequence__are_equal(const megarover_samples_ros2__srv__GoalPath_Response__Sequence * lhs, const megarover_samples_ros2__srv__GoalPath_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!megarover_samples_ros2__srv__GoalPath_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
megarover_samples_ros2__srv__GoalPath_Response__Sequence__copy(
  const megarover_samples_ros2__srv__GoalPath_Response__Sequence * input,
  megarover_samples_ros2__srv__GoalPath_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(megarover_samples_ros2__srv__GoalPath_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    megarover_samples_ros2__srv__GoalPath_Response * data =
      (megarover_samples_ros2__srv__GoalPath_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!megarover_samples_ros2__srv__GoalPath_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          megarover_samples_ros2__srv__GoalPath_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!megarover_samples_ros2__srv__GoalPath_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
