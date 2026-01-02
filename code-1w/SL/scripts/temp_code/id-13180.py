from itertools import combinations

def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for a, b, c in combinations(sequence, 3):
        if a + c == 2 * b and a != b:
            count += 1
    return count

def calculate_rating(convergence, metrics):
    base = convergence * 1.5
    adjustment = 0
    temp_result = []
    
    # Distractor: irrelevant list processing
    dummy_data = [x ** 2 for x in range(8) if x % 2 == 0]
    processed = set()
    for val in dummy_data:
        processed.add(val % 5)
    
    # Real logic begins
    for k, v in metrics.items():
        if 'error' in k:
            adjustment -= v
        elif 'precision' in k or 'recall' in k:
            adjustment += v * 0.75
    
    # Dead code path (misleading)
    intermediate_state = None
    if adjustment > 10:
        intermediate_state = "over_optimized"
    elif adjustment < -5:
        intermediate_state = "under_performing"  # Never reached due to data

    # More distractors
    stats_summary = {}
    for i in range(3):
        stats_summary[f'placeholder_{i}'] = i * 2 + 1

    # Actual contribution
    outlier_flags = [v for v in metrics.values() if v > 90]
    if len(outlier_flags) >= 2:
        base *= 1.2
    
    final_rating = base + adjustment

    # Irrelevant sorting
    sorted_keys = sorted(metrics.keys())
    temp_dict = {k: metrics[k] for k in sorted_keys}

    return round(final_rating, 4)

# Main execution
sequence_data = [4, 6, 8, 10, 12]
sync_level = analyze_pattern(sequence_data)

metrics_log = {
    'error_rate': 12,
    'system_precision': 88,
    'convergence': 64,
    'recall_score': 92,
    'latency_ms': 45,
    'memory_usage': 2048
}

# Dummy dictionary operations
shadow_copy = metrics_log.copy()
shadow_copy.update({'temp_flag': True})
del shadow_copy['latency_ms']

# Key state variables
convergence = metrics_log['convergence']
activation_sequence = [sync_level, convergence]

# Trigger main calculation
final_score = calculate_rating(convergence, metrics_log)

# Print result as required
print(f"Result: {final_score}")