def analyze_metrics(data, threshold=0.75):
    high_performers = []
    temp_buffer = []
    cumulative_sum = 0
    for i, (name, metrics) in enumerate(zip(['alpha', 'beta', 'gamma'], data)):
        avg_metric = sum(metrics) / len(metrics)
        if avg_metric > threshold:
            high_performers.append((i, avg_metric))
        temp_buffer.append(avg_metric * 0.1)  # Distractor: not used later
        cumulative_sum += avg_metric
    
    adjustment_factor = 1.0
    if len(high_performers) > 1:
        adjustment_factor = 1.2
    
    return cumulative_sum, adjustment_factor


def normalize_values(raw_data):
    flat = []
    for row in raw_data:
        for val in row:
            flat.append(val / 2.0 if val > 0 else 0)  # Semi-relevant transformation
    return flat

benchmark_data = [
    [0.85, 0.90, 0.88],
    [0.60, 0.65, 0.70],
    [0.92, 0.89, 0.94]
]

# Irrelevant pre-processing
shadow_copy = [[round(x, 2) for x in seq] for seq in benchmark_data]
dummy_stats = {k: v for k, v in enumerate([sum(seq) for seq in benchmark_data])}

# Key analysis step
raw_total, factor = analyze_metrics(benchmark_data)

# Normalize but only use length
normalized = normalize_values(benchmark_data)
scale_hint = len(normalized)  # Used to influence scaling

# Secondary distractor variables
baseline = 100
weight_map = {'low': 0.5, 'mid': 0.8, 'high': 1.3}
penalty = 0  # Never updated, red herring

# Core logic with conditional expression and dictionary lookup
level = 'high' if factor > 1.1 else 'mid'
scaling = weight_map[level]

# Final computation incorporating multiple concepts
intermediate = raw_total * scaling
final_score = int(intermediate + 0.5)  # Simulate rounding

Result: final_score