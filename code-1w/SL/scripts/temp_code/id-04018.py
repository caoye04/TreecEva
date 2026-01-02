import math

# Simulated sensor network diagnostic system
def analyze_sensor_health(raw_readings):
    healthy = set()
    degraded = set()
    for i, val in enumerate(raw_readings):
        if val > 75 and val < 95:
            healthy.add(i)
        elif val >= 95 or val <= 30:
            degraded.add(i)
    return healthy, degraded

# Legacy function - not used in current logic (red herring)
def legacy_normalization(data):
    max_val = max(data)
    return [x / max_val * 100 for x in data]

# Critical path: Flow optimization engine
def calculate_entropy(values):
    total = sum(values)
    probabilities = [(v / total) for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probabilities)


def detect_outlier_patterns(stream):
    moving_avg = [sum(stream[i:i+3]) / 3 for i in range(len(stream) - 2)]
    variance_spike = sum(1 for i in range(1, len(moving_avg)) if abs(moving_avg[i] - moving_avg[i-1]) > 15)
    return variance_spike > 2

# Main calculation pipeline
def calculate_optimal_flow(clusters, offset=0.0):
    # Extract primary and secondary nodes
    primary_nodes = [node for node in clusters if node['type'] == 'primary']
    secondary_nodes = [node for node in clusters if node['type'] == 'secondary']

    # Compute base flow from primaries
    base_flow = sum(node['reading'] * 1.1 for node in primary_nodes)

    # Apply environmental compensation (distraction: complex but partially unused)
    temp_factor = 0.95
    pressure_adj = 1.02
    humidity_comp = 0.98
    effective_flow = base_flow * temp_factor * pressure_adj

    # Secondary validation chain
    secondary_total = sum(node['reading'] for node in secondary_nodes)
    if secondary_total > 200:
        effective_flow *= 1.15

    # Entropy-based reliability weighting
    readings_only = [node['reading'] for node in primary_nodes]
    entropy = calculate_entropy(readings_only)
    reliability_weight = 0.8 + (entropy / 10)

    # Final adjustment with offset (used only if positive)
    final_flow = effective_flow * reliability_weight
    if offset > 0:
        final_flow += offset * 10

    # Dead code path - never executed due to fixed input (distractor)
    emergency_override = False
    if final_flow < 0:
        final_flow = 50
        emergency_override = True

    return final_flow

# Auxiliary debugging tool (never called)
def dump_system_state(nodes):
    return {n['id']: f"{n['status']}-{n['reading']}" for n in nodes}

# Simulated sensor cluster configuration
calibration_offset = -5.0
sensor_clusters = [
    {'id': 'S1', 'type': 'primary', 'reading': 88, 'status': 'active'},
    {'id': 'S2', 'type': 'primary', 'reading': 92, 'status': 'active'},
    {'id': 'S3', 'type': 'secondary', 'reading': 105, 'status': 'active'},
    {'id': 'S4', 'type': 'secondary', 'reading': 110, 'status': 'active'},
    {'id': 'S5', 'type': 'diagnostic', 'reading': 45, 'status': 'standby'}  # Not used in flow calc
]

# Diagnostic preprocessing (does not affect final result)
raw_diagnostics = [node['reading'] for node in sensor_clusters]
health_status = analyze_sensor_health(raw_diagnostics)

# Outlier detection on diagnostic stream (result not used)
detect_outlier_patterns(raw_diagnostics)

# Core execution point
optimized_flow_rate = calculate_optimal_flow(sensor_clusters, calibration_offset)

# Print final target result
print(f"Target result: {optimized_flow_rate}")