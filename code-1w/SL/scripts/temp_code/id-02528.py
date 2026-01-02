def calculate_final_score(data, thresholds):
    # Precompute some statistics (some are distractions)
    avg_val = sum(data) / len(data)
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val

    # Distractor: unused intermediate calculation
    normalized = [(x - min_val) / (max_val - min_val) for x in data]
    squared_errors = [((x - avg_val) ** 2) for x in data]
    variance = sum(squared_errors) / len(data)

    # Track valid segments using threshold logic
    valid_segments = []
    temp_segment = []

    for idx, value in enumerate(data):
        if value >= thresholds[0]:
            temp_segment.append(value)
        else:
            if len(temp_segment) >= thresholds[1]:
                valid_segments.append(temp_segment)
            temp_segment = []

    if len(temp_segment) >= thresholds[1]:
        valid_segments.append(temp_segment)

    # Use set operations to find unique high performers
    flattened = [item for segment in valid_segments for item in segment]
    high_performers = {x for x in flattened if x > thresholds[2]}

    # Another distractor: zipping unrelated sequences
    indices = list(range(len(flattened)))
    paired_data = list(zip(indices, flattened))
    sorted_pairs = sorted(paired_data, key=lambda x: x[1], reverse=True)
    top_three_vals = [pair[1] for pair in sorted_pairs[:3]]

    # Real computation path
    base_score = len(high_performers)
    bonus = sum(top_three_vals) // 10 if top_three_vals else 0
    penalty = len([x for x in data if x < thresholds[0] - 10])

    # Final score depends only on base_score, bonus, and penalty
    final_score = base_score + bonus - penalty

    return final_score

# Input data and parameters
data = [85, 90, 78, 92, 88, 45, 82, 96, 70, 85, 93, 87, 50, 88, 91]
thresholds = [80, 2, 85]  # min_value, min_segment_length, high_performer_threshold

# Execute function call
final_score = calculate_final_score(data, thresholds)
print(f"Target result: {final_score}")