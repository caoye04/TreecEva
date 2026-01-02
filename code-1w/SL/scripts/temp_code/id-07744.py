def process_metrics(entries, importance):
    base_score = 0
    adjustment_factor = 0.0
    temp_values = []
    cumulative = [0] * len(entries)

    # Irrelevant pre-processing: tracks unused stats
    stats_summary = {"valid": 0, "ignored": 0}
    for i, entry in enumerate(entries):
        if entry["value"] < 0:
            stats_summary["ignored"] += 1
            continue
        stats_summary["valid"] += 1

    # Real processing with distractors
    multiplier = 1
    debug_trace = []  # Unused debugging aid

    for i, entry in enumerate(entries):
        raw_value = entry["value"]
        weight = importance.get(entry["type"], 1)

        # Bitwise obfuscation (only one bit matters)
        masked = raw_value ^ 15
        if masked & 8:  # Only check bit 3
            multiplier = 2

        # Apply weighted contribution
        contribution = raw_value * weight * multiplier
        temp_values.append(contribution)

        # Cumulative array updated but only last used
        cumulative[i] = sum(temp_values) if i == 0 else cumulative[i-1] + contribution

        # Red herring: complex lambda that's never called
        analyze = lambda x: x ** 2 - x * 0.5

    # Final aggregation using list comprehension and dictionary filtering
    filtered = [v for v in temp_values if v > 5]
    scaling_map = {i: 1.1 if i % 2 == 0 else 0.9 for i in range(len(filtered))}
    scaled = sum(v * scaling_map[i] for i, v in enumerate(filtered))

    # Actual answer computation buried in logic
    adjustment_factor = sum(1 for v in entries if v["value"] % 2 == 0)
    base_score = int(scaled // 1)  # Floor to int

    final_score = base_score + adjustment_factor

    # Dead code: misleading alternate path
    if False:
        final_score *= 1.5

    return final_score

# Input data
input_entries = [
    {"type": "alpha", "value": 7},
    {"type": "beta", "value": 4},
    {"type": "gamma", "value": 9},
    {"type": "alpha", "value": 12}
]
weights = {"alpha": 1.5, "beta": 2.0}

# Execution point
final_score = process_metrics(input_entries, weights)
print(f"Result: {final_score}")