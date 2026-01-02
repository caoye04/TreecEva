from collections import defaultdict
import math

# Simulate a distributed network node analysis with diagnostic metrics
def analyze_node_health(node_metrics):
    health_scores = []
    for node_id, metrics in node_metrics.items():
        cpu_load = metrics['cpu']
        mem_usage = metrics['memory']
        latency = metrics['latency']
        packet_loss = metrics['packet_loss']

        # Irrelevant computation: theoretical bandwidth capacity (not used)
        theoretical_bw = 1000 * math.log(1 + metrics['signal_strength'], 2)

        # Misleading intermediate score
        temp_score = (cpu_load * 0.3) + (mem_usage * 0.3) + (latency * 0.4)

        # Actual health formula
        stability_factor = (100 - cpu_load) * 0.4 + (100 - mem_usage) * 0.3 + (100 - latency) * 0.2 + (100 - packet_loss * 10) * 0.1
        health_scores.append(max(stability_factor, 0))
    return health_scores

# Dead function: never called but looks relevant
def deprecated_network_scan(nodes):
    scan_results = []
    for node in nodes:
        fingerprint = ''.join(sorted(set(str(node))))
        scan_results.append(hash(fingerprint) % 100)
    return scan_results

# Another red herring: calculates average length of node IDs as strings
def string_length_analysis(node_ids):
    lengths = [len(str(nid)) for nid in node_ids]
    return sum(lengths) / len(lengths) if lengths else 0

# Core data transformation with distractors
def transform_sensor_data(raw_data):
    processed = defaultdict(float)
    buffer_cache = []

    for entry in raw_data:
        sensor_id = entry[0]
        readings = entry[1:]

        # Distractor: caching unused intermediate values
        buffer_cache.append(sum(readings) / len(readings))

        # Real processing: variance-based weighting
        mean_val = sum(readings) / len(readings)
        variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
        weight = 1 / (1 + variance)  # Higher variance → lower weight

        processed[sensor_id] += weight
    
    # Unused aggregation
    total_cached = sum(buffer_cache)
    avg_cache = total_cached / len(buffer_cache) if buffer_cache else 0

    return dict(processed)

# Main stability computation with nested logic and decoys
def compute_stability_index(nodes):
    base_weights = {'alpha': 0.5, 'beta': 0.3, 'gamma': 0.2}
    adjustment_log = []

    total_nodes = len(nodes)
    active_threshold = 75
    degraded_count = 0
    critical_count = 0

    # First pass: count node states (uses health analysis)
    all_metrics = {}
    for node in nodes:
        node_id = node['id']
        status = node['status']
        load = node['load']
        errors = node['errors']

        # Simulated metric extraction
        cpu = min(load * 1.5, 100)
        memory = min(load * 1.2 + errors * 2, 100)
        latency = 20 + load * 0.8 + errors * 5
        packet_loss = errors * 0.7
        signal = 80 - load * 0.5 - errors * 3

        all_metrics[node_id] = {
            'cpu': cpu,
            'memory': memory,
            'latency': latency,
            'packet_loss': packet_loss,
            'signal_strength': signal
        }

        # Track state counts
        if status == 'active' and load > active_threshold:
            degraded_count += 1
        elif status == 'critical':
            critical_count += 1

    # Call to actual health analyzer (used)
    health_values = analyze_node_health(all_metrics)
    avg_health = sum(health_values) / len(health_values) if health_values else 0

    # Decoy: string analysis on node IDs (irrelevant)
    node_ids = [node['id'] for node in nodes]
    avg_id_length = string_length_analysis(node_ids)

    # Fake normalization based on ID length (never affects output)
    if avg_id_length > 3:
        adjustment_log.append('ID_LENGTH_HIGH')
        dummy_correction = 0.95
    else:
        adjustment_log.append('ID_LENGTH_LOW')
        dummy_correction = 1.05

    # Transform fake sensor stream (distractor)
    fake_sensor_stream = [
        (101, 23.5, 24.1, 23.9),
        (102, 25.0, 26.2, 24.8, 25.5),
        (103, 22.1, 21.9)
    ]
    sensor_weights = transform_sensor_data(fake_sensor_stream)
    bonus_factor = sum(sensor_weights.values()) * 0.01  # Minor red herring

    # Primary index calculation
    base_index = avg_health * 10  # Scale to larger integer range

    # Degradation penalties
    if degraded_count > total_nodes * 0.3:
        base_index *= 0.85
    if critical_count > 0:
        base_index *= 0.7

    # Final adjustments with misleading components
    final_multiplier = base_weights['alpha'] + base_weights['beta'] + base_weights['gamma']
    final_index = base_index * final_multiplier

    # Add irrelevant decimal precision via decoy path
    if 'gamma' in base_weights and bonus_factor > 0:
        final_index += bonus_factor * 10  # Small addition, looks important

    # Key execution point
    final_diagnostic = int(round(final_index))

    return final_diagnostic

# Generate test network configuration
network_nodes = [
    {'id': 1001, 'status': 'active', 'load': 60, 'errors': 2},
    {'id': 1002, 'status': 'active', 'load': 85, 'errors': 5},
    {'id': 1003, 'status': 'critical', 'load': 95, 'errors': 12},
    {'id': 1004, 'status': 'active', 'load': 40, 'errors': 1},
    {'id': 1005, 'status': 'active', 'load': 70, 'errors': 3}
]

# Execute main computation
final_diagnostic = compute_stability_index(network_nodes)
print(f"Result: {final_diagnostic}")