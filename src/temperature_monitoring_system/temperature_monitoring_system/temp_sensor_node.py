#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class TempSensorNode(Node):
    def __init__(self):
        super().__init__("temperature_publisher")
        self.temp_publisher = self.create_publisher(Float32,"Temperature", 10)
        self.timer = self.create_timer(1.0, self.send_temperature)

    def send_temperature(self):
        temp = Float32()
        temp.data = round(random.uniform(20.0, 50.0), 2)
        self.temp_publisher.publish(temp)
        self.get_logger().info(f'Publishing temperature: {temp.data}')


def main(args=None):
    rclpy.init(args=args)
    node = TempSensorNode()
    rclpy.spin(node)
    rclpy.shutdown()

