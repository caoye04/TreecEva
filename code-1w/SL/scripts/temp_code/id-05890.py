from collections import Counter

# Simulate data flow monitoring in a network segment
inflow_data = ['source_A', 'source_B', 'source_A', 'source_C', 'source_A']
inflow_counter = Counter(inflow_data)

# Outgoing traffic volumes recorded in a set (unordered, unique)
outflow_list = [12, 8, 15, 7]
outflow_set = set(outflow_list)

# Auxiliary variable for system status (irrelevant to main calculation)
system_uptime_hours = 48.5

# Key computation: net flow from source_A after adjusting for last known outflow
temp_max_inflow = max(inflow_counter.values())
dropped_packets = 3  # Minor operational metric, not used in final result

net_flow = inflow_counter['source_A'] - outflow_set.pop() if outflow_set else 0

# Print final result as required
print(f"Result: {net_flow}")