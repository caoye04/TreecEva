def analyze_metrics(data):
    # Irrelevant transformation
    temp_adjustment = sum(x ** 0.5 for x in data if x > 10)
    normalized = [x / (max(data) + 1e-5) for x in data]
    
    # Semi-relevant filtering
    filtered = [x for x in normalized if x > 0.2]
    base_metric = sum(filtered) * 0.8

    # Distractor: unused complex computation
    outlier_check = [x for x in data if x < 5]
    anomaly_score = len(outlier_check) * 0.3

    return base_metric


def calculate_stability(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    stability = 1 / (1 + sum(diffs))
    return stability

# Simulated benchmark dataset
dataset_raw = [12, 15, 9, 22, 8, 45, 16, 7]

# Misleading preprocessing chain
processed_batch = [x * 1.1 for x in dataset_raw]
adjusted_batch = [int(x) for x in processed_batch if x > 10]
scaled_values = [round(x, 2) for x in processed_batch]

# Auxiliary calculation with red herring variables
aggregate_total = sum(dataset_raw)
dummy_weight = 0.95
shadow_factor = aggregate_total % 7

# Core logic embedded within noise
benchmark_data = [x + 2 for x in dataset_raw if x % 2 == 0]
intermediate_metric = analyze_metrics(benchmark_data)
consistency = calculate_stability(benchmark_data)

# Multiple influencing factors, some irrelevant
weight_a = 0.6
weight_b = 0.4
noise_offset = len(adjusted_batch) - len(benchmark_data)  # unused

final_score = int((intermediate_metric * weight_a + consistency * weight_b * 100))

# Final output
print(f"Result: {final_score}")