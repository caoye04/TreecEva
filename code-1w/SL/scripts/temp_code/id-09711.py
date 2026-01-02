from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_log = [
    {'event': 'task_start', 'timestamp': 100, 'priority': 3},
    {'event': 'data_load', 'timestamp': 105, 'priority': 2},
    {'event': 'compute_cycle', 'timestamp': 112, 'priority': 4},
    {'event': 'task_start', 'timestamp': 120, 'priority': 3},
    {'event': 'io_wait', 'timestamp': 125, 'priority': 1},
    {'event': 'compute_cycle', 'timestamp': 135, 'priority': 5},
    {'event': 'task_complete', 'timestamp': 142, 'priority': 3}
]

# Irrelevant telemetry aggregation (distraction)
def analyze_patterns(log):
    freq_map = defaultdict(int)
    for entry in log:
        freq_map[entry['event']] += 1
    return dict(freq_map)

telemetry_freq = analyze_patterns(telemetry_log)  # Unused later

# System health monitor (red herring)
health_flags = set()
critical_events = {'io_wait', 'failure'}
for event in telemetry_log:
    if event['event'] in critical_events and event['priority'] > 3:
        health_flags.add('HIGH_PRIORITY_IO')

# Core processing begins
raw_outcomes = [88, 92, 76, 85, 93]  # Performance metrics from test runs
event_categories = ['start', 'load', 'compute', 'start', 'wait', 'compute', 'complete']

# Misleading transformation chain (dead path)
normalized_data = [x / max(raw_outcomes) for x in raw_outcomes]
discounted_scores = [round(x * 0.95, 2) for x in normalized_data]  # Not used

# Bit manipulation decoy
def hash_magnitude(value):
    shifted = (value << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return toggled % 10

hash_sequence = [hash_magnitude(x) for x in raw_outcomes]  # Computed but unused

# Weight configuration for evaluation (critical)
metric_weights = {
    'accuracy': 0.4,
    'efficiency': 0.3,
    'consistency': 0.2,
    'robustness': 0.1
}

# Auxiliary statistical analysis (distractor)
def calculate_spread(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

spread = calculate_spread(raw_outcomes)  # Calculated but not part of final score
extreme_values = {x for x in raw_outcomes if x < 80 or x > 90}  # Unused set

# Core evaluation logic with nested dependencies
def assess_consistency(metrics):
    pairs = [(metrics[i], metrics[i+1]) for i in range(len(metrics)-1)]
    deviations = [abs(a - b) for a, b in pairs]
    avg_deviation = sum(deviations) / len(deviations)
    return 100 * (1 - min(avg_deviation / 20, 0.8))

def compute_efficiency_factor(n):
    if n <= 1:
        return 1
    return n * compute_efficiency_factor(n - 1)  # Recursive but unused result

# Real scoring components
base_accuracy = sum(raw_outcomes) / len(raw_outcomes)
consistency_score = assess_consistency(raw_outcomes)
efficiency_heuristic = len([e for e in telemetry_log if e['event'] == 'compute_cycle']) * 10

# Complex conditional weighting (key logic)
def evaluate_performance(weights, outcomes):
    acc = sum(outcomes) / len(outcomes)
    
    # Nested structure with distractors
    temp_results = {}
    temp_results['accuracy'] = acc
    temp_results['consistency'] = assess_consistency(outcomes)
    temp_results['efficiency'] = efficiency_heuristic
    temp_results['robustness'] = 85 if len(extreme_values) < 3 else 60  # Uses outer scope
    
    # Final weighted combination
    final = 0.0
    for key, weight in weights.items():
        if key == 'accuracy':
            final += weight * temp_results['accuracy']
        elif key == 'consistency':
            final += weight * temp_results['consistency']
        elif key == 'efficiency':
            # Efficiency scaled to 0-100
            scaled = min(temp_results['efficiency'], 100)
            final += weight * scaled
        elif key == 'robustness':
            final += weight * temp_results['robustness']
    
    # Additional adjustment based on outlier count (uses closure)
    outlier_count = len([x for x in outcomes if abs(x - acc) > 10])
    if outlier_count >= 2:
        final *= 0.95  # Penalty
    
    return round(final, 4)

# Execution point of interest
final_score = evaluate_performance(metric_weights, raw_outcomes)
print(f"Target result: {final_score}")