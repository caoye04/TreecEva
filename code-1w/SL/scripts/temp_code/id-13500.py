import math

# Simulated system performance analyzer with distractions
def analyze_component_health(sensor_data, threshold=75):
    # Irrelevant health check with dead-end logic
    overload_count = 0
    stress_factor = 0.0
    for val in sensor_data:
        if val > threshold:
            overload_count += 1
            stress_factor += (val - threshold) * 1.5
    normalized_stress = stress_factor / (len(sensor_data) + 1e-8)
    return normalized_stress  # Unused in final logic

# Distractor function: network latency simulation
def simulate_latency(nodes, base_delay=2):
    route_delays = {}
    for i, node in enumerate(nodes):
        delay = (base_delay + i % 3) * (i + 1)
        route_delays[node] = delay
    return route_delays  # Computationally heavy but unused

# Core metric processor - actually used
def transform_metrics(raw_values):
    transformed = []
    shift_key = 3
    for x in raw_values:
        shifted = x >> 1  # Bit manipulation
        adjusted = (shifted * 1.7) + 2.5
        transformed.append(round(adjusted, 4))
    return transformed

# Data fusion engine
def fuse_datasets(primary, secondary):
    fused = {}
    for k in primary:
        if k in secondary:
            fused[k] = primary[k] * secondary[k]
        else:
            fused[k] = primary[k] ** 1.1
    return fused

# Real processing chain
benchmark_config = {
    'version': 'X2',
    'scaling_factor': 1.8,
    'thresholds': [60, 70, 85],
    'weights': {'perf': 0.6, 'mem': 0.4},
    'active': True
}

# Raw diagnostic readings (simulated)
machine_readings = [88, 92, 76, 81, 85]
memory_trace = [65, 70, 72, 68, 75]

# Irrelevant intermediate transformations
temporal_peaks = [x for x in machine_readings if x > 80]
baseline_offset = sum(memory_trace) / len(memory_trace)

# Decoy data structures
network_graph = {'node_a': [1,2], 'node_b': [3,4], 'node_c': [5,6]}
packet_routes = set()
for k in network_graph:
    packet_routes.add(f"route_{k[-1]}")

# Key data pipeline begins here
raw_metrics = {
    'cpu_raw': machine_readings,
    'mem_raw': memory_trace
}

# Apply transformation to flat list
cpu_processed = transform_metrics(machine_readings)
mem_processed = transform_metrics(memory_trace)

# Build metrics log - relevant structure
metrics_log = {
    'cpu': sum(cpu_processed) / len(cpu_processed),
    'mem': sum(mem_processed) / len(mem_processed),
    'timestamp': '2024-05-17',
    'sequence_id': 918273
}

# Secondary weighting map
weight_map = {
    'cpu': benchmark_config['weights']['perf'],
    'mem': benchmark_config['weights']['mem']
}

# Fused evaluation (only this matters)
fused_metrics = fuse_datasets(metrics_log, weight_map)

# Auxiliary noise variables
drift_correction = 0.0
for i in range(5):
    drift_correction += math.sin(i) * 0.1

# Critical red herring: looks important but unused
aggregated_diagnostics = {
    'health_index': analyze_component_health(machine_readings),
    'latency_profile': simulate_latency(['A', 'B', 'C', 'D']),
    'peak_load': max(machine_readings),
    'stability_ratio': temporal_peaks.count(85) / len(temporal_peaks)
}

# Core scoring logic
config_scale = benchmark_config['scaling_factor']

# Final computation path
weighted_cpu = fused_metrics['cpu'] * config_scale
weighted_mem = fused_metrics['mem'] * config_scale

# Determine execution mode based on version
mode_multiplier = 1.0
if benchmark_config['version'] == 'X2':
    mode_multiplier = 1.25
elif benchmark_config['version'] == 'X1':
    mode_multiplier = 0.9

interim_score = (weighted_cpu + weighted_mem) * mode_multiplier

# Apply final nonlinear adjustment
final_score = int((interim_score ** 1.1) - 450)

# Output result as required
print(f"Result: {final_score}")