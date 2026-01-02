from collections import Counter

# Simulate data flows from various sources and destinations
inflow_records = ['source_A', 'source_B', 'source_A', 'source_C', 'source_A', 'source_B']
outflow_records = ['dest_X', 'dest_Y', 'dest_X', 'dest_Z', 'dest_Y', 'dest_X', 'dest_X']

# Count occurrences using Counter
total_inflows = len(inflow_records)
total_outflows = len(outflow_records)

inflow_counter = Counter(inflow_records)
outflow_counter = Counter(outflow_records)

# Track auxiliary statistic (irrelevant to final result but adds minimal distraction)
unique_sources = len(inflow_counter)

# Key computation point
net_flow = inflow_counter['source_A'] - outflow_counter['dest_X']

# Print final result
print(f"Result: {net_flow}")