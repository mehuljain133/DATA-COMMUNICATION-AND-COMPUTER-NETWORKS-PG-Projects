# Unit-III Network Architecture and Reference Models: Layered network architectures, protocol hierarchies, interface and services, ISO-OSI reference model, TCP/IP reference model, Internet protocol stack.

import matplotlib.pyplot as plt
import numpy as np

# Define Layered Network Architectures
layers_osi = ['Application', 'Presentation', 'Session', 'Transport', 'Network', 'Data Link', 'Physical']
layers_tcp_ip = ['Application', 'Transport', 'Internet', 'Network Access']

# Define a simple Protocol Hierarchy
protocols_osi = {
    'Application': ['HTTP', 'FTP', 'SMTP'],
    'Presentation': ['SSL/TLS', 'JPEG', 'GIF'],
    'Session': ['NetBIOS', 'RPC'],
    'Transport': ['TCP', 'UDP'],
    'Network': ['IP', 'ICMP', 'ARP'],
    'Data Link': ['Ethernet', 'PPP'],
    'Physical': ['Ethernet cables', 'Fiber optics']
}

protocols_tcp_ip = {
    'Application': ['HTTP', 'FTP', 'SMTP'],
    'Transport': ['TCP', 'UDP'],
    'Internet': ['IP', 'ICMP', 'ARP'],
    'Network Access': ['Ethernet', 'Wi-Fi']
}

# Function to visualize OSI and TCP/IP Model
def plot_layers(layers, protocols, model_name):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot layers
    y_pos = np.arange(len(layers))
    ax.barh(y_pos, np.ones(len(layers)), align='center', color='lightblue')

    # Annotate layers and protocols
    for i, layer in enumerate(layers):
        ax.text(1.02, i, layer, ha='left', va='center', fontsize=12, fontweight='bold', color='black')
        ax.text(1.05, i, ', '.join(protocols[layer]), ha='left', va='center', fontsize=10, color='darkblue')

    ax.set_xlim(0, 1.2)
    ax.set_yticks(y_pos)
    ax.set_yticklabels([])  # Remove y-axis ticks as they are redundant
    ax.set_xlabel('Protocols', fontsize=12)
    ax.set_title(f'{model_name} Protocol Stack', fontsize=14)

    plt.tight_layout()
    plt.show()

# Plot OSI Model
plot_layers(layers_osi, protocols_osi, "ISO-OSI Model")

# Plot TCP/IP Model
plot_layers(layers_tcp_ip, protocols_tcp_ip, "TCP/IP Model")

# Simulate Protocol Hierarchy (Conceptual)
def simulate_protocol_communication(model_name, layers, protocols):
    print(f"\nSimulating {model_name} Communication Process...\n")
    for i, layer in enumerate(layers):
        print(f"Layer {i+1}: {layer}")
        print(f"Protocols used in this layer: {', '.join(protocols[layer])}")
        print("-" * 50)

# Simulate Communication for OSI and TCP/IP Models
simulate_protocol_communication("ISO-OSI Model", layers_osi, protocols_osi)
simulate_protocol_communication("TCP/IP Model", layers_tcp_ip, protocols_tcp_ip)


