from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='temperature_monitoring_system',
            executable='temp_sensor_node',
            name='temp_sensor_node'
        ),
        Node(
            package='temperature_monitoring_system',
            executable='threshold_node',
            name='threshold_node'
        ),
        Node(
            package='temperature_monitoring_system',
            executable='alert_node',
            name='alert_node'
        ),
    ])
