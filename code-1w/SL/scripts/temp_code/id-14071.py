from collections import Counter

data_packets = ['source_a', 'source_b', 'source_a', 'relay_c', 'source_a', 'relay_c']
inflow_counter = Counter(data_packets)
outflow_list = [5, 3, 8, 2]
outflow_set = set(outflow_list)

# Simulate packet validation filter
valid_sources = {key for key in inflow_counter.keys() if 'source' in key}
total_valid = sum(inflow_counter[src] for src in valid_sources)

# Critical computation point
temporary_offset = len(outflow_list) * 2
dummy_var = [x ** 2 for x in outflow_list if x < 4]
net_flow = inflow_counter['source_a'] - outflow_set.pop() if outflow_set else 0

print(f"Result: {net_flow}")