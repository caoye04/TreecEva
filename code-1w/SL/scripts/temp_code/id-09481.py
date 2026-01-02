import itertools

# Simulated system performance metrics from various subsystems
def collect_metrics():
    base_load = 78
    peak_spike = 92
    avg_response = (base_load + peak_spike) / 2
    jitter = (peak_spike - base_load) * 0.3
    efficiency_ratio = base_load / peak_spike
    
    # Irrelevant telemetry (distraction)
    ambient_temp = 23.5
    fan_rpm = 2400
    power_draw_watts = 89.2
    
    return {
        'latency': avg_response,
        'throughput': base_load,
        'reliability': efficiency_ratio,
        'scalability': peak_spike,
        'stability': 100 - jitter
    }

# Weighting schema for evaluation (some weights are decoys)
def get_weights():
    criticality = {
        'latency': 0.30,
        'throughput': 0.25,
        'reliability': 0.20,
        'scalability': 0.15,
        'stability': 0.10
    }
    
    # Unused weight sets (dead code paths - distraction)
    legacy_schema = {'old_a': 0.5, 'old_b': 0.5}
    experimental = {k: v * 1.1 for k, v in criticality.items()}
    
    return criticality

# Auxiliary function that appears useful but isn't used directly
def normalize(value, min_val=0, max_val=100):
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0

# Bit manipulation red herring
def obfuscate_key(n):
    shifted = (n << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return (toggled >> 2) | (n << 1)

# Main evaluation logic with distractors
def evaluate_performance(metrics, weights):
    # Initialize accumulator
    raw_score = 0.0
    
    # Apply weighted sum using only specific keys (ignore extras)
    relevant_keys = ['latency', 'throughput', 'reliability']
    
    # Distractor: unused transformation map
    transform_map = {key: round(val ** 0.5, 4) for key, val in metrics.items()}
    
    # Real computation happens here — moderate nesting with filtering
    for key in weights.keys():
        if key not in metrics:
            continue
        contribution = metrics[key] * weights[key]
        
        # Conditional adjustment (only applies to one element)
        if key == 'latency':
            adjusted = contribution * 0.95  # minor penalty
        else:
            adjusted = contribution
        
        # Only accumulate contributions from relevant keys
        if key in relevant_keys:
            raw_score += adjusted
        
        # Dead branch with misleading calculation
        if key == 'scalability':
            hypothetical = contribution * 1.2
            raw_score -= 0  # No-op to mislead
    
    # Additional irrelevant data structure
    audit_log = [
        f"Metric processed at {len(metrics)} points",
        f"Final raw: {raw_score:.3f}"
    ]
    
    # Secondary adjustment phase
    multiplier = 1.0
    if raw_score > 20:
        multiplier = 1.05
    elif raw_score < 15:
        multiplier = 0.95
    
    # Final scaling
    final_raw = raw_score * multiplier
    
    # Red herring: tuple unpacking with dummy values
    backup, _, recovery_point = (final_raw * 0.9, 42, final_raw * 1.1)
    
    # Real final score derived from controlled transformation
    temp_result = final_raw + (metrics['stability'] * weights['stability'])
    
    # One-liner list comprehension that produces unused result
    snapshots = [obfuscate_key(int(metrics[k])) for k in metrics.keys() if isinstance(metrics[k], (int, float))]
    
    # Actual answer derivation
    final_score = round(temp_result, 4)
    
    # Print required output format
    print(f"Result: {final_score}")
    
    return final_score

# Orchestration block
if __name__ == "__main__":
    # Collect real data
    metrics = collect_metrics()
    
    # Retrieve weighting scheme
    weights = get_weights()
    
    # Compute final score
    final_score = evaluate_performance(metrics, weights)
    
    # Ensure output is printed as specified
    # Result already printed inside function
