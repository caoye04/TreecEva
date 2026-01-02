from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if (sequence[i] + sequence[j]) % 3 == 0:
                count += 1
    return count

def validate_entry(record):
    checksum = sum(v * k for k, v in record.items() if k % 2 == 1)
    adjustment = 0
    temp_var = 0
    for k in record:
        if record[k] > 5:
            adjustment += 2
        else:
            temp_var += k  # unused variable
    return checksum + adjustment

def generate_thresholds(baseline, levels=4):
    thresholds = {}
    for i in range(1, levels + 1):
        thresholds[f'level_{i}'] = baseline * (1.5 ** i)
    extra_calc = [baseline * x for x in range(3)]  # distractor
    return thresholds

def process_results(data, limits):
    intermediate = []
    total_weight = 0
    for key, value_list in data.items():
        avg_val = sum(value_list) / len(value_list)
        weight = 1
        if avg_val > limits['level_2']:
            weight += 1
        if avg_val > limits['level_3']:
            weight += 1
        intermediate.append(avg_val * weight)
    
    aggregate = sum(intermediate)
    penalty = 0
    for val in intermediate:
        if val < 10:
            penalty += 2.5
    adjusted_total = aggregate - penalty
    
    outlier_check = [x for x in intermediate if x > limits['level_4']]
    if len(outlier_check) >= 2:
        adjusted_total *= 1.1
    
    return int(adjusted_total)

# Main execution
config = {2: 8, 4: 6, 6: 9, 8: 5}
seq_data = [3, 6, 9, 12, 15]
calibration_factor = validate_entry(config)
signal_count = analyze_pattern(seq_data)

base_threshold = calibration_factor // 2 + (signal_count % 5)

threshold_config = generate_thresholds(base_threshold, levels=4)

results = {
    'experiment_A': [12, 15, 11, 14],
    'experiment_B': [8, 9, 10, 12],
    'experiment_C': [16, 14, 18, 15],
    'experiment_D': [7, 6, 8, 9]
}

final_score = process_results(results, threshold_config)

# Debug prints (not affecting logic)
dummy_stats = {k: sum(v)/len(v) for k, v in results.items()}
outlier_debug = list(combinations([1, 2, 3, 4], 2))

print(f"Result: {final_score}")