from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [120, 85, 90, 110, 95, 130, 100]
    processed = defaultdict(int)
    for i, val in enumerate(raw_data):
        if val > 100:
            processed['high'] += 1
        else:
            processed['low'] += 1
    return dict(processed)

# Weighting function for different metric categories
compute_weights = lambda x: round((x[1] * 1.5 + x[0] * 0.8) / sum(x), 3)

# Red herring: irrelevant statistical computation
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

irrelevant_stats = calculate_variance([5, 12, 8, 20, 14, 7])

# Main evaluation logic
def evaluate_performance(metrics, weights):
    base = metrics.get('high', 0) * weights[0]
    penalty = metrics.get('low', 0) * weights[1]
    adjustment_factor = (metrics.get('high', 0) - metrics.get('low', 0))
    
    # Nested conditional with misleading branches
    if adjustment_factor > 0:
        base *= 1.1
    elif adjustment_factor == 0:
        base *= 0.95
    else:
        base *= 0.85  # Strong penalty

    temp_result = base - penalty  # Intermediate tracking
    extra_offset = 0
    
    # Unnecessary loop that computes unrelated count
    redundant_count = 0
    for i in range(1, 6):
        for j in range(1, 4):
            if (i + j) % 2 == 0:
                redundant_count += 1  # This does nothing meaningful

    # More red herrings
    dummy_slice = [10, 20, 30, 40, 50][1:4:2]  # [20, 40] — unused
    flag_check = any(x > 25 for x in dummy_slice)  # Always True, not used

    # Final adjustment using case-insensitive mapping (semi-relevant)
    mode = 'STANDARD'.lower()
    if mode == 'standard':
        extra_offset = 5
    elif mode == 'aggressive':
        extra_offset = -3
    else:
        extra_offset = 0

    final_value = temp_result + extra_offset
    return int(round(final_value))

# Execution flow
metrics = collect_metrics()  # {'high': 4, 'low': 3}
weight_vector = (2.0, 1.2)
scaling_weight = compute_weights((4, 3))  # Irrelevant: ~1.029

# Key statement
final_score = evaluate_performance(metrics, weight_vector)

print(f"Result: {final_score}")