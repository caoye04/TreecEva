import itertools

# Device communication profiles: [device_id, connections, data_volume_gb, protocols_used]
device_profiles = [
    ['DEV001', 15, 8.3, ['TCP', 'UDP']],
    ['DEV002', 8, 2.1, ['TCP']],
    ['DEV003', 25, 15.7, ['TCP', 'UDP', 'ICMP']],
    ['DEV004', 3, 0.5, ['UDP']],
    ['DEV005', 12, 6.2, ['TCP', 'ICMP']],
    ['DEV006', 20, 11.8, ['TCP', 'UDP', 'ICMP', 'SCTP']],
    ['DEV007', 5, 1.2, ['TCP']],
    ['DEV008', 18, 9.4, ['UDP', 'ICMP']]
]

# Trust score calculation parameters
base_weights = {'connections': 2.5, 'data_volume': 1.8, 'protocol_diversity': 3.2}
threshold = 45.0

# Calculate trust scores for each device
trust_scores = {}
for profile in device_profiles:
    device_id, connections, data_volume, protocols = profile
    protocol_bonus = len(protocols) * base_weights['protocol_diversity']
    score = (connections * base_weights['connections'] + 
             data_volume * base_weights['data_volume'] + 
             protocol_bonus)
    trust_scores[device_id] = score

# Identify flagged devices (below threshold)
flagged_devices = {dev_id for dev_id, score in trust_scores.items() if score < threshold}

# Cross-reference with suspicious connection patterns
suspicious_patterns = {'UDP', 'ICMP'}
flagged_devices_count = 0

for profile in device_profiles:
    device_id, _, _, protocols = profile
    if device_id in flagged_devices:
        protocol_set = set(protocols)
        # Check if device uses any suspicious protocols
        if protocol_set & suspicious_patterns:
            flagged_devices_count += 1
        elif 'TCP' in protocol_set and len(protocol_set) == 1:
            # Special case: only TCP with low diversity
            if trust_scores[device_id] < 30.0:
                flagged_devices_count += 1

print(f"Result: {flagged_devices_count}")