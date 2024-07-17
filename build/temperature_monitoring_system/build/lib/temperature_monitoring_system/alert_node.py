#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AlertPublisher(Node):
    def __init__(self):
        super().__init__('alert_publisher')
        self.subscription = self.create_subscription(String, 'alert_trigger', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'alert', 10)
    
    def listener_callback(self, msg: String):
        alert_msg = String()
        alert_msg.data = 'Alert: Temperature has exceeded the threshold!'
        self.publisher_.publish(alert_msg)
        self.get_logger().info(f'Publishing: {alert_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = AlertPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


