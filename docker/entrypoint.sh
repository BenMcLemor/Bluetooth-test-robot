#!/bin/bash
set -e

# Start Bluetooth service
service dbus start
service bluetooth start
sleep 2
hciconfig hci0 up || true

# Source ROS2
source /opt/ros/humble/setup.bash

# Source our workspace
if [ -f /ros_ws/install/setup.bash ]; then
    source /ros_ws/install/setup.bash
fi

# Execute command
exec "$@"
