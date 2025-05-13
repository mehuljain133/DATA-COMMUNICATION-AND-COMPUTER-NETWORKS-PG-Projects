# Unit-V Medium Access Sublayer: CSMA/CD protocol and Ethernet, hubs and switches, fast Ethernet, gigabit Ethernet, CSMA/CA protocol and WLAN. 

import random
import time

# Constants
ETHERNET_SPEED = 10  # Mbps for standard Ethernet
FAST_ETHERNET_SPEED = 100  # Mbps for Fast Ethernet
GIGABIT_ETHERNET_SPEED = 1000  # Mbps for Gigabit Ethernet
MAX_COLLISION_ATTEMPTS = 5

# Function to simulate a random collision (for CSMA/CD and CSMA/CA)
def detect_collision():
    return random.random() < 0.1  # 10% chance of collision

# CSMA/CD Protocol: Carrier Sense Multiple Access with Collision Detection
def csma_cd(data, speed):
    print(f"--- CSMA/CD Protocol Simulation with {speed} Mbps ---")
    attempts = 0
    while attempts < MAX_COLLISION_ATTEMPTS:
        print(f"Attempt {attempts + 1}: Sending data -> {data}")
        # Carrier sensing (check if the medium is free)
        if detect_collision():
            print("Collision detected!")
            backoff_time = random.randint(1, 5)  # Random backoff time between 1 and 5 seconds
            print(f"Backing off for {backoff_time} seconds...")
            time.sleep(backoff_time)  # Simulate waiting for the backoff time
            attempts += 1
        else:
            print("Data sent successfully!")
            break

    if attempts == MAX_COLLISION_ATTEMPTS:
        print("Max collision attempts reached! Transmission failed.")

# Function for Ethernet frames
def ethernet_frame(data):
    print(f"Framing data: {data}")
    return f"Ethernet Frame: {data}"

# Simulate Hub: Broadcasts data to all connected devices
def hub(data):
    print("\n--- Simulating Hub ---")
    print("Hub: Broadcasting data to all devices:", data)
    print("Every connected device receives the same data.")

# Simulate Switch: Forwards data to the correct device (unicast)
def switch(data, destination_device):
    print("\n--- Simulating Switch ---")
    print(f"Switch: Forwarding data to {destination_device}: {data}")

# Function to simulate the CSMA/CA protocol (used in WLAN)
def csma_ca(data):
    print(f"\n--- CSMA/CA Protocol Simulation ---")
    print("Carrier sensing: Checking if the channel is idle.")
    if detect_collision():
        print("Collision detected! Waiting for backoff...")
        backoff_time = random.randint(1, 5)
        print(f"Backing off for {backoff_time} seconds...")
        time.sleep(backoff_time)
    else:
        print(f"Data sent successfully: {data}")

# Main function to run the simulation for different scenarios
def main():
    data = "Hello, Network! This is a test message."

    # CSMA/CD Protocol Simulations for different speeds
    for speed in [ETHERNET_SPEED, FAST_ETHERNET_SPEED, GIGABIT_ETHERNET_SPEED]:
        csma_cd(data, speed)

    # Simulating Ethernet Frames
    frame = ethernet_frame(data)

    # Simulate Hub (broadcasting)
    hub(frame)

    # Simulate Switch (directed transmission)
    switch(frame, "Device 1")

    # Simulate CSMA/CA (WLAN)
    csma_ca(data)

if __name__ == "__main__":
    main()
