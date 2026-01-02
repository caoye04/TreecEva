from collections import defaultdict

# Simulate hourly resource usage across multiple servers
def analyze_server_load(log_entries):
    usage_counts = defaultdict(int)
    temporal_weights = {}
    server_utilization = {}
    total_requests = 0
    idle_events = 0  # tracking irrelevant metric

    for entry in log_entries:
        timestamp, server_id, req_type, duration = entry
        hour = timestamp.split(':')[0]
        key = f'{server_id}_{hour}'
        
        # Relevant accumulation
        usage_counts[key] += 1
        total_requests += 1
        
        # Irrelevant computations (distractors)
        if req_type == 'GET':
            weight = float(duration) / (int(hour) + 1)
            temporal_weights[key] = temporal_weights.get(key, 0) + weight
        
        if int(duration) > 500:
            server_utilization[server_id] = server_utilization.get(server_id, 0) + 1
        
        # Dead logic path - never impacts final result
        if 'error' in req_type:
            idle_events += 1  # this field is unused later

    # Secondary processing: normalize weights (irrelevant)
    norm_factor = sum(temporal_weights.values()) if temporal_weights else 1
    for k in temporal_weights:
        temporal_weights[k] /= norm_factor

    # Critical computation step
    peak_capacity = max(usage_counts.values())

    # Additional red herring variables
    avg_per_server = sum(usage_counts.values()) / len(set(k.split('_')[0] for k in usage_counts))
    peak_hour = max(set(k.split('_')[1] for k in usage_counts), key=lambda h: sum(1 for k in usage_counts if k.endswith(h)))

    print(f'Result: {peak_capacity}')
    return peak_capacity

# Deterministic input data
logs = [
    ('09:12', 'srv-a', 'GET', '234'),
    ('09:15', 'srv-b', 'POST', '120'),
    ('09:22', 'srv-a', 'GET', '189'),
    ('10:05', 'srv-a', 'GET', '203'),
    ('10:10', 'srv-c', 'PUT', '98'),
    ('10:12', 'srv-a', 'GET', '255'),
    ('10:18', 'srv-b', 'GET', '301'),
    ('10:22', 'srv-a', 'GET', '198'),
    ('11:05', 'srv-c', 'GET', '210')
]

analyze_server_load(logs)