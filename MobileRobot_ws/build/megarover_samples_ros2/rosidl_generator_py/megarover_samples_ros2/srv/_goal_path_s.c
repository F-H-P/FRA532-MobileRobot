// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from megarover_samples_ros2:srv/GoalPath.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "megarover_samples_ros2/srv/detail/goal_path__struct.h"
#include "megarover_samples_ros2/srv/detail/goal_path__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__float64_multi_array__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__float64_multi_array__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__float64_multi_array__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__float64_multi_array__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool megarover_samples_ros2__srv__goal_path__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[55];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("megarover_samples_ros2.srv._goal_path.GoalPath_Request", full_classname_dest, 54) == 0);
  }
  megarover_samples_ros2__srv__GoalPath_Request * ros_message = _ros_message;
  {  // x_path
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_path");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__float64_multi_array__convert_from_py(field, &ros_message->x_path)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // y_path
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_path");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__float64_multi_array__convert_from_py(field, &ros_message->y_path)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * megarover_samples_ros2__srv__goal_path__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of GoalPath_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("megarover_samples_ros2.srv._goal_path");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "GoalPath_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  megarover_samples_ros2__srv__GoalPath_Request * ros_message = (megarover_samples_ros2__srv__GoalPath_Request *)raw_ros_message;
  {  // x_path
    PyObject * field = NULL;
    field = std_msgs__msg__float64_multi_array__convert_to_py(&ros_message->x_path);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_path", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_path
    PyObject * field = NULL;
    field = std_msgs__msg__float64_multi_array__convert_to_py(&ros_message->y_path);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_path", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "megarover_samples_ros2/srv/detail/goal_path__struct.h"
// already included above
// #include "megarover_samples_ros2/srv/detail/goal_path__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool megarover_samples_ros2__srv__goal_path__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[56];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("megarover_samples_ros2.srv._goal_path.GoalPath_Response", full_classname_dest, 55) == 0);
  }
  megarover_samples_ros2__srv__GoalPath_Response * ros_message = _ros_message;
  ros_message->structure_needs_at_least_one_member = 0;

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * megarover_samples_ros2__srv__goal_path__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of GoalPath_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("megarover_samples_ros2.srv._goal_path");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "GoalPath_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  (void)raw_ros_message;

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
