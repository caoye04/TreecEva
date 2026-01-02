def calculate_final_score(raw_data, limits):
    # Preprocess: filter valid entries based on multiple criteria
    valid_entries = []
    temp_sum = 0
    outlier_count = 0  # distractor: not used in final logic

    for item in raw_data:
        if item < 0:
            continue  # skip negative values
        if item > limits['max']:
            outlier_count += 1
            continue
        if item < limits['min']:
            continue
        valid_entries.append(item)

    # Compute base metrics
    base_total = sum(valid_entries)
    entry_count = len(valid_entries)
    average_value = base_total / entry_count if entry_count > 0 else 0

    # Distractor block: irrelevant statistical computation
    squared_devs = [ (x - average_value) ** 2 for x in valid_entries ]
    variance_estimate = sum(squared_devs) / entry_count if entry_count > 0 else 0
    std_dev_hint = variance_estimate ** 0.5  # unused beyond this

    # Use set operations to detect unique magnitude groups
    magnitudes = {len(str(int(x))) for x in valid_entries}  # number of digits
    bonus_multiplier = 1
    if 3 in magnitudes:  # numbers like 100-999
        bonus_multiplier += 0.1
    if 4 in magnitudes:  # numbers like 1000-9999
        bonus_multiplier += 0.15

    # Apply conditional adjustments using boolean logic and comparisons
    adjustment_factor = 1.0
    if average_value > limits['target']:
        adjustment_factor *= 1.05
    elif average_value < limits['target'] * 0.9:
        adjustment_factor *= 0.95
    else:
        adjustment_factor *= 1.02

    # Simulate early termination under rare condition (not triggered here)
    if entry_count == 0:
        return 0

    # Core scoring formula
    preliminary_score = base_total * adjustment_factor * bonus_multiplier

    # Additional distraction: complex string-based tagging (unused)
    tags = []
    for v in valid_entries[:3]:  # only first three
        tag = "".join([chr(ord('A') + int(d) % 26) for d in str(int(v))])
        tags.append(tag)
    final_tag = "-".join(tags)  # completely irrelevant to score

    # Final non-linear transformation
    final_score = int(preliminary_score ** 0.5 * 10)

    return final_score

# Main execution
if __name__ == "__main__":
    data_set = [150, 200, 85, 1000, 420, 73, 999, 50]
    thresholds = {
        'min': 70,
        'max': 1050,
        'target': 300
    }
    
    # Intermediate variables with side distractions
    temp_analysis = [x for x in data_set if x % 2 == 0]  # even numbers only
    total_pairs = len(temp_analysis) // 2
    
    # Key execution point
    final_score = calculate_final_score(data_set, thresholds)
    print(f"Result: {final_score}")