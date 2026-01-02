def analyze_data(samples):
    raw_stats = []
    temp_sum = 0
    
    for sample in samples:
        if sample % 3 == 0:
            temp_sum += sample * 2
        elif sample % 5 == 0:
            temp_sum += sample // 2
    
    raw_stats.append(temp_sum)
    return raw_stats[0] if raw_stats else 0

# Irrelevant preprocessing step
preliminary_filter = lambda x: [i for i in x if i > 0]
sample_data = [-5, -2, 0, 3, 5, 9, 10, 12, 15]
cleaned_data = preliminary_filter(sample_data)

# Distraction: unused statistical computation
mean_val = sum(cleaned_data) / len(cleaned_data) if cleaned_data else 0
variance_proxy = sum((x - mean_val) ** 2 for x in cleaned_data) / len(cleaned_data) if cleaned_data else 0

# Core logic begins
base_metrics = {x for x in cleaned_data if x % 2 == 1}  # odd values
auxiliary_metrics = {x for x in cleaned_data if x % 2 == 0}  # even values

# Misleading metric combination
combined_metrics = base_metrics.union(auxiliary_metrics)
disregarded_overlap = base_metrics.intersection(auxiliary_metrics)  # empty, but included for distraction

metric_set = sorted(list(combined_metrics))

# Secondary distraction: simulate historical comparison
historical_reference = {1, 3, 5, 7, 9}
conceptual_similarity = len(historical_reference.intersection(base_metrics))

scaling_factor = 1.5 if conceptual_similarity > 2 else 1.0

# Actual evaluation function
weight_map = {}
for val in metric_set:
    if val in base_metrics:
        weight_map[val] = 2
    else:
        weight_map[val] = 1

weighted_total = 0
for k, v in weight_map.items():
    weighted_total += k * v

size_correction = len(metric_set) - len(disregarded_overlap)
corrected_score = weighted_total / size_correction if size_correction else 0

# Final transformation with logical conditions
if corrected_score > 10:
    final_score = int(corrected_score * scaling_factor)
elif corrected_score > 5:
    final_score = int(corrected_score + 3)
else:
    final_score = int(corrected_score)

Result: final_score