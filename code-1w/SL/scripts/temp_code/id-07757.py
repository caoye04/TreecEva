from collections import Counter

# Simulate data flow from multiple sources
inflow_data = ['source_a', 'source_b', 'source_a', 'source_c', 'source_a']
inflow_counter = Counter(inflow_data)

# Outgoing flows represented as a set (unordered, unique)
outflow_set = {2, 5, 8, 11}

# Auxiliary variable - not directly related to main computation
temp_log = [x * 2 for x in range(3)]

# Key logic block with conditional modification of outflow_set
if inflow_counter['source_a'] > 2:
    outflow_set.discard(11)

# Critical execution point
net_flow = inflow_counter['source_a'] - outflow_set.pop() if outflow_set else 0

print(f"Result: {net_flow}")