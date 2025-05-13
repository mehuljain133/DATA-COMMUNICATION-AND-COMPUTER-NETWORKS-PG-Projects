# Unit-IV Datalink Layer Functions and Protocols: Framing, flow-control, error recovery protocols, Data link layer of internet-PPP protocol.

import random
import time

# Function for framing data (adding start and end flags)
def frame_data(data):
    start_flag = "START"
    end_flag = "END"
    return f"{start_flag}{data}{end_flag}"

# Function for error detection using checksum (simple parity bit for illustration)
def compute_checksum(data):
    checksum = sum(ord(char) for char in data) % 256
    return checksum

# Function for simulating error in transmission
def introduce_error(data):
    error_chance = 0.1  # 10% chance of error
    if random.random() < error_chance:
        data = data[:-1]  # Introduce error by removing the last character
        print("Error introduced in transmission!")
    return data

# Function to simulate Automatic Repeat reQuest (ARQ) for error recovery
def arq_transmission(data):
    retries = 0
    max_retries = 5
    success = False
    while retries < max_retries:
        print(f"Sending data: {data}")
        # Frame the data
        framed_data = frame_data(data)
        
        # Introduce error to simulate a corrupted frame
        transmitted_data = introduce_error(framed_data)
        
        # Compute checksum
        checksum = compute_checksum(transmitted_data)
        print(f"Checksum for transmitted data: {checksum}")
        
        # Simulate receiving the data and checking the checksum
        received_checksum = compute_checksum(transmitted_data)
        if checksum == received_checksum:
            print("Data received successfully.")
            success = True
            break
        else:
            retries += 1
            print(f"Checksum mismatch! Retry attempt {retries}/{max_retries}")
            time.sleep(1)  # Simulate time delay for retry
    
    if not success:
        print("Transmission failed after max retries!")
    else:
        print("Transmission successful.")

# Flow Control - Stop-and-Wait Protocol
def stop_and_wait(data):
    print("Start Stop-and-Wait Protocol...")
    print(f"Sending data: {data}")
    framed_data = frame_data(data)
    # Introduce error to simulate a corrupted frame
    transmitted_data = introduce_error(framed_data)
    checksum = compute_checksum(transmitted_data)
    
    print(f"Checksum for transmitted data: {checksum}")
    # Simulate receiving the data and checking the checksum
    received_checksum = compute_checksum(transmitted_data)
    
    if checksum == received_checksum:
        print("Data received successfully.")
    else:
        print("Error detected! Retransmitting...")
        stop_and_wait(data)  # Retry transmission in case of error

# Simulate PPP (Point-to-Point Protocol)
def ppp_protocol(data):
    print("\nSimulating PPP Protocol...")
    
    # 1. Framing data
    framed_data = frame_data(data)
    print(f"Framed Data: {framed_data}")
    
    # 2. Add control information (example: LCP - Link Control Protocol for PPP)
    control_info = "LCP (Link Control Protocol)"
    print(f"Control Info: {control_info}")
    
    # 3. Simulate data transmission with potential error
    transmitted_data = introduce_error(framed_data)
    
    # 4. Simulate PPP error detection
    checksum = compute_checksum(transmitted_data)
    print(f"Checksum for transmitted data: {checksum}")
    received_checksum = compute_checksum(transmitted_data)
    
    if checksum == received_checksum:
        print("PPP Data received successfully.")
    else:
        print("PPP Error detected! Retransmitting...")
        ppp_protocol(data)  # Retry transmission in case of error

# Main simulation
def main():
    data = "Hello, this is a message to be transmitted."

    # 1. Simulate ARQ Transmission (Automatic Repeat reQuest)
    print("\n--- ARQ Transmission Simulation ---")
    arq_transmission(data)

    # 2. Simulate Flow Control using Stop-and-Wait Protocol
    print("\n--- Flow Control Simulation: Stop-and-Wait ---")
    stop_and_wait(data)

    # 3. Simulate PPP (Point-to-Point Protocol)
    print("\n--- PPP Protocol Simulation ---")
    ppp_protocol(data)

if __name__ == "__main__":
    main()
