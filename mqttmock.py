#!/usr/bin/python3

import paho.mqtt.client as mqtt
import json
import time
import random

# Define MQTT settings
MQTT_BROKER = "localhost"  # Change to your broker address
MQTT_PORT = 1883            # Default MQTT port

# Create an MQTT client instance
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT)

# Mock data publishing function with random values
def publish_mock_data():
    topics = [
        "copilot/data/gyro/x",
        "copilot/data/gyro/y",
        "copilot/data/gyro/z",
        "copilot/data/acceleration/x",
        "copilot/data/acceleration/y",
        "copilot/data/acceleration/z",
        "copilot/data/mag/x",
        "copilot/data/mag/y",
        "copilot/data/mag/z",
        "copilot/data/gyro/temp",
        "copilot/data/mag/heading",
        "copilot/data/system/cpu",
        "copilot/data/system/memory"
    ]

    for topic in topics:
        # Generate random payloads based on the topic
        if "gyro" in topic:
            payload = json.dumps({"value": round(random.uniform(-100, 100), 2)})  # Gyro values between -100 and 100
        elif "acceleration" in topic:
            payload = json.dumps({"value": round(random.uniform(-10, 10), 2)})  # Acceleration values between -10 and 10
        elif "mag" in topic:
            payload = json.dumps({"value": round(random.uniform(0, 360), 2)})   # Magnetic values between 0 and 360 degrees
        elif "temp" in topic:
            payload = json.dumps({"value": round(random.uniform(20, 30), 2)})   # Temperature values between 20 and 30 degrees Celsius
        elif "cpu" in topic:
            payload = json.dumps({"value": random.randint(0, 100)})             # CPU usage percentage
        elif "memory" in topic:
            payload = json.dumps({"value": random.randint(0, 16000)})          # Memory usage in MB
            
        client.publish(topic, payload)
        print(f"Published {payload} to {topic}")
        time.sleep(1)  # Sleep between publishes for demonstration

# Publish mock data
publish_mock_data()

# Disconnect from the broker
client.disconnect()

