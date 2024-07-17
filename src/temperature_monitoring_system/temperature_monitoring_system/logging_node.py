import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import datetime

class TemperatureLogger(Node):
    def __init__(self):
        super().__init__('temperature_logger')
        self.subscription = self.create_subscription(Float32,'Temperature',self.listener_callback,10)
        self.log_file = 'temperature_log.txt'
        with open(self.log_file, 'w') as f:
            f.write('Time, Temperature\n')

    def listener_callback(self, msg):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        temperature = msg.data
        with open(self.log_file, 'a') as f:
            f.write(f'{current_time}, {temperature:.2f}\n')
        self.get_logger().info(f'Logged temperature: {temperature:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureLogger()
    rclpy.spin(node)
    rclpy.shutdown()


