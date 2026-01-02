from collections import Counter

# Simulate data flow monitoring in a network node
inflow_data = ['source_A', 'source_B', 'source_A', 'source_C', 'source_A']
outflow_data = ['sink_X', 'sink_Y', 'sink_Z', 'sink_X']

inflow_counter = Counter(inflow_data)
outflow_counter = Counter(outflow_data)

# Calculate effective net flow from source_A to sink_X
net_flow = inflow_counter['source_A'] - outflow_counter.get('sink_X', 0)

# Irrelevant auxiliary calculation (minor distraction)
total_inflow = sum(inflow_counter.values())
utilization = total_inflow / (len(inflow_data) + 1)

Result: net_flow