# Use ARMv7 base image for Raspberry Pi 3
FROM arm32v7/ubuntu:22.04

# Install ROS2 Humble
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    lsb-release \
    && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2.list \
    && apt-get update && apt-get install -y \
    ros-humble-ros-base \
    python3-colcon-common-extensions \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Bluetooth tools
RUN apt-get update && apt-get install -y \
    bluez \
    bluez-tools \
    && rm -rf /var/lib/apt/lists/*

# Install Python Bluetooth libraries
RUN pip3 install bleak

# Set up workspace
WORKDIR /ros_ws
COPY src ./src

# Build ROS2 workspace
RUN . /opt/ros/humble/setup.sh && \
    colcon build --symlink-install

# Entrypoint script
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["ros2", "run", "my_bt_test", "simple_scanner"]
