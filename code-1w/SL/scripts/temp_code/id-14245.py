from collections import defaultdict

# Simulate water flow monitoring in a pipeline system over several hours
flow_data = [120, 85, 150, 60, 200]
durations = [30, 45, 60, 25, 90]
threshold = 100

# Aggregating hourly adjusted flows using defaultdict
time_adjusted_flows = defaultdict(float)
for i, (flow, duration) in enumerate(zip(flow_data, durations)):
    time_adjusted_flows[i] = flow * (duration / 60)

# Calculate total inflow and outflow
inflow = sum(time_adjusted_flows.values())
waste_factor = 0.1
maintenance_loss = 5.5
outflow = inflow * (1 - waste_factor) - maintenance_loss

# Critical computation point
net_flow = inflow - outflow if inflow > threshold else (inflow - outflow) // 2

# Print final result
print(f"Result: {net_flow}")