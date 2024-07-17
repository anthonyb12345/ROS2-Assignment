# ROS2-Assignment

# Temperature Monitoring System

## Overview

This ROS 2 package contains nodes for simulating a temperature sensor, monitoring temperature thresholds, publishing alerts, and logging temperature data for analysis. The package includes the following nodes:

1. `temp_sensor_node`: Simulates a temperature sensor by publishing random temperature values to the `Temperature` topic.
2. `threshold_node`: Subscribes to the `Temperature` topic and checks if the temperature exceeds a predefined threshold. If the threshold is exceeded, it publishes an alert to the `alert_trigger` topic.
3. `alert_node`: Subscribes to the `alert_trigger` topic and publishes an alert message to the `alert` topic.
4. `logging_node`: Subscribes to the `Temperature` topic and logs the temperature values to a file.

### Building the Package

1. Clone the repository to your workspace:

    ```bash
    cd ~/ros2_ws/src
    git clone git@github.com:anthonyb12345/ROS2-Assignment.git
    ```

2. Navigate to the root of your workspace:

    ```bash
    cd ~/ros2_ws
    ```

3. Build the package using `colcon`:

    ```bash
    colcon build
    ```

4. Source the setup file:

    ```bash
    source install/setup.bash
    ```

## Running the Package

You can launch all the nodes together using the provided launch file:

  ```bash
  ros2 launch temperature_monitoring_system temperature_monitor_launch.py
  ```

## Verifying Nodes

To verify that the nodes are running, you can list the active nodes:
   ```bash
   ros2 node list
   ros2 topic list
   ```
   
## Checking Temperature Logs
Temperature data is logged to temperature_log.txt. You can view the log file in real-time by running:
   ```bash
   tail -f temperature_log.txt
   ```


