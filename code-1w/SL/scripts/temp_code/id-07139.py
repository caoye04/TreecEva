def analyze_metrics(x, y):
    temp_a = x ** 2 + y * 3
    temp_b = (x + y) % 7
    irrelevant_sum = 0
    for i in range(5):
        irrelevant_sum += i ** 3  # Distractor loop
    if temp_b > 4:
        return temp_a - 10
    return temp_a + 5


def compute_bias_factor(a, b):
    raw = abs(a - b)
    adjustment = 0
    if raw > 10:
        adjustment = 5
    elif raw > 5:
        adjustment = 3
    else:
        adjustment = 1
    decoy_value = adjustment * 100  # Misleading intermediate
    return adjustment


def process_iteration(values):
    total = 0
    penalty = 0
    for v in values:
        if v < 0:
            penalty += 1
            continue
        total += v ** 0.5
    scaling = 2.5 if penalty == 0 else 1.8
    return total * scaling


def evaluate_performance(data_stream, threshold):
    base_metric = 0
    for item in data_stream:
        if item > threshold:
            base_metric += item // threshold
        else:
            base_metric += item % (threshold // 4 + 1)
    
    # Complex conditional expression with nested logic
    adjusted_metric = base_metric * (1.2 if base_metric > 15 else (0.85 if base_metric > 8 else 0.6))
    
    # Irrelevant secondary analysis (distractor)
    outlier_count = 0
    for item in data_stream:
        if item % 11 == 0 and item > 20:
            outlier_count += 1
    suppression_factor = 1.0
    if outlier_count > 2:
        suppression_factor = 0.9
    
    # Key recursive helper (simple recursion)
    def recursively_reduce(n, depth=0):
        if n <= 1 or depth >= 3:
            return n
        return recursively_reduce(n // 2, depth + 1)
    
    reduced_base = recursively_reduce(int(base_metric))
    
    # Combine multiple concepts: arithmetic, conditionals, recursion, comparisons
    auxiliary_score = analyze_metrics(len(data_stream), int(adjusted_metric))
    bias_correction = compute_bias_factor(reduced_base, len(data_stream))
    stream_analysis = process_iteration(data_stream)
    
    # Final computation with red herring variables
    initial_estimate = auxiliary_score + stream_analysis
    calibration_offset = outlier_count * 7  # Looks important but not used directly
    final_score = int(initial_estimate // bias_correction) + reduced_base
    
    # Decoy assignment that looks like it affects outcome
    if final_score % 2 == 0:
        final_score -= 3
    else:
        final_score += 2
    
    # Actual result printed
    return final_score

# Simulate execution
data_input = [12, 8, 15, 3, 22]
config_threshold = 10
final_score = evaluate_performance(data_input, config_threshold)
print(f"Result: {final_score}")