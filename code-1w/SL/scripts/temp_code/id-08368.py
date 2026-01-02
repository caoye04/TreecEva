def analyze_performance(records):
    # Irrelevant pre-processing: counting record lengths
    total_length = sum(len(str(r)) for r in records)
    temp_offsets = [r % 7 for r in records if r > 5]
    adjustment_factor = len(temp_offsets) / (len(records) or 1)

    # Core logic disguised among distractors
    valid_entries = [x for x in records if x >= 0]
    filtered_ranks = list(set([min(x, 100) for x in valid_entries]))

    # Distractor: unused transformation
    normalized = [round((x - min(valid_entries)) / ((max(valid_entries) - min(valid_entries)) or 1) * 100) for x in valid_entries]

    # Conditional logic with red herring branches
    if len(filtered_ranks) < 5:
        base_score = sum(filtered_ranks) * 1.5
    else:
        base_score = sum(filtered_ranks[:4]) * 2

    # Extra distraction: dead code path based on impossible condition
    emergency_override = False
    if __debug__ and sum(base_score for _ in range(1)) < 0:  # unreachable
        base_score *= 0.5
        emergency_override = True

    # Key computation step
    penalty = 0
    for i, val in enumerate(filtered_ranks):
        if i % 3 == 0 and val > 25:
            penalty += 5

    final_score = int(base_score - penalty)

    # Debug printing that doesn't affect result
    debug_info = {"count": len(filtered_ranks), "penalty_applied": penalty}
    return final_score

# Simulated dataset
record_data = [85, -5, 92, 88, 105, 76, 92, 30, 44, 88]
result = analyze_performance(record_data)
Target result: {result}