from collections import Counter

# Simulate data packet flows in a network segment
tx_packets = ['source_a', 'source_b', 'source_a', 'source_c', 'source_b', 'source_a']
rx_packets = ['dest_x', 'dest_y', 'dest_x', 'dest_z', 'dest_y', 'dest_x', 'dest_x']

# Count occurrence of each source and destination
inflow_counter = Counter(tx_packets)
outflow_counter = Counter(rx_packets)

# Track auxiliary metric: unique sources (minimal interference)
unique_sources = len(inflow_counter)
expected_volume = 2 * unique_sources  # Irrelevant calculation, minor distraction

# Key computational step
net_flow = inflow_counter['source_a'] - outflow_counter['dest_x']

# Output result
print(f"Result: {net_flow}")