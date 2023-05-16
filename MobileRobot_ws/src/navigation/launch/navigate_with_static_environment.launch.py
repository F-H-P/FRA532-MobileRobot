#!usr/bin/python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='navigation',
            executable='path_tracking.py',
        ),
        Node(
            package='navigation',
            executable='GlobalPlanning_A-star.py',
        ),
        Node(
            package='navigation',
            executable='Behavior_server.py',
        ),

    ])