def calculate_final_score(records, limits):
    # Irrelevant pre-processing: normalize unrelated fields
    normalized_ids = [r[0] % 17 for r in records if r[0] > 0]
    temp_weights = [abs(w - 5.0) for w in limits]

    # Relevant data extraction and slicing
    values = [r[2] for r in records]
    data_slice = values[1:-1]  # Exclude first and last

    # Misleading statistical distraction
    mean_val = sum(values) / len(values)
    stdev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    filtered_outliers = [v for v in values if abs(v - mean_val) <= 2 * stdev]

    # Threshold filtering using dictionary mapping
    category_map = {0: 'low', 1: 'med', 2: 'high'}
    category_count = {'low': 0, 'med': 0, 'high': 0}

    for val in data_slice:
        cat_key = int(val // 10) % 3
        cat_name = category_map.get(cat_key, 'unknown')
        if cat_name in category_count:
            category_count[cat_name] += 1

    # Secondary logic: apply thresholds with conditional overrides
    adjusted_counts = []
    for i, thresh in enumerate(limits):
        effect = category_count[category_map[i]] * (i + 1)
        if effect > thresh:
            adjusted_counts.append(effect // 2)
        else:
            adjusted_counts.append(effect + 1)

    # Final computation chain
    raw_score = sum(adjusted_counts)
    penalty = len([v for v in data_slice if v < 5]) * 3
    bonus = len(normalized_ids) % 4  # Red herring: derived from irrelevant ID processing

    intermediate = raw_score - penalty
    final_score = intermediate + bonus

    return final_score

# Main execution context
user_data = [
    (101, 'A', 12),
    (102, 'B', 8),
    (103, 'C', 23),
    (104, 'D', 6),
    (105, 'E', 19),
    (106, 'F', 4),
    (107, 'G', 11)
]
thresholds = [5, 7, 10]
data_slice = []

# Call function to compute result
def main():
    global final_score
    final_score = calculate_final_score(user_data, thresholds)
    print(f"Target result: {final_score}")

main()