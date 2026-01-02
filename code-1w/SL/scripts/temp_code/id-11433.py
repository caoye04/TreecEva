def process_metrics(entries):
    total = 0
    count = 0
    temp_buffer = []

    for entry in entries:
        if 'active' not in entry or not entry['active']:
            continue
        
        raw_value = entry.get('value', 0)
        offset = entry.get('offset', 0)
        adjusted = raw_value - offset
        
        # Irrelevant transformation (distractor)
        normalized = (adjusted / 100.0) * 1.5 if adjusted > 50 else adjusted / 75.0
        temp_buffer.append(normalized)
        
        multiplier = 1
        if adjusted > 30:
            multiplier += 0.2
        if adjusted < 0:
            multiplier -= 0.1
        
        scaled = adjusted * multiplier
        total += scaled
        count += 1

    avg = total / count if count > 0 else 0
    return avg


def calculate_final_score(data, weights):
    base_scores = []
    aux_tracker = []

    for i, segment in enumerate(data):
        slice_mid = len(segment) // 2
        left_part = segment[:slice_mid]
        right_part = segment[slice_mid:]
        
        # Real computation branch
        sum_left = sum(x ** 0.5 for x in left_part if x > 0)
        sum_right = sum(x % 7 for x in right_part)
        combined = sum_left + sum_right
        
        # Distractor: tracking unused intermediate
        aux_tracker.append(len(left_part) + len(right_part))
        
        weight_factor = weights[i] if i < len(weights) else 1.0
        weighted_score = combined * weight_factor
        base_scores.append(weighted_score)
    
    # Misleading dead-end calculation
    outlier_check = [s for s in base_scores if s > 100]
    correction = len(outlier_check) * 0.5
    
    final_sum = sum(base_scores)
    result = final_sum - correction  # Final meaningful computation
    
    # Additional red herring
    temp_result = result * 0.987
    dummy_flag = temp_result < 500
    
    return int(result)

# Main execution
raw_data = [
    [16, 25, 9, 4, 36, 49],
    [8, 27, 64, 125],
    [10, 20, 30, 40, 50]
]

weights_list = [1.2, 0.8, 1.5]

# Unused but plausible-looking preprocessing (distractor)
data_copy = [row[:] for row in raw_data]
sorted_slices = [sorted(row[1:-1]) for row in data_copy if len(row) > 2]

summary_stats = {
    'max_len': max(len(row) for row in raw_data),
    'total_elements': sum(len(row) for row in raw_data),
    'placeholder': None
}

interim_values = process_metrics([
    {'value': 45, 'offset': 10, 'active': True},
    {'value': 60, 'offset': 5, 'active': True},
    {'value': 30, 'offset': 0, 'active': False},  # filtered out
    {'value': 75, 'offset': 25, 'active': True}
])

result = calculate_final_score(raw_data, weights_list)
print(f"Target result: {result}")