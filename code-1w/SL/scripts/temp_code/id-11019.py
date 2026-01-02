from collections import defaultdict

# Simulate hourly network traffic data for two servers
timestamps = [1, 2, 3, 4, 5]
server_a_in = [120, 150, 130, 170, 160]
server_b_out = [110, 145, 135, 160, 158]

# Aggregate inflows and outflows using defaultdict
flow_data = defaultdict(list)
for t in timestamps:
    flow_data['inflows'].append(server_a_in[t-1])
    flow_data['outflows'].append(server_b_out[t-1])

# Extract lists for clarity
inflows = flow_data['inflows']
outflows = flow_data['outflows']

# Compute net flow - key execution point
net_flow = sum(inflows) - sum(outflows)

# Irrelevant statistic (minor distraction)
avg_inflow = sum(inflows) / len(inflows) if inflows else 0

print(f"Result: {net_flow}")