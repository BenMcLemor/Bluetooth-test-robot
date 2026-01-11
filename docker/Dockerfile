# Verwende das offizielle ROS2 ARM Image für Raspberry Pi
FROM ros:humble-ros-base

# Setze explizit die ARM Architektur (optional)
ARG TARGETARCH=arm64
ARG TARGETPLATFORM=linux/arm/v7

# Installiere zusätzliche Pakete
RUN apt-get update && apt-get install -y \
    bluez \
    bluez-tools \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Bluetooth Python Bibliotheken
RUN pip3 install bleak

# Arbeitsverzeichnis
WORKDIR /ros_ws

# Kopiere deinen Code
COPY src ./src

# Baue ROS2 Workspace
RUN . /opt/ros/humble/setup.sh && \
    colcon build --symlink-install

# Entrypoint
CMD ["bash", "-c", "source /ros_ws/install/setup.bash && ros2 run my_bt_test simple_scanner"]
