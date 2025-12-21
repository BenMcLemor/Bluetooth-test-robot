#!/usr/bin/env python3
"""
Einfacher Bluetooth Scanner (Simulation)
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import json

class SimpleBTScanner(Node):
    def __init__(self):
        super().__init__('simple_bt_scanner')
        
        # Publisher für Scan-Ergebnisse
        self.scan_pub = self.create_publisher(String, 'bluetooth/devices', 10)
        
        # Timer für regelmäßiges Scannen
        self.create_timer(5.0, self.scan_devices)
        
        self.get_logger().info('📡 Einfacher Bluetooth Scanner gestartet!')
    
    def scan_devices(self):
        """Simuliere Bluetooth-Scan"""
        # Simulierte Bluetooth-Geräte
        simulated_devices = [
            {"name": "Handy-Max", "address": "AA:BB:CC:11:22:33", "rssi": -65},
            {"name": "BT-Kopfhörer", "address": "DD:EE:FF:44:55:66", "rssi": -72},
            {"name": "Smartwatch", "address": "11:22:33:AA:BB:CC", "rssi": -80},
        ]
        
        # Erstelle Nachricht
        msg = String()
        msg.data = json.dumps({
            "timestamp": time.time(),
            "devices": simulated_devices,
            "count": len(simulated_devices)
        })
        
        # Sende Nachricht
        self.scan_pub.publish(msg)
        
        self.get_logger().info(f'📱 {len(simulated_devices)} Bluetooth-Geräte gefunden')

def main(args=None):
    rclpy.init(args=args)
    scanner = SimpleBTScanner()
    rclpy.spin(scanner)
    scanner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
