def analyze_efficiency(values):
    filtered = [v for v in values if v > 0]
    squared = list(map(lambda x: x ** 2, filtered))
    sum_sq = sum(squared)
    count_pos = len(filtered)
    avg_sq = sum_sq / count_pos if count_pos else 0
    return avg_sq

# Simulate system metrics with noise
temp_data = [3, -1, 4, 0, 2, 5, -2]
raw_metrics = {'throughput': 85, 'latency': 45, 'error_rate': 2.3}

# Irrelevant transformation (dead path)
dummy_set = {x % 3 for x in range(10)}
shadow_copy = temp_data[::-1]
offset = sum(dummy_set)  # Distractor computation

# Core logic disguised among side calculations
extended_data = temp_data + [x ^ 1 for x in temp_data[:3]]  # Bitwise XOR distraction
masked_data = [x for x in extended_data if x != 3]  # Remove specific value

# Compute derived metric using lambda and filtering
derived_metric = list(filter(lambda x: x % 2 == 0, masked_data))
bonus_points = len(derived_metric) * 1.5

# Weighted evaluation with red herring variables
weights = {'throughput': 0.5, 'latency': 0.3, 'error_rate': 0.2}
penalty_factor = 0.9  # Unused in final calculation but looks important
normalization_shift = 10  # Misleading adjustment not applied

# Actual performance model
metrics = {
    'throughput': raw_metrics['throughput'] + bonus_points,
    'latency': analyze_efficiency(temp_data),
    'error_rate': len([x for x in temp_data if x < 0])  # Count negatives as proxy
}

# Final scoring with correct weight application
final_score = 0
for key in metrics:
    if key in weights:
        final_score += metrics[key] * weights[key]

# Additional irrelevant operations to increase cognitive load
redundant_calc = (final_score ** 2) % 7
debug_info = {k: round(v, 2) for k, v in metrics.items()}

# Output target result
print(f"Result: {final_score}")