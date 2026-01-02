from collections import defaultdict, Counter

# Simulate system benchmark data with multiple test phases
def generate_test_data():
    raw_scores = [88, 92, 76, 94, 85, 90, 78, 83]
    phases = ['init', 'load', 'stress', 'peak', 'init', 'load', 'stress', 'peak']
    
    # Misleading transformation: irrelevant normalization
    normalized = [round((x - min(raw_scores)) / (max(raw_scores) - min(raw_scores)) * 100) for x in raw_scores]
    
    # Actual relevant data structure
    phase_map = defaultdict(list)
    for i, p in enumerate(phases):
        phase_map[p].append(raw_scores[i])
    
    return phase_map, normalized

# Auxiliary function that computes average but includes red herring logic
def compute_average_with_bias(data, bias_factor=0.0):
    """
    This function appears to adjust for bias, but bias_factor is unused in critical path.
    """
    total = sum(data)
    count = len(data)
    
    # Distractor: this conditional doesn't affect final result due to default argument
    adjustment = 0
    if bias_factor > 1:
        adjustment = int(bias_factor * 2)
    
    return round(total / count) + adjustment

# Secondary metric calculator - looks important but isn't used in final score
def calculate_stability_index(phase_data):
    all_vals = []
    for vals in phase_data.values():
        all_vals.extend(vals)
    range_val = max(all_vals) - min(all_vals)
    return round(100 - range_val, 2)

# Core performance calculation with slicing distraction
def calculate_performance(benchmark_data):
    # Extract only the 'load' and 'stress' phases for evaluation
    relevant_phases = ['load', 'stress']
    filtered_scores = []
    
    for phase in relevant_phases:
        if phase in benchmark_data:
            # Use slicing to take middle values (simulate filtering outliers)
            sorted_vals = sorted(benchmark_data[phase])
            mid_vals = sorted_vals[1:-1] if len(sorted_vals) > 2 else sorted_vals
            filtered_scores.extend(mid_vals)
    
    # Introduce distractor counter (looks diagnostic, not used)
    score_counter = Counter(filtered_scores)
    modes = [k for k, v in score_counter.items() if v == max(score_counter.values())]
    
    # Compute base performance - average of filtered scores
    base_perf = compute_average_with_bias(filtered_scores)
    
    # Apply weighting based on phase contribution (only two phases)
    load_avg = compute_average_with_bias(benchmark_data['load'])
    stress_avg = compute_average_with_bias(benchmark_data['stress'])
    
    # Final formula: harmonic mean approximation
    if load_avg > 0 and stress_avg > 0:
        weighted_harmonic = 2 * ((base_perf * stress_avg) / (base_perf + stress_avg))
    else:
        weighted_harmonic = base_perf
    
    # Final adjustment: use floor unless near threshold
    adjustment = 2 if abs(weighted_harmonic - 85.0) < 5 else 0
    final_score = int(weighted_harmonic) + adjustment
    
    # Irrelevant print statements (distraction)
    debug_info = f"Modes: {modes}, Stability: {calculate_stability_index(benchmark_data)}"
    
    return final_score

# Main execution flow
data_map, norm_data = generate_test_data()

# Unused variables - red herrings
baseline_shift = sum(norm_data) // len(norm_data)
drift_correction = [x - baseline_shift for x in norm_data]

# Key execution point
final_score = calculate_performance(data_map)

print(f"Result: {final_score}")