from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.4, 'errors': 2, 'priority': 'high'},
    {'node': 'B', 'load': 0.8, 'errors': 5, 'priority': 'medium'},
    {'node': 'C', 'load': 0.3, 'errors': 1, 'priority': 'high'},
    {'node': 'D', 'load': 0.9, 'errors': 8, 'priority': 'low'},
    {'node': 'E', 'load': 0.6, 'errors': 3, 'priority': 'medium'}
]

# Irrelevant helper that looks important but isn't used in critical path
def legacy_normalization(data):
    return [max(0, x - 0.1) for x in data]

# Decoy function - appears useful but never called
def calculate_reliability_index(nodes):
    return sum([1 / (1 + node['errors']) for node in nodes])

# Unused utility for bit manipulation red herring
def bitmask_from_status(status_code):
    return (status_code << 2) ^ 0xFF

# Core processing functions
def aggregate_by_priority(logs):
    aggregated = defaultdict(lambda: {'total_load': 0, 'total_errors': 0, 'count': 0})
    priority_weight = {'low': 1, 'medium': 2, 'high': 3}
    
    for entry in logs:
        p = entry['priority']
        aggregated[p]['total_load'] += entry['load']
        aggregated[p]['total_errors'] += entry['errors']
        aggregated[p]['count'] += 1
        
        # Distractor computation with fake significance
        if entry['load'] > 0.7:
            aggregated[p]['total_load'] *= 0.95  # misleading adjustment

    return aggregated

def compute_efficiency_ratio(aggregated_data):
    ratios = {}
    for priority, stats in aggregated_data.items():
        avg_load = stats['total_load'] / stats['count']
        avg_errors = stats['total_errors'] / stats['count']
        # Real metric: efficiency penalized by error rate and high load
        ratios[priority] = (1 - avg_load) * (1 / (1 + avg_errors))
    return ratios

def derive_stability_vector(telemetry):
    # Another plausible but unused path
    error_counts = [t['errors'] for t in telemetry]
    return [math.exp(-e * 0.1) for e in error_counts]

# Configuration that looks configurable but is actually hardcoded in logic
baseline_config = {
    'threshold': 0.75,
    'weight_map': {'high': 2.0, 'medium': 1.3, 'low': 0.8},
    'decay_factor': 0.9,
    'use_legacy_scaling': False  # This key is never read
}

# Main evaluation logic - this is where the real computation happens
def evaluate_performance(logs, config):
    # Step 1: Aggregate by priority (used)
    agg_data = aggregate_by_priority(logs)
    
    # Step 2: Compute efficiency ratios (used)
    efficiency = compute_efficiency_ratio(agg_data)
    
    # Step 3: Extract weights from config (only weight_map is used)
    weights = config['weight_map']
    
    # Step 4: Calculate weighted performance score
    raw_score = 0
    for priority in weights:
        if priority in efficiency:
            raw_score += weights[priority] * efficiency[priority]
    
    # Step 5: Apply arbitrary scaling to produce final result
    scaled_score = raw_score * 100
    
    # Red herring: fake normalization that doesn't affect outcome
    if config['use_legacy_scaling']:
        scaled_score = legacy_normalization([scaled_score])[0]
    
    # Final transformation
    final_value = int(scaled_score + 0.5)  # round to nearest integer
    
    # Dead code branch - unreachable due to prior int conversion
    if isinstance(final_value, float):
        final_value = math.ceil(final_value)
    
    return final_value

# Irrelevant data structure that seems related
historical_trends = Counter(['peak', 'normal', 'peak', 'degraded'])

# Simulate auxiliary diagnostic check (unused)
diagnostic_matrix = [[telemetry_stream[i]['errors'] for _ in range(2)] for i in range(len(telemetry_stream))]

# Critical execution point
metrics_log = telemetry_stream
final_score = evaluate_performance(metrics_log, baseline_config)

# Output the target result
print(f"Result: {final_score}")