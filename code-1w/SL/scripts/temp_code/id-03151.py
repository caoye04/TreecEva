def analyze_trends(data, threshold=0.5):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    trend_ratio = len(above_threshold) / len(below_threshold) if below_threshold else float('inf')
    return trend_ratio

raw_metrics = [0.2, 0.7, 0.9, 0.3, 0.6, 0.8, 0.1]
adjusted_metrics = [round(x * 1.2, 2) for x in raw_metrics]

# Irrelevant transformation
shifted_data = [x - 0.1 for x in adjusted_metrics if x > 0.4]
duplicate_filter = set()
cleaned_shifted = []
for val in shifted_data:
    if val not in duplicate_filter:
        cleaned_shifted.append(val)
        duplicate_filter.add(val)

enum_indexed = list(enumerate(cleaned_shifted))
indexed_pairs = [(i, round(v, 2)) for i, v in enum_indexed]

# Simulate multiple metric evaluations
evaluation_map = {}
for i, val in indexed_pairs:
    if i % 2 == 0:
        evaluation_map[i] = val * 1.5
    else:
        evaluation_map[i] = val * 0.8

metric_set = set(evaluation_map.values())

# Auxiliary function with red herring logic
def compute_baseline(items):
    base = sum(items) / len(items)
    deviation = [abs(x - base) for x in items]
    return base + (sum(deviation) / len(deviation))

baseline_correction = compute_baseline(list(metric_set))

# Dummy case conversion for distraction
status_labels = ['HIGH', 'LOW', 'MEDIUM']
case_converted = [label.lower() for label in status_labels]
flag_map = dict(zip(status_labels, case_converted))

# Core logic disguised among distractions
size_factor = len(metric_set)
weight_sequence = [0.3, 0.5, 0.7, 0.9]
weighted_sum = sum(w * (i + 1) for i, w in enumerate(weight_sequence[:len(metric_set) % 4 + 1]))

scaling_factor = analyze_trends(raw_metrics, 0.4)

intermediate_result = baseline_correction * scaling_factor

# Actual performance evaluation
mask_values = [v for i, v in enumerate(metric_set) if i % 2 == len(metric_set) % 2]
masked_avg = sum(mask_values) / len(mask_values) if mask_values else 0

final_score = int(round(intermediate_result + masked_avg - weighted_sum))

Result: final_score