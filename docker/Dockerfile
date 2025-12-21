# Basis-Image mit ROS2
FROM ros:humble-ros-base

# Arbeitsverzeichnis
WORKDIR /ros_ws

# Kopiere deinen Code
COPY src /ros_ws/src

# Installiere Python
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Baue ROS2 Workspace
RUN . /opt/ros/humble/setup.sh && \
    colcon build

# Start-Befehl
CMD ["bash", "-c", "source /ros_ws/install/setup.bash && ros2 run my_bt_test simple_scanner"]
