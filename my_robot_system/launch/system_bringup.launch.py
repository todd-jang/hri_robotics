from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='my_robot_system', executable='ultrasonic_node'),
        Node(package='my_robot_system', executable='depth_camera_node'),
        Node(package='my_robot_system', executable='vla_inference_node'),
        Node(package='my_robot_system', executable='policy_inference_node'),
        Node(package='my_robot_system', executable='skill_manager'),
        Node(package='my_robot_system', executable='master_controller'),
    ])
