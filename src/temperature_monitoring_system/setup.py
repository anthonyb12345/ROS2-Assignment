from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'temperature_monitoring_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anthony',
    maintainer_email='anthony.bassil3@net.usj.edu.lb',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "temp_sensor_node = temperature_monitoring_system.temp_sensor_node:main",
            "threshold_node = temperature_monitoring_system.threshold_node:main",
            "alert_node = temperature_monitoring_system.alert_node:main",
            "logging_node = temperature_monitoring_system.logging_node:main"
        ],
    },
)
