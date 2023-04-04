#!usr/bin/python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    path_tracking = Node(
        package='navigation',
        executable='path_tracking.py'
    ),
    global_path_planning = Node(
        package='navigation',
        executable='GlobalPlanning_A-star.py'
    ),
    behavior_server = Node(
        package='navigation',
        executable='Behavior_server.py'
    )

    return LaunchDescription([
        path_tracking,
        global_path_planning,
        behavior_server
    ])