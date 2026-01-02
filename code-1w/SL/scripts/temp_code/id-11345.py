import itertools

def analyze_trends(data, threshold=0.5):
    """Irrelevant function analyzing trends (dead code path)."""
    moving_avg = [sum(data[i:i+3]) / 3 for i in range(len(data)-2)]
    return [x for x in moving_avg if x > threshold]

# Irrelevant constants and decoy data structures
trend_data = [0.1, 0.7, 0.8, 0.3, 0.9]
decoy_matrix = [[i * j for j in range(5)] for i in range(5)]  # Unused matrix
useless_pairs = list(itertools.combinations([1, 2, 3], 2))

# Core system parameters (some relevant, some not)
base_multiplier = 1.5
scaling_factor = 2.0  # Used later
offset_correction = -0.25  # Never used

# Metric weights — only some are actually used
candidate_metrics = ['accuracy', 'latency', 'throughput', 'reliability']
metric_weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.2,
    'reliability': 0.1,
    'usability': 0.05  # Distractor weight (not used)
}

# Raw outcomes from testing (only specific indices matter)
raw_outcomes = [
    {'accuracy': 0.92, 'latency': 45, 'errors': 2},
    {'accuracy': 0.88, 'latency': 52, 'errors': 1},
    {'accuracy': 0.95, 'latency': 40, 'errors': 3}
]

# Auxiliary transformation map (partially used)
score_mapping = {i: val for i, val in enumerate([1.0, 0.8, 0.6, 0.4, 0.2])}

# Decoy aggregation using itertools (never invoked)
def compute_aggregated_risk(profiles):
    all_perms = list(itertools.permutations(profiles, 2))
    risk_sum = 0
    for p1, p2 in all_perms:
        risk_sum += abs(p1['accuracy'] - p2['accuracy'])
    return risk_sum / (len(profiles) + 1)

# Linear search for best candidate based on adjusted score
def find_top_candidate(results, weights):
    max_score = -1
    best_idx = -1
    for idx in range(len(results)):
        r = results[idx]
        # Compute composite score
        acc_score = r['accuracy'] * weights['accuracy']
        # Latency penalty: invert and scale (lower latency = better)
        latency_norm = (100 - r['latency']) / 100.0
        lat_score = latency_norm * weights['latency']
        thrpt_score = min(r['accuracy'], 0.93) * weights['throughput']  # Capped logic
        rel_score = (1 - r['errors'] * 0.05) * weights['reliability']
        total = acc_score + lat_score + thrpt_score + rel_score
        if total > max_score:
            max_score = total
            best_idx = idx
    return best_idx, max_score

# Recursive depth limiter (distractor)
def validate_hierarchy(level, depth=0):
    if depth >= 3:
        return False
    if level == 'final':
        return True
    return validate_hierarchy(level, depth + 1)

# Main evaluation logic
def preprocess_entry(entry):
    # Normalize accuracy to capped range
    entry['accuracy'] = min(entry['accuracy'], 0.95)
    return entry

def evaluate_performance(weights, outcomes):
    processed = [preprocess_entry(out) for out in outcomes]
    
    # Determine top performer index
    top_idx, base_score = find_top_candidate(processed, weights)
    
    # Apply scaling factor (defined earlier)
    adjusted_score = base_score * scaling_factor
    
    # Bit manipulation red herring
    magic_offset = (top_idx << 2) ^ 5  # Computed but unused
    
    # Additional irrelevant calculation chain
    temp_vals = [processed[i]['accuracy'] * (i+1) for i in range(len(processed))]
    avg_temp = sum(temp_vals) / len(temp_vals)
    perturbation = abs(avg_temp - 0.88) * 10
    
    # Final scoring uses only adjusted_score and top_idx in non-obvious way
    final_component = adjusted_score + (top_idx * 0.01)
    
    # Dead branch — looks important but never executed
    if validate_hierarchy('intermediate'):
        final_component *= 0.9
    
    # Critical result computation
    final_component = round(final_component, 6)
    
    # Spurious use of itertools
    redundant_combo_check = list(itertools.chain.from_iterable(
        [(i, j) for j in range(i)] for i in range(3)
    ))
    
    return final_component

# Execution point of interest
final_score = evaluate_performance(metric_weights, raw_outcomes)
print(f"Result: {final_score}")