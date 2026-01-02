def evaluate_performance(metrics, base):
    adjustment = 0
    temp_values = []
    threshold = sum(base) / len(base)
    
    for val in metrics:
        if val > threshold:
            adjustment += val * 0.1
        temp_values.append(val ** 0.5)
    
    filtered = list(filter(lambda x: x > 5, metrics))
    dummy_sum = sum([x for x in temp_values if x < 4])
    
    aggregate = 0
    for i, v in enumerate(filtered):
        aggregate += v - base[i % len(base)]
    
    # Misleading intermediate calculation
    outlier_check = set(metrics) - set(base)
    spike_count = len([x for x in outlier_check if x > max(base)])
    
    if spike_count > 0:
        aggregate *= 1.1
    
    final_score = int(aggregate + adjustment)
    return final_score

# Baseline and input data
dataset_metrics = [12, 15, 9, 18, 21]
baseline_ref = [10, 14, 8, 12]

interim_result = [x // 2 for x in dataset_metrics]
dummy_str = "processing_complete"
status_flag = dummy_str.upper().replace("_", "-")

final_score = evaluate_performance(dataset_metrics, baseline_ref)
print(f"Result: {final_score}")