def analyze_performance(metrics):
    # Irrelevant transformation
    temp_data = [x ** 0.5 for x in metrics if x > 10]
    adjusted = [x * 1.1 for x in metrics]
    
    # Distractor: complex but unused calculation
    outlier_count = sum(1 for x in adjusted if x > 50)
    penalty = 0
    if outlier_count > 3:
        penalty = outlier_count * 2

    # Relevant computation
    base_score = sum(x for x in adjusted if x < 60)
    return base_score

# Unused helper function (dead code path)
def validate_input(data):
    return all(isinstance(x, (int, float)) and x >= 0 for x in data)

# Lambda for conditional scaling
dynamic_scale = lambda x, factor: x * factor if x < 45 else x * (factor * 0.8)

# Simulated test results
test_results = [23, 45, 12, 67, 34, 55, 29, 41]

# Bonus logic with conditional expression
performance_flag = 'high' if sum(test_results) > 250 else 'low'
bonus_multiplier = 1.5 if performance_flag == 'high' else 1.1

# Apply dynamic scaling using lambda (some values affected)
scaled_results = [dynamic_scale(val, bonus_multiplier) for val in test_results]

# Additional distractor variables
average_raw = sum(test_results) / len(test_results)
variance_proxy = sum((x - average_raw) ** 2 for x in test_results)
theoretical_max = len(test_results) * 70
utilization_ratio = sum(test_results) / theoretical_max

# Core analysis pipeline
base_value = analyze_performance(scaled_results)

# Secondary adjustment chain
adjustment_factor = 0.95
if any(x > 60 for x in scaled_results):
    adjustment_factor += 0.05
    extra_adjust = sum(1 for x in scaled_results if x > 60) * 2
    base_value -= extra_adjust  # minor correction

# Final aggregation with tuple unpacking
intermediate = (base_value, utilization_ratio, penalty)
raw_score, _, _ = intermediate

# Final score calculation — this is the key statement
final_score = raw_score * adjustment_factor

Result: {final_score}