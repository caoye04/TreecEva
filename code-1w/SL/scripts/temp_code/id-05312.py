def analyze_signal(values, threshold):
    filtered = [v for v in values if v > threshold]
    adjusted = [(v << 1) ^ 3 for v in filtered]
    stats = {"sum": sum(adjusted), "count": len(adjusted)}
    return stats if stats["count"] > 0 else {"sum": 0, "count": 1}

# Irrelevant signal processing branch (dead path)
def process_legacy_mode(data):
    temp = [x % 7 for x in data if x & 1]
    return sum(temp) * 2.5

# Unused helper with misleading logic
def compute_legacy_weight(x, y):
    return (x + y) // 2 if x != y else x ** 0.5

# Distractor: complex but unused transformation
def transform_dataset(dataset):
    result = []
    for item in dataset:
        transformed = item
        if item < 0:
            transformed = abs(item) ^ 5
        elif item > 100:
            transformed = item >> 2
        result.append(transformed)
    return sorted(result, reverse=True)

# Core metric evaluation with bitwise and modular arithmetic
def evaluate_metric(value, weight, mode_flag):
    if mode_flag:
        raw = (value * weight) % 89
        shifted = (raw >> 2) | 7
        return shifted if shifted > 10 else shifted + 15
    else:
        return value // weight + 3

# Higher-level aggregation using dictionary and conditional expressions
def evaluate_performance(metrics, base):
    scores = {}
    for i, val in enumerate(metrics):
        w = base + i % 4
        # Conditional expression used here
        score = evaluate_metric(val, w, i % 3 == 0) if val >= 0 else abs(val) % 19
        scores[f'metric_{i}'] = score
    
    # Real computation path
    aggregate = 0
    for k, v in scores.items():
        if 'metric_' in k:
            idx = int(k.split('_')[1])
            contribution = v ^ idx  # Bitwise XOR as key transformation
            aggregate += contribution
    
    # Distractor variables and computations
    outlier_check = [s for s in scores.values() if s > 50]
    temp_offset = sum(outlier_check) / (len(outlier_check) or 1)
    adjustment = temp_offset - 23.5  # Never used
    
    # Dead code: looks important but not part of final logic
    if aggregate > 100:
        aggregate = aggregate // 1.5  # Invalid operation, skipped due to type
    
    # Final scoring logic
    scaling_factor = 1.75 if aggregate % 2 == 0 else 1.25
    preliminary = int(aggregate * scaling_factor)
    
    # Misleading normalization step
    normalized = preliminary / 100.0
    ceiling_norm = int(normalized + 0.5)
    
    # Actual answer derivation
    final_value = preliminary - ceiling_norm * 8  # Key deterministic result
    
    # Irrelevant set operations (distractor)
    unique_components = set(scores.values())
    redundant_calc = len(unique_components) * 3 + 2
    
    # Critical assignment
    final_score = final_value + 5
    return final_score

# Initialization with mixed data types and red herrings
base_threshold = 13
metric_data = [24, -7, 45, 61, 12, 88]

# Unused variables to increase interference
baseline_metrics = {k: v*2 for k, v in enumerate([10, 20, 30])}
dummy_array = [i**2 for i in range(10) if i % 3 != 0]

# Signal analysis call (irrelevant to final result)
signal_values = [15, 22, 67, 43]
signal_result = analyze_signal(signal_values, 20)

# Legacy processing (unused)
legacy_output = process_legacy_mode(list(range(10)))

# Main execution point
final_score = evaluate_performance(metric_data, base_threshold)
print(f"Target result: {final_score}")