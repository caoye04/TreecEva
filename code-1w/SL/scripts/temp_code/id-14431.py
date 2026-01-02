def analyze_metrics(data_slice):
    # Irrelevant preprocessing step (distractor)
    temp_offset = sum(data_slice) // len(data_slice)
    adjusted_values = [x - temp_offset for x in data_slice]

    # Semi-relevant transformation
    normalized = [abs(x) ** 0.5 for x in adjusted_values if x != 0]

    # Dead computation path (not used later)
    outlier_count = 0
    for val in normalized:
        if val > 2.0:
            outlier_count += 1

    # Actual relevant calculation
    signal_strength = sum(normalized[:3])
    return signal_strength


def extract_features(raw_data):
    # Slice operations and dictionary use
    time_window = raw_data[2:7]
    feature_map = {
        'peak': max(time_window),
        'base': min(time_window),
        'span': len(time_window)
    }

    # Distractor: unused feature computation
    avg_val = sum(time_window) / len(time_window)
    feature_map['offset'] = avg_val - feature_map['base']

    # Return only one part of the map (others are distractions)
    return feature_map['peak'] - feature_map['base']


def calculate_performance(dataset):
    score = 0

    # Conditional branch based on length (actual logic trigger)
    if len(dataset) >= 5:
        segment_a = dataset[:4]
        segment_b = dataset[3:6]

        # Real metric contribution
        metric_x = analyze_metrics(segment_a)
        metric_y = extract_features(segment_b)

        # Dummy intermediate variables (distraction)
        dummy_weight = 0.85
        scaling_factor = 1.0 + (dummy_weight * 0.15)
        buffer_adjustment = (metric_x - metric_y) % 4

        # Core arithmetic combination
        score += int(metric_x * 2)
        score += int(metric_y ** 1.5)

        # Another red herring: conditional that never triggers due to data constraints
        if buffer_adjustment > 10:
            score -= 50  # unreachable with current data

    else:
        score = -1

    # Final adjustment using dictionary lookup (semi-relevant)
    penalty_table = {0: 5, 1: 3, 2: 2, 3: 0}
    extra_penalty = penalty_table.get(len(dataset) % 4, 1)
    score -= extra_penalty

    return score

# Main execution flow
raw_input_data = [4, 8, 6, 10, 12, 7, 3]
intermediate_shift = sum(x * 2 for x in raw_input_data if x < 6)  # irrelevant accumulation
baseline_reference = raw_input_data[1:5]  # distractor slice

# Key statement
final_score = calculate_performance(raw_input_data)
print(f"Result: {final_score}")