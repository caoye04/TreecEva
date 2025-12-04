import itertools

def calculate_priority(metrics):
    # This function calculates a priority factor based on network metrics
    if not metrics:
        return 0
    
    # Extract only values divisible by 3 or 5
    relevant = [m for m in metrics if m % 3 == 0 or m % 5 == 0]
    
    # If no relevant metrics, use backup calculation
    if not relevant:
        return sum(metrics) / len(metrics) if metrics else 0
    
    # Calculate priority based on relevant metrics
    return max(relevant) - min(relevant)

def analyze_network_traffic(packets):
    # Analyze network traffic data (distractor function)
    total_bytes = sum(p.get('size', 0) for p in packets)
    avg_latency = sum(p.get('latency', 0) for p in packets) / len(packets) if packets else 0
    return {'bytes': total_bytes, 'latency': avg_latency}

# Network traffic simulation data (mostly distractor)
packets = [
    {'id': 'pkt001', 'size': 1280, 'latency': 45},
    {'id': 'pkt002', 'size': 512, 'latency': 32},
    {'id': 'pkt003', 'size': 2048, 'latency': 60}
]

# Network metrics collection
raw_metrics = [75, 42, 18, 30, 65, 90, 23, 81, 45, 60]
filtered_metrics = []

# Packet processing (distractor code)
traffic_stats = analyze_network_traffic(packets)
packet_threshold = traffic_stats['latency'] * 0.8

# Generate potential metric combinations (distractor)
possible_combinations = list(itertools.combinations(raw_metrics, 3))
potential_values = [sum(combo) / 3 for combo in possible_combinations]

# String-based network status code (distractor with string methods)
status_code = "NETWORK_STATUS_OPTIMAL"
if "OPTIMAL" in status_code:
    optimization_factor = len([c for c in status_code if c.isupper()])
else:
    optimization_factor = 0

# Process metrics based on status (mixing relevant and irrelevant)
if status_code.startswith("NETWORK"):
    # This branch is taken
    priority_threshold = 40
    
    # Filter metrics (this is the key calculation)
    for metric in raw_metrics:
        if metric > priority_threshold:
            filtered_metrics.append(metric)
        elif metric % 2 == 0 and metric < priority_threshold:
            # Distractor calculation
            adjusted = metric * 1.5
            if adjusted > 50:
                filtered_metrics.append(int(adjusted))
    
    # Calculate backup values (distractor)
    backup_values = [m for m in raw_metrics if m not in filtered_metrics]
    backup_priority = sum(backup_values) / len(backup_values) if backup_values else 0
else:
    # Dead code path
    filtered_metrics = [m for m in raw_metrics if m % 7 == 0]
    backup_priority = max(raw_metrics) if raw_metrics else 0

# Misleading intermediate calculation
intermediate_result = optimization_factor * 3
if intermediate_result > 30:
    # Dead code path
    filtered_metrics = [30, 60, 90]

# This is the key statement that calculates the answer
priority_factor = calculate_priority(filtered_metrics)

# Misleading post-calculation (distractor)
if len(filtered_metrics) > 5:
    priority_factor += 10
elif len(filtered_metrics) < 3:
    priority_factor = priority_factor * 0.8

# Further distractor calculations
network_health_score = (priority_factor / max(raw_metrics)) * 100
network_stability = sum(1 for m in filtered_metrics if m > 50) / len(filtered_metrics) if filtered_metrics else 0

print(f"Result: {priority_factor}")