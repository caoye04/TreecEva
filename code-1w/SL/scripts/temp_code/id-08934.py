from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed computing environment
timestamped_logs = [
    {'node': 'A', 'load': 0.6, 'errors': 2, 'response_time': 120},
    {'node': 'B', 'load': 0.8, 'errors': 5, 'response_time': 180},
    {'node': 'C', 'load': 0.3, 'errors': 1, 'response_time': 90},
    {'node': 'A', 'load': 0.7, 'errors': 0, 'response_time': 130},
    {'node': 'B', 'load': 0.4, 'errors': 3, 'response_time': 110},
    {'node': 'C', 'load': 0.9, 'errors': 6, 'response_time': 200}
]

# Irrelevant statistical summary (distractor)
error_distribution = Counter([log['errors'] for log in timestamped_logs])
node_load_history = defaultdict(list)
for log in timestamped_logs:
    node_load_history[log['node']].append(log['load'])

# Misleading normalization function (dead code path)
def legacy_normalize(values):
    mean_val = sum(values) / len(values)
    return [(v - mean_val) / mean_val for v in values]

# Unused transformation matrix (red herring)
transform_matrix = [[1.0, -0.1], [0.05, 1.2]]

# Simulated baseline thresholds (distractor variables)
thresholds = {
    'high_load': 0.75,
    'max_errors': 4,
    'slow_response': 150
}

# Historical performance snapshot (irrelevant data)
historical_data = {
    'peak_load': 0.95,
    'avg_downtime': 1.2,
    'total_nodes': 5
}

# Core metric computation engine
metric_weights = {
    'stability': 0.4,
    'responsiveness': 0.35,
    'consistency': 0.25
}

# Raw results derived from logs
raw_results = {}

# Compute stability score based on load variance across nodes
node_loads = defaultdict(list)
for entry in timestamped_logs:
    node_loads[entry['node']].append(entry['load'])

variances = []
for node, loads in node_loads.items():
    mean_load = sum(loads) / len(loads)
    variance = sum((x - mean_load) ** 2 for x in loads) / len(loads)
    variances.append(variance)

overall_variance = sum(variances) / len(variances)
raw_results['stability'] = max(0, 100 * (1 - overall_variance))  # Inverse relationship

# Compute responsiveness score from response times
response_times = [log['response_time'] for log in timestamped_logs]
normalized_response = [1000 / (rt + 1) for rt in response_times]  # Higher is better
raw_results['responsiveness'] = sum(normalized_response) / len(normalized_response)

# Compute consistency score using error frequency
total_entries = len(timestamped_logs)
error_count = sum(log['errors'] for log in timestamped_logs)
error_rate = error_count / total_entries
raw_results['consistency'] = 100 * (1 - min(error_rate, 0.5))  # Capped at 50% error rate

# Auxiliary scoring function (partially used, adds confusion)
def calculate_adjusted_score(base, penalty_factor=1.0):
    return base * (0.95 ** penalty_factor)

# Secondary irrelevant transformation
shifted_scores = {k: v + 5 for k, v in raw_results.items()}

# Another decoy function that looks important but isn't used
def compute_reliability_index(data):
    if not data:
        return 0.0
    reliability = 0.0
    for item in data:
        reliability += math.exp(-item.get('errors', 0))
    return reliability / len(data)

# Key evaluation function combining weighted metrics
def evaluate_performance(weights, results):
    # Intermediate normalized scores
    norm_results = {}
    for key in results:
        # Normalize to 0-100 scale
        norm_results[key] = results[key]  # Already in approximate range
    
    # Apply weights and compute final weighted sum
    weighted_sum = 0.0
    for metric, weight in weights.items():
        if metric in norm_results:
            weighted_sum += norm_results[metric] * weight
    
    # Additional adjustment based on hidden logic
    adjustment_key = ''.join([chr(97 + (len(weights) * 2))])  # 'c'
    adjustment_map = {'a': 0.9, 'b': 0.95, 'c': 1.0, 'd': 1.05}
    final_adjustment = adjustment_map.get(adjustment_key, 1.0)
    
    # Final score calculation
    final_score = weighted_sum * final_adjustment
    
    # Introduce a conditional mutation that doesn't trigger (misdirection)
    debug_mode = False
    if debug_mode:  # Dead branch
        print(f"Debug: {norm_results}")
    
    return final_score

# Execute main evaluation
temp_result = evaluate_performance({'dummy': 0.5}, raw_results)  # Fake call (red herring)
final_score = evaluate_performance(metric_weights, raw_results)  # Actual target execution
print(f"Target result: {final_score}")