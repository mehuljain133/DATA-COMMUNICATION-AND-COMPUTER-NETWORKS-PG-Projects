# Unit-II Network Classification and Network services: Local Area Networks, Metropolitan Area Networks, Wide Area Network, wireless networks, internetworking and Internet, business and home applications, mobile user services. 

import networkx as nx
import matplotlib.pyplot as plt
import random

# Create a network graph to visualize different types of networks
G = nx.Graph()

# Add nodes (devices) for different networks
devices_lan = ['PC1', 'PC2', 'PC3', 'Router_LAN']
devices_man = ['PC4', 'PC5', 'Router_MAN', 'Switch_MAN']
devices_wan = ['Server', 'PC6', 'Router_WAN', 'Switch_WAN']
devices_wireless = ['Mobile1', 'Mobile2', 'BaseStation']
devices_internet = ['WebServer', 'DNS', 'Router_Internet']

# Add devices as nodes to the graph
G.add_nodes_from(devices_lan + devices_man + devices_wan + devices_wireless + devices_internet)

# Create edges (connections between devices in the network)
edges = [
    ('PC1', 'Router_LAN'), ('PC2', 'Router_LAN'), ('PC3', 'Router_LAN'),
    ('Router_LAN', 'Router_MAN'), ('Router_MAN', 'Router_WAN'),
    ('Router_WAN', 'Server'), ('PC6', 'Router_WAN'), ('Switch_WAN', 'Router_WAN'),
    ('Mobile1', 'BaseStation'), ('Mobile2', 'BaseStation'),
    ('BaseStation', 'Router_MAN'), ('Router_MAN', 'Router_LAN'),
    ('WebServer', 'Router_Internet'), ('DNS', 'Router_Internet'),
    ('Router_Internet', 'Server')
]

# Add edges to the graph
G.add_edges_from(edges)

# Network visualization
plt.figure(figsize=(10, 8))

# Draw the graph with different colors for different network types
node_colors = []
for node in G.nodes:
    if node in devices_lan:
        node_colors.append('blue')
    elif node in devices_man:
        node_colors.append('green')
    elif node in devices_wan:
        node_colors.append('red')
    elif node in devices_wireless:
        node_colors.append('orange')
    else:
        node_colors.append('purple')

# Draw the graph
pos = nx.spring_layout(G)  # Force-directed layout for better visualization
nx.draw(G, pos, with_labels=True, node_size=3000, node_color=node_colors, font_size=12, font_weight='bold', edge_color='gray')

# Title and show the graph
plt.title("Network Types and Devices Visualization", fontsize=14)
plt.show()

# Network Classification and Description
network_types = {
    "LAN (Local Area Network)": "Small-scale network, typically within a building or office.",
    "MAN (Metropolitan Area Network)": "Mid-size network, typically spans across a city or large campus.",
    "WAN (Wide Area Network)": "Large-scale network, connects devices across cities, countries, or continents.",
    "Wireless Networks": "Mobile communication networks using wireless technologies like Wi-Fi, LTE, 5G.",
    "Internet": "Global network connecting millions of devices using IP protocol."
}

print("\nNetwork Classification and Descriptions:")
for net_type, description in network_types.items():
    print(f"{net_type}: {description}")

# Mobile User Services Concept
mobile_services = [
    "Mobile Internet Access (3G/4G/5G)",
    "Location-based Services (GPS, Maps)",
    "Mobile Email and Messaging",
    "Mobile E-Commerce",
    "Mobile VoIP (Voice over IP)"
]

print("\nMobile User Services:")
for service in mobile_services:
    print(f"- {service}")

# Business and Home Applications
business_applications = [
    "Enterprise Resource Planning (ERP)",
    "Cloud Computing",
    "Customer Relationship Management (CRM)",
    "E-commerce Websites",
    "Video Conferencing"
]

home_applications = [
    "Home Networking (Wi-Fi)",
    "Smart Home Devices (IoT)",
    "Streaming Services (Netflix, Hulu)",
    "Online Shopping",
    "Social Media Access"
]

print("\nBusiness Applications:")
for app in business_applications:
    print(f"- {app}")

print("\nHome Applications:")
for app in home_applications:
    print(f"- {app}")

