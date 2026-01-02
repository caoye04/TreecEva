from collections import defaultdict

# Simulate a network flow analysis with metadata tracking
node_metrics = [
    {'type': 'router', 'in': 45, 'out': 23, 'temp': 67},
    {'type': 'switch', 'in': 67, 'out': 34, 'temp': 54},
    {'type': 'firewall', 'in': 34, 'out': 89, 'temp': 78},
    {'type': 'bridge', 'in': 78, 'out': 45, 'temp': 65},
    {'type': 'repeater', 'in': 23, 'out': 12, 'temp': 90}
]

# Extract and transform data using list comprehensions and slicing
raw_inflows = [node['in'] for node in node_metrics if node['type'] != 'unknown']
inflows = raw_inflows[:]

raw_outflows = [node['out'] for node in node_metrics]
outflows = raw_outflows[::1]  # Redundant full copy

# Misleading temperature average calculation (unused)
temp_readings = [node['temp'] for node in node_metrics]
avg_temp = sum(temp_readings) / len(temp_readings)
high_temp_nodes = [t for t in temp_readings if t > 70]

data_log = []
for i, (in_val, out_val) in enumerate(zip(inflows, outflows)):
    status = 'normal' if in_val >= out_val else 'warning'
    data_log.append({'index': i, 'status': status})

# Initialize counters for side statistics (partially used)
event_count = defaultdict(int)
for log in data_log:
    event_count[log['status']] += 1

# Dead code: simulate packet loss estimation (not affecting result)
packet_loss_estimate = 0.0
if event_count.get('warning', 0) > 1:
    packet_loss_estimate = 0.15 * sum(outflows)
else:
    packet_loss_estimate = 0.05 * sum(outflows)

# Core computation: net data flow (this determines the answer)
net_flow = sum(inflows) - sum(outflows)

# Print result as required
print(f"Result: {net_flow}")