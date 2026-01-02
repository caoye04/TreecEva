def calculate_rating(values, limits):
    score = 0
    penalty = 0
    temp_result = []
    
    # Irrelevant pre-processing (distractor)
    scaling_factor = 1.0
    offset = 10
    dummy_accumulator = 0
    for i in range(len(values)):
        dummy_accumulator += values[i] * scaling_factor + offset

    # Actual logic begins: assess each value against threshold
    for idx, (val, lim) in enumerate(zip(values, limits)):
        if val > lim:
            score += 10
        elif val == lim:
            score += 5
        else:
            penalty += 2
    
    # Secondary adjustment with red herring computation
    multiplier = len(values) // 2
    fake_score = sum([x * multiplier for x in values])  # unused
    
    # Nested conditional that looks important but only triggers in edge cases (not met here)
    if all(v >= l for v, l in zip(values, limits)) and len(values) > 10:
        score *= 2
    elif any(v < 0 for v in values):
        score -= 10
    
    # Final scoring
    final_rating = score - penalty
    
    # More distraction: sorting unrelated data
    metadata_log = [(i, values[i]) for i in range(len(values))]
    metadata_log.sort(key=lambda x: x[1], reverse=True)
    rank_map = {item[0]: rank for rank, item in enumerate(metadata_log)}
    
    return final_rating

# Main execution
raw_inputs = [85, 92, 78, 96, 88, 73, 91, 84]
thresholds = [80, 90, 85, 95, 80, 75, 88, 82]

# Preprocessing chain with intermediate distractions
processed = [x - 5 for x in raw_inputs]
adjusted_values = []
for v in processed:
    if v < 70:
        adjusted_values.append(v + 3)
    elif v > 90:
        adjusted_values.append(v - 2)
    else:
        adjusted_values.append(v)

# Dummy state tracking (irrelevant)
count_high = 0
status_flags = []
for val in adjusted_values:
    if val > 85:
        count_high += 1
        status_flags.append(True)
    else:
        status_flags.append(False)

# Critical statement
final_score = calculate_rating(adjusted_values, thresholds)

# Output result
print(f"Result: {final_score}")