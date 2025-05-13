# Unit-VI Network and transport layers functions and protocols: Network switching mechanismsCircuit switching, packet switching, routing and congestion control, TCP/IP protocol architecture

import random
import time

# Constants for simulation
MAX_HOPS = 5
MAX_PACKETS = 3
CONGESTION_THRESHOLD = 70  # Percentage
MAX_CONGESTION_TRIES = 3
NETWORK_SIZE = 5  # Number of nodes in the network

# Simulating Circuit Switching
def circuit_switching(data, start_node, end_node):
    print("\n--- Circuit Switching Simulation ---")
    print(f"Establishing a dedicated path from Node {start_node} to Node {end_node}")
    # Simulating the transmission over a dedicated path
    time.sleep(1)  # Simulating time for data transfer
    print(f"Data transferred successfully over the dedicated path: {data}")

# Simulating Packet Switching
def packet_switching(data):
    print("\n--- Packet Switching Simulation ---")
    packets = [f"Packet {i+1}: {data}" for i in range(MAX_PACKETS)]
    print(f"Breaking the data into {MAX_PACKETS} packets:")
    
    for packet in packets:
        # Randomly simulate packet routing through different nodes
        route = random.randint(1, NETWORK_SIZE)
        print(f"Sending {packet} to Node {route}")
        time.sleep(0.5)
    
    print("All packets have been sent independently.")

# Simulating Routing
def routing(data):
    print("\n--- Routing Simulation ---")
    print(f"Routing data: {data}")
    
    # Simulating packet routing through a network with multiple nodes
    hops = random.randint(1, MAX_HOPS)
    print(f"Routing data through {hops} hops...")
    for hop in range(hops):
        print(f"Node {hop+1}: Forwarding the packet.")
        time.sleep(0.5)
    
    print(f"Data successfully routed through {hops} hops.")

# Simulating Congestion Control
def congestion_control():
    print("\n--- Congestion Control Simulation ---")
    congestion_level = random.randint(50, 100)
    print(f"Current network congestion level: {congestion_level}%")
    
    if congestion_level > CONGESTION_THRESHOLD:
        print(f"Congestion level exceeds {CONGESTION_THRESHOLD}% - Initiating congestion control...")
        # Simulating backoff and reducing data transmission rate
        time.sleep(2)  # Backoff period
        print("Congestion resolved by slowing down transmission.")
    else:
        print("Network congestion is within acceptable limits.")

# Simulating TCP/IP Protocol Architecture
def tcp_ip_protocol(data):
    print("\n--- TCP/IP Protocol Architecture Simulation ---")
    
    # TCP/IP stack layers
    layers = ["Application Layer", "Transport Layer", "Internet Layer", "Link Layer"]
    
    # Simulate data encapsulation through TCP/IP stack
    for layer in layers:
        print(f"Encapsulating data at {layer}: {data}")
        data = f"Data encapsulated in {layer}"
        time.sleep(0.5)
    
    print(f"Data successfully transmitted through the TCP/IP stack.")

# Main simulation function
def main():
    data = "Hello, this is a test message to be transmitted across the network."
    
    # Simulate Circuit Switching between nodes 1 and 4
    circuit_switching(data, 1, 4)
    
    # Simulate Packet Switching
    packet_switching(data)
    
    # Simulate Routing through random nodes
    routing(data)
    
    # Simulate Congestion Control
    congestion_control()
    
    # Simulate TCP/IP Protocol stack
    tcp_ip_protocol(data)

if __name__ == "__main__":
    main()
