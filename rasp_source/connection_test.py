""" Raspberry Pi 4 MQTT publication & subscription
"""

import paho.mqtt.client as mqtt
import time

# Define the MQTT broker information
BROKER_ADDRESS = "localhost"
PORT = 1883
TOPIC = "test/topic/"   # This will change depending on the program

def mqtt_callback(client, userdata, message):
	print(f"\nRecieved message: {message.payload.decode()} on topic {message.topic}")


def main() -> None:
	# Initialize the MQTT client
	client = mqtt.Client()

	# Attach the on_message callback
	client.on_message = mqtt_callback
	
	# Connect to the broker
	print("Connecting to MQTT broker...")
	client.connect(BROKER_ADDRESS, PORT, 60)
	
	# Start the loop to process network traffic and dispoatch callbacks
	client.loop_start()
	
	# Subscribe to the topic
	print(f"SUbscribing to tipoc: {TOPIC}")
	client.subscribe(TOPIC)
	
	# Publish messahes to the topic in a loop
	try:
		while True:
			message = input("Enter a message to publish (or 'exit' to quit): ")
			if message.lower() == 'exit':
				break
			client.publish(TOPIC, message)
			print(f"Message published: {message}")
	except KeyboardInterrupt:
		print("\nExiting...")
		
	# Stop the loop and disconnect the client
	client.loop_stop()
	client.disconnect()
	print("Disconnected from MQTT broker.")

if __name__ == "__main__":
	main()
