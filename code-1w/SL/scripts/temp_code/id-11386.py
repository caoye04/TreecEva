def analyze_traffic(flow):
    if flow['protocol'] == 'TCP':
        return flow['size'] * 0.9
    elif flow['protocol'] == 'UDP':
        return flow['size'] * 0.7
    else:
        return flow['size'] * 0.5

base_config = {
    'max_rate': 120,
    'burst_capacity': 300,
    'threshold': 85,
    'scaling_factor': 1.25
}

usage_log = [
    {'timestamp': 1678886400, 'protocol': 'TCP', 'size': 120},
    {'timestamp': 1678886401, 'protocol': 'UDP', 'size': 80},
    {'timestamp': 1678886402, 'protocol': 'ICMP', 'size': 30},
    {'timestamp': 1678886403, 'protocol': 'TCP', 'size': 200}
]

# Irrelevant helper function (dead code path)
def validate_checksum(packet):
    checksum = 0
    for b in str(packet).encode('utf-8'):
        checksum ^= b
    return checksum % 256

# Distractor variables
temp_offset = 0.05
scale_ratio = base_config['scaling_factor'] * 0.8
baseline_score = sum([len(str(v)) for v in base_config.values()])

# Simulate historical averages (not used in final calculation)
historical_avg = 0
for entry in usage_log:
    historical_avg += entry['size']
historical_avg /= len(usage_log)

# Auxiliary tracking state (partially used)
effective_load = 0
priority_count = 0
for flow in usage_log:
    adjusted_size = analyze_traffic(flow)
    effective_load += adjusted_size
    if flow['protocol'] == 'TCP':
        priority_count += 1

# Secondary metric with no impact
collision_risk = (priority_count * 10) % 7

# Core adjustment logic
def adjust_bandwidth(config, log):
    total_utilization = 0
    peak_usage = 0
    protocol_weights = {'TCP': 3, 'UDP': 2, 'ICMP': 1}
    weight_sum = 0
    
    for record in log:
        proto = record['protocol']
        raw_size = record['size']
        # Weighted contribution
        if proto in protocol_weights:
            weight = protocol_weights[proto]
            total_utilization += raw_size * weight
            weight_sum += weight
            if raw_size > peak_usage:
                peak_usage = raw_size
    
    weighted_avg = total_utilization / weight_sum if weight_sum > 0 else 0
    
    # Apply scaling based on threshold rules
    if weighted_avg > config['threshold']:
        multiplier = config['scaling_factor']
    else:
        multiplier = 1.0
    
    # Compute base bandwidth
    base_bandwidth = config['max_rate'] * (effective_load / 100.0)  # Uses outer scope variable
    
    # Final adjustment
    final = base_bandwidth * multiplier
    
    # Red herring computation
    buffer_reserve = (config['burst_capacity'] - final) * temp_offset
    
    return int(final + 0.5)  # Rounded integer result

# Key execution point
final_bandwidth = adjust_bandwidth(base_config, usage_log)

# Print result as required
print(f"Result: {final_bandwidth}")