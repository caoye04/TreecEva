from itertools import accumulate

# Simulate sensor readings for fluid dynamics analysis
inflows = [12, 8, 15, 3, 9]
outflows = [5, 10, 6, 11, 7]  # Distractor: not used in final computation

# Preprocess: smooth inflow data with cumulative average
smoothed = list(accumulate(inflows))

# Secondary metric: peak_to_average_ratio (distractor)
peak_to_average_ratio = max(inflows) / (sum(inflows) / len(inflows))

# Key computational step
net_flow = sum(inflows) ^ (inflows[0] & inflows[-1])

# Additional unused transformation (minor interference)
doubled = [x * 2 for x in inflows if x > 10]

print(f"Result: {net_flow}")