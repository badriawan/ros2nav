# init_robot.launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='project_localization',
            executable='initial_pose_pub',
            name='initial_pose_publisher',
            output='screen'
        )
    ])