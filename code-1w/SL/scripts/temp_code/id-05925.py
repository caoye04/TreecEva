from collections import defaultdict
import itertools

# Simulate distributed system node load transfers over time
node_transfers = [
    ('node_a', 'node_b', 15), ('node_b', 'node_c', 10), ('node_c', 'node_d', 20),
    ('node_d', 'node_a', 5), ('node_a', 'node_c', 12), ('node_b', 'node_d', 8)
]

# Irrelevant metadata - distractor
system_metadata = {
    'version': '3.2.1',
    'deployment_region': 'us-west-2',
    'uptime_days': 47,
    'redundancy_factor': 3.7
}

# Track incoming and outgoing loads per node
flow_counter = defaultdict(lambda: {'in': 0, 'out': 0})
for src, dst, load in node_transfers:
    flow_counter[src]['out'] += load
    flow_counter[dst]['in'] += load

# Compute net flow (could be positive or negative)
net_flows = {node: data['in'] - data['out'] for node, data in flow_counter.items()}

# Distractor computation: normalize flows (not used later)
normalized_flows = {}
total_magnitude = sum(abs(x) for x in net_flows.values()) + 1e-9
for node, net in net_flows.items():
    normalized_flows[node] = round(net / total_magnitude, 4)

# System state tracks active nodes and baseline capacity
system_state = {
    'active_nodes': ['node_a', 'node_b', 'node_c'],
    'base_capacity_per_node': 100,
    'overhead_ratio': 0.15
}

# Transfer logs with duplicated and filtered entries (some irrelevant)
transfer_logs = []
for entry in node_transfers:
    transfer_logs.append(('send', entry[0], entry[2]))
    transfer_logs.append(('recv', entry[1], entry[2]))

# Add redundant echo-like entries (distractor)
echo_logs = [('echo', n, int(l * 0.1)) for t, n, l in transfer_logs if t == 'recv']
transfer_logs.extend(echo_logs)

# Filter only send/recv for processing
filtered_ops = [op for op in transfer_logs if op[0] in ('send', 'recv')]

# Aggregate total operations per node (semi-relevant)
op_counter = defaultdict(int)
for op_type, node, load in filtered_ops:
    op_counter[node] += 1

# Primary logic: calculate effective balancing factor based on transfer patterns
unique_pairs = set((src, dst) for src, dst, _ in node_transfers)
balance_factor = len(unique_pairs) / (len(system_state['active_nodes']) + 1)

# Secondary: compute adjustment from net surplus/deficit among active nodes
active_net_flow = sum(net_flows[n] for n in system_state['active_nodes'])
adjustment = abs(active_net_flow) // 10 if active_net_flow != 0 else 1

# Helper function to calculate stable operational capacity
def calculate_stable_capacity(logs, state):
    # Extract total transferred volume
    total_volume = sum(entry[2] for entry in logs if entry[0] in ('send', 'recv'))
    
    # Red herring: count message types (unused)
    type_count = {t: 0 for t in ['send', 'recv', 'echo']}
    for typ, _, _ in logs:
        if typ in type_count:
            type_count[typ] += 1
    
    # Real work: base depends on active nodes and overhead
    active_count = len(state['active_nodes'])
    raw_capacity = active_count * state['base_capacity_per_node']
    adjusted_capacity = raw_capacity * (1 - state['overhead_ratio'])
    
    # Apply dynamic scaling based on volume and balance
    scaling_factor = 0.8 + (min(total_volume / 100.0, 0.5))
    
    # Final stabilization using adjustment and floor
    stabilized = int(adjusted_capacity * scaling_factor) - adjustment
    
    return stabilized

# Execute main calculation
final_capacity = calculate_stable_capacity(transfer_logs, system_state)

# Print result as required
print(f"Target result: {final_capacity}")