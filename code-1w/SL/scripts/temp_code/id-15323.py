def preprocess_entries(raw_entries):
    normalized = {}
    temp_sum = 0
    scaling_factor = 1.5
    
    for key, value in raw_entries.items():
        if len(key) % 2 == 0:
            normalized[key.upper()] = value * scaling_factor
        else:
            normalized[key.lower()] = value + 2
        temp_sum += value

    adjustment = temp_sum / (len(normalized) + 1)
    return normalized, adjustment


def filter_outliers(data_dict, threshold=30):
    filtered = {}
    outlier_count = 0
    total_values = 0
    
    for k, v in data_dict.items():
        if isinstance(v, str):
            continue
        if v > threshold:
            filtered[k] = v
        else:
            outlier_count += 1
        total_values += 1
    
    stats = {
        'kept': len(filtered),
        'discarded': outlier_count,
        'total': total_values
    }
    return filtered, stats


def calculate_final_score(data):
    base_score = 0
    penalty = 0
    bonus_tracker = []
    
    for idx, (k, v) in enumerate(data.items()):
        if 'X' in k:
            base_score += v * 0.5
            bonus_tracker.append(idx)
        elif 'y' in k:
            base_score += v * 1.2
        else:
            base_score += v
        
        if idx % 3 == 0:
            penalty += 1.5
    
    final_bonus = len(bonus_tracker) * 2.5
    return int(base_score - penalty + final_bonus)

# Main execution
raw_data = {
    'alpha': 8,
    'betaX': 12,
    'gamma': 5,
    'deltaY': 10,
    'epsilonX': 14,
    'zeta': 6
}

processed_data, adjust_val = preprocess_entries(raw_data)
filtered_data, info = filter_outliers(processed_data, threshold=9)

intermediate_metric = sum(v for v in processed_data.values() if isinstance(v, (int, float)))
spurious_calc = adjust_val * 2.1

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")