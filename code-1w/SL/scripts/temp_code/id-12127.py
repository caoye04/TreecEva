def analyze_efficiency(data, threshold=0.75):
    """ Irrelevant analysis function (dead code path) """
    return sum(x > threshold for x in data) / len(data)

# Distractor variables (irrelevant to final result)
decoy_metrics = [0.82, 0.71, 0.93, 0.64]
decoy_weights = [0.1, 0.3, 0.4, 0.2]
temp_results = []
scaling_factor = 1.25
normalization_offset = 0.05

# Real data hidden among distractors
metrics = [0.9, 0.8, 0.7, 0.6]  # Performance metrics across four subsystems
weights = [0.4, 0.3, 0.2, 0.1]  # Weighted importance of each subsystem

# Misleading intermediate calculation (not used in final answer)
weighted_avg = sum(m * w for m, w in zip(decoy_metrics, decoy_weights))
adjusted_avg = weighted_avg * scaling_factor - normalization_offset

# Auxiliary function that looks important but is never called
def compute_stability_index(seq, window=3):
    return [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))] if len(seq) > 1 else [0]

# Bit manipulation red herring
flag_register = 0b1101
flag_register ^= 0b1010  # XOR with arbitrary mask
flag_register |= 0b0011  # OR with another mask
status_check = bin(flag_register).count('1')

# More decoys
log_entries = [{'level': 'INFO', 'value': x * 0.1} for x in range(10)]
summary_stats = {f'stats_{i}': {'min': 0, 'max': 0} for i in range(3)}

# Core logic disguised within distractions
def evaluate_performance(measures, importance):
    """ Computes weighted harmonic mean of performance metrics """
    if not measures or not importance:
        return 0.0
    
    # Filter out negligible components (conceptual red herring: none are actually filtered)
    valid_pairs = [(m, w) for m, w in zip(measures, importance) if m > 0.01]
    
    # Simulate conditional complexity with always-true branch
    adjustment = 1.0
    if len(valid_pairs) == len(measures):  # Always true
        # Use enumerate to add index-based adjustment (only some indices matter)
        adjustments = []
        for idx, (metric_val, weight_val) in enumerate(valid_pairs):
            if idx % 2 == 0:
                # Apply non-linear transformation on even indices
                adjusted_metric = 1 / (1 + 0.1 * idx + (1 - metric_val))
            else:
                adjusted_metric = metric_val * (1 + 0.05 * idx)
            adjustments.append(adjusted_metric)
        
        # Combine using harmonic mean with weights
        weighted_inv_sum = sum(w / v for w, v in zip(importance, adjustments))
        adjustment = len(valid_pairs) / weighted_inv_sum if weighted_inv_sum != 0 else 0
    
    # Secondary red herring: unused lambda
    outlier_filter = lambda x, thres=0.5: x if x > thres else thres
    
    # Final score computed through complex but deterministic path
    base_score = sum(m * w for m, w in zip(measures, importance))
    return int(round(base_score * adjustment * 100))

# Unused list transformation
processed_data = list(map(lambda x: x * 2, [1, 2, 3]))

# Key statement — the actual computation of interest
final_score = evaluate_performance(metrics, weights)

# Another dead path
if __name__ == '__main__':
    debug_mode = False
    if debug_mode:
        print("Debug:", analyze_efficiency([0.5, 0.6, 0.7]))

print(f"Target result: {final_score}")