// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from msg_interfaces:srv/CommandGUI.idl
// generated code does not contain a copyright notice
#include "msg_interfaces/srv/detail/command_gui__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `command`
#include "std_msgs/msg/detail/string__functions.h"

bool
msg_interfaces__srv__CommandGUI_Request__init(msg_interfaces__srv__CommandGUI_Request * msg)
{
  if (!msg) {
    return false;
  }
  // command
  if (!std_msgs__msg__String__init(&msg->command)) {
    msg_interfaces__srv__CommandGUI_Request__fini(msg);
    return false;
  }
  return true;
}

void
msg_interfaces__srv__CommandGUI_Request__fini(msg_interfaces__srv__CommandGUI_Request * msg)
{
  if (!msg) {
    return;
  }
  // command
  std_msgs__msg__String__fini(&msg->command);
}

bool
msg_interfaces__srv__CommandGUI_Request__are_equal(const msg_interfaces__srv__CommandGUI_Request * lhs, const msg_interfaces__srv__CommandGUI_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // command
  if (!std_msgs__msg__String__are_equal(
      &(lhs->command), &(rhs->command)))
  {
    return false;
  }
  return true;
}

bool
msg_interfaces__srv__CommandGUI_Request__copy(
  const msg_interfaces__srv__CommandGUI_Request * input,
  msg_interfaces__srv__CommandGUI_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // command
  if (!std_msgs__msg__String__copy(
      &(input->command), &(output->command)))
  {
    return false;
  }
  return true;
}

msg_interfaces__srv__CommandGUI_Request *
msg_interfaces__srv__CommandGUI_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__CommandGUI_Request * msg = (msg_interfaces__srv__CommandGUI_Request *)allocator.allocate(sizeof(msg_interfaces__srv__CommandGUI_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(msg_interfaces__srv__CommandGUI_Request));
  bool success = msg_interfaces__srv__CommandGUI_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
msg_interfaces__srv__CommandGUI_Request__destroy(msg_interfaces__srv__CommandGUI_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    msg_interfaces__srv__CommandGUI_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
msg_interfaces__srv__CommandGUI_Request__Sequence__init(msg_interfaces__srv__CommandGUI_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__CommandGUI_Request * data = NULL;

  if (size) {
    data = (msg_interfaces__srv__CommandGUI_Request *)allocator.zero_allocate(size, sizeof(msg_interfaces__srv__CommandGUI_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = msg_interfaces__srv__CommandGUI_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        msg_interfaces__srv__CommandGUI_Request__fini(&data[i - 1]);
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
msg_interfaces__srv__CommandGUI_Request__Sequence__fini(msg_interfaces__srv__CommandGUI_Request__Sequence * array)
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
      msg_interfaces__srv__CommandGUI_Request__fini(&array->data[i]);
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

msg_interfaces__srv__CommandGUI_Request__Sequence *
msg_interfaces__srv__CommandGUI_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__CommandGUI_Request__Sequence * array = (msg_interfaces__srv__CommandGUI_Request__Sequence *)allocator.allocate(sizeof(msg_interfaces__srv__CommandGUI_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = msg_interfaces__srv__CommandGUI_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
msg_interfaces__srv__CommandGUI_Request__Sequence__destroy(msg_interfaces__srv__CommandGUI_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    msg_interfaces__srv__CommandGUI_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
msg_interfaces__srv__CommandGUI_Request__Sequence__are_equal(const msg_interfaces__srv__CommandGUI_Request__Sequence * lhs, const msg_interfaces__srv__CommandGUI_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!msg_interfaces__srv__CommandGUI_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
msg_interfaces__srv__CommandGUI_Request__Sequence__copy(
  const msg_interfaces__srv__CommandGUI_Request__Sequence * input,
  msg_interfaces__srv__CommandGUI_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(msg_interfaces__srv__CommandGUI_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    msg_interfaces__srv__CommandGUI_Request * data =
      (msg_interfaces__srv__CommandGUI_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!msg_interfaces__srv__CommandGUI_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          msg_interfaces__srv__CommandGUI_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!msg_interfaces__srv__CommandGUI_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `res`
#include "std_msgs/msg/detail/int64__functions.h"

bool
msg_interfaces__srv__CommandGUI_Response__init(msg_interfaces__srv__CommandGUI_Response * msg)
{
  if (!msg) {
    return false;
  }
  // res
  if (!std_msgs__msg__Int64__init(&msg->res)) {
    msg_interfaces__srv__CommandGUI_Response__fini(msg);
    return false;
  }
  return true;
}

void
msg_interfaces__srv__CommandGUI_Response__fini(msg_interfaces__srv__CommandGUI_Response * msg)
{
  if (!msg) {
    return;
  }
  // res
  std_msgs__msg__Int64__fini(&msg->res);
}

bool
msg_interfaces__srv__CommandGUI_Response__are_equal(const msg_interfaces__srv__CommandGUI_Response * lhs, const msg_interfaces__srv__CommandGUI_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // res
  if (!std_msgs__msg__Int64__are_equal(
      &(lhs->res), &(rhs->res)))
  {
    return false;
  }
  return true;
}

bool
msg_interfaces__srv__CommandGUI_Response__copy(
  const msg_interfaces__srv__CommandGUI_Response * input,
  msg_interfaces__srv__CommandGUI_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // res
  if (!std_msgs__msg__Int64__copy(
      &(input->res), &(output->res)))
  {
    return false;
  }
  return true;
}

msg_interfaces__srv__CommandGUI_Response *
msg_interfaces__srv__CommandGUI_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__CommandGUI_Response * msg = (msg_interfaces__srv__CommandGUI_Response *)allocator.allocate(sizeof(msg_interfaces__srv__CommandGUI_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(msg_interfaces__srv__CommandGUI_Response));
  bool success = msg_interfaces__srv__CommandGUI_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
msg_interfaces__srv__CommandGUI_Response__destroy(msg_interfaces__srv__CommandGUI_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    msg_interfaces__srv__CommandGUI_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
msg_interfaces__srv__CommandGUI_Response__Sequence__init(msg_interfaces__srv__CommandGUI_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__CommandGUI_Response * data = NULL;

  if (size) {
    data = (msg_interfaces__srv__CommandGUI_Response *)allocator.zero_allocate(size, sizeof(msg_interfaces__srv__CommandGUI_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = msg_interfaces__srv__CommandGUI_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        msg_interfaces__srv__CommandGUI_Response__fini(&data[i - 1]);
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
msg_interfaces__srv__CommandGUI_Response__Sequence__fini(msg_interfaces__srv__CommandGUI_Response__Sequence * array)
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
      msg_interfaces__srv__CommandGUI_Response__fini(&array->data[i]);
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

msg_interfaces__srv__CommandGUI_Response__Sequence *
msg_interfaces__srv__CommandGUI_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msg_interfaces__srv__CommandGUI_Response__Sequence * array = (msg_interfaces__srv__CommandGUI_Response__Sequence *)allocator.allocate(sizeof(msg_interfaces__srv__CommandGUI_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = msg_interfaces__srv__CommandGUI_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
msg_interfaces__srv__CommandGUI_Response__Sequence__destroy(msg_interfaces__srv__CommandGUI_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    msg_interfaces__srv__CommandGUI_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
msg_interfaces__srv__CommandGUI_Response__Sequence__are_equal(const msg_interfaces__srv__CommandGUI_Response__Sequence * lhs, const msg_interfaces__srv__CommandGUI_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!msg_interfaces__srv__CommandGUI_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
msg_interfaces__srv__CommandGUI_Response__Sequence__copy(
  const msg_interfaces__srv__CommandGUI_Response__Sequence * input,
  msg_interfaces__srv__CommandGUI_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(msg_interfaces__srv__CommandGUI_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    msg_interfaces__srv__CommandGUI_Response * data =
      (msg_interfaces__srv__CommandGUI_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!msg_interfaces__srv__CommandGUI_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          msg_interfaces__srv__CommandGUI_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!msg_interfaces__srv__CommandGUI_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
