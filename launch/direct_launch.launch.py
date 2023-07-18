import os
import sys

import launch
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
from launch import LaunchDescription

def generate_launch_description():
      """Generate launch description with multiple components."""
      path_file = os.path.dirname(__file__)

      ld = launch.LaunchDescription()


      device_container = IncludeLaunchDescription(
          PythonLaunchDescriptionSource(
              [
                  os.path.join(get_package_share_directory("canopen_core"), "launch"),
                  "/canopen.launch.py",
              ]
          ),
          launch_arguments={
              "master_config": os.path.join(
                  get_package_share_directory("driver_motor"),
                  "config",
                  "single-db42",
                  "master.dcf",
              ),
              "master_bin": os.path.join(
                  get_package_share_directory("drive_motor"),
                  "config",
                  "single-db42",
                  "master.bin",
              ),
              "bus_config": os.path.join(
                  get_package_share_directory("drive_motor"),
                  "config",
                  "single-db42",
                  "bus.yml",
              ),
              "can_interface_name": "can0",
          }.items(),

      )

      ld.add_action(device_container)

      return ld