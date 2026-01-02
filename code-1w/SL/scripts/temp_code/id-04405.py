def analyze_metrics(raw_values):
    normalized = [(x - min(raw_values)) / (max(raw_values) - min(raw_values)) for x in raw_values]
    squared_devs = [(x - sum(normalized)/len(normalized))**2 for x in normalized]
    variance = sum(squared_devs) / len(squared_devs)
    return variance


def preprocess_dataset(data_stream):
    filtered = [x for x in data_stream if x > 0]
    sorted_data = sorted(filtered, reverse=True)
    midpoint = len(sorted_data) // 2
    upper_half = sorted_data[:midpoint]
    lower_half = sorted_data[midpoint:]
    avg_upper = sum(upper_half) / len(upper_half) if upper_half else 0
    avg_lower = sum(lower_half) / len(lower_half) if lower_half else 0
    trend_estimate = avg_upper - avg_lower
    return trend_estimate

benchmark_data = [38, 12, 45, 7, 23, 56, 19, 31, 5, 67, 89, 14, 28]

# Distractor variables and computations
auxiliary_weights = [0.1, 0.3, 0.5, 0.7, 0.9]
dummy_aggregate = sum([w * idx for idx, w in enumerate(auxiliary_weights)])
shadow_copy = benchmark_data[::2]
phantom_sum = sum([x**2 for x in shadow_copy if x % 2 == 1])

intermediate_metric = analyze_metrics(benchmark_data)
trend_signal = preprocess_dataset(benchmark_data)

# Simulate calibration offset (not actually used in final result)
calibration_factor = 0.85
adjusted_trend = trend_signal * calibration_factor
normalization_shift = max(benchmark_data) / 100

# Core logic chain with list comprehension and comparisons
significance_flags = [1 if x >= 25 else 0 for x in benchmark_data]
activation_count = sum(significance_flags)
weight_vector = [x / sum(benchmark_data) for x in benchmark_data]
effective_weight = sum([w * f for w, f in zip(weight_vector, significance_flags)])

# Final performance calculation
base_score = activation_count * 100
dynamic_bonus = int(effective_weight * 500)
penalty_rate = 0.1 * intermediate_metric * 100

final_score = base_score + dynamic_bonus - int(penalty_rate)

# Irrelevant sorting operation (dead-end)
sorted_flags = sorted(significance_flags, key=lambda x: -x)
buffer_cache = [final_score + i for i in range(3)]

print(f"Result: {final_score}")