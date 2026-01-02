import math

# Simulated network telemetry data
def collect_telemetry(nodes):
    signal_strengths = {node: (hash(node) % 100 + 50) / 10.0 for node in nodes}
    return signal_strengths

def calculate_jitter(latency_list):
    mean = sum(latency_list) / len(latency_list)
    variance = sum((x - mean) ** 2 for x in latency_list) / len(latency_list)
    return math.sqrt(variance)

def evaluate_stability(metric_log):
    if not metric_log:
        return 0.0
    return sum(v * 0.9 ** i for i, v in enumerate(reversed(metric_log)))  # Exponential decay weighting

def analyze_bandwidth_capacity(link_count, base_rate=100):
    # Irrelevant calculation - decoy function
    total_capacity = 0
    for i in range(link_count):
        total_capacity += base_rate * (1.1 ** i)
    return total_capacity  # Not used in final result

def filter_anomalies(data_stream):
    threshold = sum(data_stream) / len(data_stream) * 1.5
    return [x for x in data_stream if x < threshold]

# Unused helper - dead code path
def deprecated_routing_score(path_matrix):
    score = 0
    for row in path_matrix:
        for val in row:
            score += val % 7
    return score

# Core logic with distractors
network_nodes = ['nexus_core', 'edge_01', 'edge_02', 'relay_alpha', 'relay_omega']
system_load = [85, 90, 92, 87, 89, 95, 91, 86]  # CPU load percentages over time

# Distractor variables
baseline_offset = 42
reference_checksum = hash('diagnostic_mode') % 1000
temporal_factor = len(system_load) * 0.5

# Simulate historical logs - irrelevant to final result
historical_diagnostics = {
    'day_1': [88, 87, 89],
    'day_2': [90, 91, 88],
    'day_3': [92, 93, 90]
}

# Misleading intermediate computation
aggregated_historical = sum(sum(v) for v in historical_diagnostics.values()) // 3

# Real-time signal data (used)
telemetry_data = collect_telemetry(network_nodes)

# Jitter analysis on system load (used in part)
jitter_metric = calculate_jitter(system_load)

# Prepare node weights based on signal (used)
node_weights = {node: int(strength) for node, strength in telemetry_data.items()}

# Dead code - never called
unused_shadow_map = {i: pow(2, i) for i in range(10)}

# Decoy data structure
phantom_cache = set()
for k in telemetry_data:
    phantom_cache.add(f"cached_{k}_diag")

# Another red herring: bandwidth capacity (not used)
link_count = len(network_nodes) - 1
calculated_bandwidth = analyze_bandwidth_capacity(link_count)

# Filtered load without outliers (used)
clean_load = filter_anomalies(system_load)

# Stability trend from recent behavior (used)
stability_index = evaluate_stability(clean_load)

# Auxiliary transformation - looks important but isn't used
transformed_signals = {k: round(v ** 1.1, 2) for k, v in telemetry_data.items()}

# Key intermediate: weighted signal sum (used)
weighted_signal_sum = sum(node_weights.values())

# Secondary metric: normalized jitter impact
jitter_impact = (jitter_metric / max(clean_load)) * 100

# Build diagnostic context using dictionary operations
context_map = {
    'nodes': set(network_nodes),
    'active_count': len(network_nodes),
    'baseline': baseline_offset,
    'checksum': reference_checksum
}

# Add unused metadata to distract
context_map.update({
    'version': '2.1',
    'mode': 'diagnostic'
})

# Compute secondary indicators
secondary_flags = []
if stability_index > 85:
    secondary_flags.append(1)
if jitter_impact < 5:
    secondary_flags.append(2)

# Critical cross-reference between sets and values
redundant_relays = {'relay_alpha', 'relay_omega'}
mission_critical = {'nexus_core'}
peripheral_nodes = context_map['nodes'] - redundant_relays - mission_critical

# Final aggregation using multiple concepts
# Only this function produces the target answer

# Additional distraction: bit manipulation that goes nowhere
distraction_key = 0
for w in node_weights.values():
    distraction_key ^= (w << 2) | (w >> 3)

# Actual final computation begins here
normalization_factor = len(clean_load)
effective_stability = stability_index * 0.95

# Composite score calculation
raw_composite = (
    effective_stability + 
    (weighted_signal_sum / 10.0) + 
    (100 - jitter_impact) + 
    (len(peripheral_nodes) * 5)
)

# Final adjustment using integer division and rounding
final_diagnostic = int(round(raw_composite // 1.05))

# Target result output
print(f"Result: {final_diagnostic}")