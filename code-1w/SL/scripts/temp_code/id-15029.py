from itertools import compress, cycle

def analyze_pattern(sequence):
    # Irrelevant helper function that analyzes sequence patterns but not used in final result
    changes = [b - a for a, b in zip(sequence, sequence[1:])]
    trend = sum(1 for c in changes if c > 0) - sum(1 for c in changes if c < 0)
    return trend

def normalize(data):
    # Normalizes data but this function is actually unused
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def evaluate_performance(metrics, weights):
    # Core logic: weighted harmonic mean with filtering
    filtered_metrics = [m for m in metrics if m > 0.1]  # Remove near-zero metrics
    
    # Misleading intermediate calculation
    avg_metric = sum(metrics) / len(metrics)
    temp_adjustment = avg_metric * 0.05  # Distractor adjustment not used later
    
    # Weight cycling to match metric count
    weight_cycle = list(cycle(weights))[:len(filtered_metrics)]
    
    # Introduce redundant tuple unpacking
    pairs = list(zip(filtered_metrics, weight_cycle))
    values, applied_weights = zip(*pairs)
    
    # Compute weighted harmonic mean
    weighted_inv_sum = sum(w / v for v, w in pairs)
    total_weight = sum(applied_weights)
    
    # Secondary distractor: simulate confidence interval
    variance_proxy = sum((v - avg_metric)**2 for v in metrics) / len(metrics)
    margin_of_error = (variance_proxy ** 0.5) * 0.1  # Not actually used
    
    # Final computation
    result = total_weight / weighted_inv_sum
    
    # Additional red herring: adjust based on sequence trend (but never called)
    dummy_seq = [1, 3, 2, 4, 5]
    trend_bias = analyze_pattern(dummy_seq)  # Computed but unused
    
    return result

# Main execution
raw_data = [0.85, 0.92, 0.78, 0.0, 0.96, 0.88, 0.0]  # Two zero entries to be filtered out
base_weights = [0.2, 0.3, 0.25, 0.15]

# Preprocessing distraction: string-based flag handling
flags = "enabled, active, verified"
flag_list = flags.split(', ')
enabled_modes = set(flag_list)  # Unused in logic

# Another irrelevant list transformation
shifted_data = [x + 0.01 for x in raw_data if x > 0]  # Slight shift, not used

# Key execution point
final_score = evaluate_performance(raw_data, base_weights)

print(f"Result: {final_score}")