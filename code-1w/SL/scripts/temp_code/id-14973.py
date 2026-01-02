def analyze_metrics(raw_values, threshold=50):
    # Irrelevant transformation (dead-end computation)
    shadow_copy = [x * 1.5 for x in raw_values if x < 70]
    processed = [x for x in raw_values if x >= threshold]
    
    # Semi-relevant filtering
    filtered_set = set(processed)
    outlier_count = 0
    for val in raw_values:
        if val > 90:
            outlier_count += 1

    # Distractor: complex but unused structure
    stats_summary = {
        'max': max(processed),
        'min': min(processed),
        'count': len(processed),
        'outliers': outlier_count
    }

    adjusted_vals = [x - 5 for x in processed]
    return adjusted_vals


def generate_baseline(ref_list):
    # Bitwise manipulation as red herring
    encoded = []
    for i, val in enumerate(ref_list):
        encoded.append(val ^ i)  # XOR with index - not used later
    
    # Real work: create shifted baseline
    shift_val = sum(ref_list) // len(ref_list)
    return [x + shift_val for x in ref_list[:3]]


def evaluate_performance(metrics, base):
    # Use slicing and set operations (required)
    segment_a = metrics[1:-1]  # slice out first and last
    unique_metrics = set(segment_a)
    
    # Additional irrelevant computation
    temp_sum = 0
    for m in metrics:
        temp_sum += m % 7
    
    # Core logic hidden among distractions
    adjustment = 0
    for b in base:
        if b in unique_metrics:
            adjustment += b // 4
        else:
            adjustment -= b % 3
    
    core_total = sum(unique_metrics)
    final_value = core_total - adjustment
    
    # This print is required to expose result
    return final_value

# Main execution flow
raw_input_data = [45, 62, 88, 41, 73, 95, 54]
metric_set = analyze_metrics(raw_input_data, threshold=40)
baseline_data = generate_baseline([12, 18, 24])

# Key assignment point
final_score = evaluate_performance(metric_set, baseline_data)
print(f"Result: {final_score}")