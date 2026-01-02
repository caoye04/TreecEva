from itertools import combinations
from math import log

# Simulated system metrics from a distributed data processing pipeline
task_durations = [120, 95, 134, 88, 105, 118, 99]
error_counts = [2, 0, 1, 0, 3, 1, 0]
resource_usage = [78, 65, 88, 60, 73, 81, 67]

# Irrelevant auxiliary data (distractor)
user_sessions = [12, 15, 10, 8, 20, 14, 11]
dummy_flags = [True, False, True, True, False, True, False]

# Weight configuration for performance evaluation (meaningful)
weights = {'duration': 0.4, 'errors': 0.35, 'resources': 0.25}

# Misleading normalization factors (red herring - not actually used in final calc)
normalization_factor_v1 = max(task_durations)
normalization_factor_v2 = sum(task_durations) / len(task_durations)
scaling_offset = 1e-3

# Auxiliary function that appears important but is unused (dead code path)
def legacy_normalize(data):
    return [x / max(data) for x in data]

# Another decoy function with plausible name
def calculate_reliability_index(errors, duration):
    if sum(errors) == 0:
        return 100.0
    return 100 * (1 - sum(errors) / (len(errors) * 3))

# Core evaluation logic
valid_nodes = [i for i in range(len(task_durations)) if error_counts[i] <= 1]
filtered_durations = [task_durations[i] for i in valid_nodes]
filtered_resources = [resource_usage[i] for i in valid_nodes]

# Compute efficiency ratios using combinatorics (actual relevant use of itertools)
efficiency_pairs = []
for a, b in combinations(range(len(filtered_durations)), 2):
    time_ratio = filtered_durations[a] / filtered_durations[b]
    resource_ratio = filtered_resources[a] / filtered_resources[b]
    if time_ratio > 1.1 or resource_ratio < 0.9:
        efficiency_pairs.append(abs(time_ratio - resource_ratio))

total_efficiency_gap = sum(efficiency_pairs)

# Secondary metric: stability score based on variation
stability_score = 0
for i in range(1, len(filtered_durations)):
    diff = abs(filtered_durations[i] - filtered_durations[i-1])
    stability_score += log(1 + diff)

# Simulated threshold filter (irrelevant intermediate result)
threshold_exceedances = [dur for dur in task_durations if dur > 110]
phantom_metric = len(threshold_exceedances) * scaling_offset

# Build comprehensive metrics dictionary
metrics = {
    'avg_duration': sum(filtered_durations) / len(filtered_durations),
    'total_efficiency_gap': total_efficiency_gap,
    'stability_score': stability_score,
    'node_count': len(valid_nodes),
    'raw_resource_avg': sum(filtered_resources) / len(filtered_resources)
}

# Dummy set operations for distraction (set theory red herring)
active_indices = set(range(7))
failed_indices = {i for i, e in enumerate(error_counts) if e > 1}
recovered_indices = active_indices - failed_indices
duplicate_check = recovered_indices & {3, 4, 5} | {99, 100}  # includes invalid ids

# Another irrelevant transformation chain
temp_scores = []
for val in user_sessions:
    temp = val * 1.05
    temp = round(temp, 1)
    temp_scores.append(temp)

# Critical function: evaluates system performance
def evaluate_performance(met, w):
    # Normalize components to prevent dominance by scale
    norm_duration = met['avg_duration'] / 100.0
    norm_gap = min(met['total_efficiency_gap'] / 10.0, 5.0)  # capped impact
    norm_stability = met['stability_score'] / 5.0
    
    # Weighted combination
    duration_component = (1 - norm_duration) * w['duration']
    error_component = (5 - norm_gap) * w['errors']
    resource_component = (1 - norm_stability) * w['resources']
    
    # Final aggregation
    raw_score = duration_component + error_component + resource_component
    
    # Adjust by node count with diminishing returns
    adjustment_factor = met['node_count'] ** 0.5 / 3.0
    return raw_score * adjustment_factor

# Execute critical statement
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")