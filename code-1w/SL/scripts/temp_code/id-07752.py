from collections import Counter

# Water treatment plant flow monitoring
inflow_readings = [320, 415, 380, 430, 390]
outflow_readings = [310, 405, 375, 440, 385]

# Count frequency of readings (irrelevant for final result)
frequency_in = Counter(inflow_readings)
frequency_out = Counter(outflow_readings)

# Calculate total inflow and outflow
inflow_sum = sum(inflow_readings)
outflow_sum = sum(outflow_readings)

# Determine net water flow in the system
net_flow = inflow_sum - outflow_sum

# Print result
print(f"Result: {net_flow}")