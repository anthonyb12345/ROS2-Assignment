import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TempThreshold(Node):
    def __init__(self):
        super().__init__("Threshold")
        