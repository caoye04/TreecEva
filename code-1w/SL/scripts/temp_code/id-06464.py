from collections import defaultdict

# Simulate packet flow data over network segments
segments = ['A', 'B', 'C', 'D']
packet_data = [120, 150, 90, 200]
data_map = defaultdict(int)

for i, seg in enumerate(segments):
    data_map[seg] = packet_data[i]

# Calculate inflow and outflow
inflow = sum([data_map[s] for s in segments if s in ['A', 'C']])
outflow = sum([data_map[s] for s in segments if s in ['B', 'D']])
threshold = 100

# Key statement
net_flow = inflow - outflow if inflow > threshold else inflow // 2

# Additional irrelevant tracking (minor distraction)
current_status = 'active'
heartbeat_interval = 5

print(f"Result: {net_flow}")