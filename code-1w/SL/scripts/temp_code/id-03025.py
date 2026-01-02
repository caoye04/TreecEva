def calculate_final_score(data, thresholds):
    # Preprocessing: Normalize and filter data
    normalized = []
    temp_sum = 0
    outlier_count = 0  # Tracking outliers (distractor)

    for i, val in enumerate(data):
        if val < 0:
            temp_sum += abs(val)
            continue  # Skip negative values
        norm_val = val / (i + 1) if i % 2 == 0 else val * 0.9
        normalized.append(norm_val)

    # Secondary processing with zip and filtering
    processed = []
    debug_log = []  # Distractor: not used later
    for idx, (norm, th) in enumerate(zip(normalized, thresholds * len(normalized))):
        if idx >= len(thresholds):
            th = thresholds[idx % len(thresholds)]
        adjusted = norm - th
        if adjusted > 5:
            processed.append(adjusted * 0.8)
        elif adjusted > 0:
            processed.append(adjusted)
        else:
            processed.append(0)

    # State tracking with irrelevant counters
    total_positive = 0
    cumulative_shift = 0  # Unused accumulator
    peak_value = float('-inf')

    for j, p_val in enumerate(processed):
        if p_val > 0:
            total_positive += p_val
            if p_val > peak_value:
                peak_value = p_val
        cumulative_shift += j * 0.1  # Meaningless accumulation

    # Core logic: weighted contribution from high-impact elements
    high_impact_contrib = 0
    weights = [1.1, 1.3, 1.05]
    weight_index = 0

    for k, proc in enumerate(processed):
        if proc > 3:
            high_impact_contrib += proc * weights[weight_index % len(weights)]
            weight_index += 1

    # Final scoring with red herring computation
    fake_penalty = len(debug_log) * 10  # Always zero
    base_score = total_positive * 1.5
    bonus = high_impact_contrib * 0.4
    final_score = int(base_score + bonus - fake_penalty)

    return final_score

# Input data
raw_data = [12, -5, 18, 4, 21, 7, 0, 9]
data = [x for x in raw_data if x != 0]  # Remove zeros
thresholds = [2, 4, 3]

# Execution point of interest
final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")