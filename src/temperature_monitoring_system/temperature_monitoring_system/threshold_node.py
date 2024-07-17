import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
import random

class ThresholdSubscriber(Node):
    def __init__(self):
        super().__init__('threshold_subscriber')
        self.subscription = self.create_subscription(Float32, 'Temperature', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'alert_trigger', 10)
        self.threshold = 40
    
    def listener_callback(self, temp: Float32):
        if temp.data > self.threshold:
            alert_msg = String()
            alert_msg.data = 'Temperature threshold exceeded!'
            self.publisher_.publish(alert_msg)
            self.get_logger().info(f'Alert: {alert_msg.data}')
        else:
            self.get_logger().info(f'Temperature: {temp.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ThresholdSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
