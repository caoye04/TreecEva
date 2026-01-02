from collections import Counter

# Simulate data packet flows in a network segment
inflow_packets = ['source_A', 'source_B', 'source_A', 'source_C', 'source_A']
outflow_packets = ['dest_X', 'dest_Y', 'dest_X', 'dest_X', 'dest_Z']

timing_log = [1.02, 2.11, 3.05, 4.18]  # Irrelevant timing data (minor distraction)
inflow_counter = Counter(inflow_packets)
outflow_counter = Counter(outflow_packets)

total_inflow = sum(inflow_counter.values())  # Auxiliary computation
total_outflow = sum(outflow_counter.values())  # Auxiliary computation

drop_rate = 0.05  # Packet drop rate (not used in final calculation)
adjustment = len(timing_log) // 2  # Adjustment based on log size

net_flow = inflow_counter['source_A'] - outflow_counter['dest_X'] + adjustment
print(f"Result: {net_flow}")