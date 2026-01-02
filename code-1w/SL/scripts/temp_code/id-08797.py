def evaluate_performance(records, importance):
    temp_result = 0
    base_adjustment = 0.0
    threshold_counter = 0
    cumulative = [0] * len(records)
    
    # Irrelevant string processing (distractor)
    status_labels = ['pass', 'fail', 'review']
    label_map = {label: idx for idx, label in enumerate(status_labels)}
    processed_flags = []
    
    for i, record in enumerate(records):
        # Real logic begins: check if record meets threshold
        if sum(record) / len(record) > 75:
            threshold_counter += 1

        # Destructuring assignment with distraction
        a, b, c = record[0], record[1], record[2]
        variation = abs(a - b) + (c >> 2)
        
        # Meaningless character counting (distractor)
        flag_str = f"Status_{i % 3}".lower().replace('_', '')
        char_count = len([ch for ch in flag_str if ch in 'aeiou'])
        processed_flags.append(char_count)
        
        # Actual contribution to result
        weighted_sum = sum(x * y for x, y in zip(record, importance))
        adjustment_factor = (lambda x: x ** 0.5 if x > 0 else 0)(weighted_sum // 10)
        cumulative[i] = weighted_sum + adjustment_factor
    
    # Sorting irrelevant data (distractor)
    sorted_flags = sorted(processed_flags, reverse=True)
    avg_flag = sum(sorted_flags) / len(sorted_flags) if sorted_flags else 0
    
    # Core logic dependency
    active_segments = [x for x in cumulative if x > 80]
    temp_result = sum(active_segments) // len(active_segments) if active_segments else 0
    
    # Final computation using dictionary lookup (semi-relevant)
    config = {'offset': 5, 'multiplier': 2}
    final_score = (temp_result + config['offset']) * config['multiplier']
    
    # Dead code path (distractor)
    if base_adjustment > 100:
        final_score *= 1.1
    
    return final_score

# Input data
data = [
    [80, 78, 85],
    [70, 90, 88],
    [60, 75, 70],
    [95, 85, 90]
]

weights = [0.4, 0.3, 0.3]

# Execute main logic
final_score = evaluate_performance(data, weights)
print(f"Result: {final_score}")