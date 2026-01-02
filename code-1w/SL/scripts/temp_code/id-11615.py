from collections import defaultdict
import math

# Simulate sensor data processing with noise filtering and performance evaluation
def preprocess_readings(raw_data):
    filtered = []
    noise_floor = 0.05
    for val in raw_data:
        if abs(val) > noise_floor:
            filtered.append(abs(val))
    return sorted(filtered, reverse=True)

# Heuristic to estimate signal reliability
def assess_reliability(sequence):
    if len(sequence) == 0:
        return 0.0
    variance = sum((x - sum(sequence)/len(sequence))**2 for x in sequence) / len(sequence)
    return round(math.exp(-variance), 4)

# Auxiliary function - counts transitions above threshold
def count_peaks(data, threshold=0.5):
    peaks = 0
    for i in range(1, len(data)):
        if data[i-1] < threshold <= data[i]:
            peaks += 1
    return peaks  # Not used in final result but looks relevant

# Main evaluation logic with weighted aggregation
def evaluate_performance(weights, outcomes):
    temp_results = defaultdict(float)
    total_weight = sum(weights.values())
    
    # Normalize weights
    normalized_weights = {k: v/total_weight for k, v in weights.items()}
    
    intermediate_log = []
    for metric, weight in normalized_weights.items():
        base_val = outcomes.get(metric, 0)
        adjusted = base_val * weight * 100
        temp_results[metric] = round(adjusted, 3)
        intermediate_log.append(f'{metric}: {adjusted:.3f}')
    
    # Apply non-linear bonus for high consistency
    consistency = outcomes.get('stability', 0)
    bonus_factor = 1 + math.tanh(consistency * 0.1)  # Scales bonus asymptotically
    
    aggregate = sum(temp_results.values()) * bonus_factor
    
    # Distractor computation: entropy-like measure (not used)
    if aggregate > 50:
        entropy_proxy = -sum(w * math.log(w + 1e-8) for w in normalized_weights.values())
        entropy_proxy = round(entropy_proxy, 4)
    
    # Final adjustment based on outlier ratio (precomputed)
    top_3_ratio = sum(sorted(outcomes.values(), reverse=True)[:3]) / sum(outcomes.values()) if outcomes else 0
    final_adjustment = 0.9 + 0.2 * top_3_ratio
    
    return int(round(aggregate * final_adjustment))

# Simulated input data from multi-sensor array
raw_metrics = [0.12, -0.03, 0.81, 0.44, -0.67, 0.0, 0.93, -0.25, 0.18]
cleaned = preprocess_readings(raw_metrics)

# Assign semantic labels to top readings
labels = ['stability', 'response_time', 'power_efficiency', 'thermal_output']
label_mapping = {i: labels[i % len(labels)] for i in range(len(cleaned))}

# Build outcome map using lambda transformation
outcome_builder = lambda vals, lbls: {lbls[i]: round(v * 0.76 + 0.1, 2) for i, v in enumerate(vals)}
raw_outcomes = outcome_builder(cleaned[:4], [labels[0], labels[1], labels[2], labels[3]])

# Add extra keys to mislead focus
raw_outcomes['calibration'] = 0.5
raw_outcomes['baseline_drift'] = 0.14

# Weight configuration for evaluation
metric_weights = {
    'stability': 0.3,
    'response_time': 0.25,
    'power_efficiency': 0.25,
    'thermal_output': 0.2
}

# Additional irrelevant tracking
state_tracker = defaultdict(int)
for k in ['init', 'sync', 'process', 'finalize']:
    state_tracker[k] += 1

# Key execution point
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Print result as required
print(f"Result: {final_score}")