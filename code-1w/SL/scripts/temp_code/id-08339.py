def calculate_rating(entries, penalties):
    base_score = 0
    adjustment_factor = 0.85
    temp_offset = 0
    legacy_buffer = [0] * len(entries)

    # Irrelevant pre-scan: simulates data validation but unused
    for i, key in enumerate(entries):
        if key.startswith('temp'):
            temp_offset += 1
        legacy_buffer[i] = len(key) * 2  # Dead storage

    # Core scoring logic
    raw_values = []
    for k, v in entries.items():
        if v > 0 and not k.startswith('backup'):
            raw_values.append(v)

    sorted_vals = sorted(raw_values, reverse=True)
    top_contributions = sorted_vals[:3]  # Only top 3 count

    # Real computation begins
    for val in top_contributions:
        base_score += val ** 0.5  # Square root contribution

    # Apply conditional penalty from dictionary lookup
    total_penalty = 0
    for idx, val in enumerate(top_contributions):
        penalty_key = f"penalty_{idx + 1}"
        if penalty_key in penalties:
            total_penalty += penalties[penalty_key]

    # Distractor block: complex-looking but unused transformation
    shadow_score = 0
    for x in sorted_vals:
        for y in sorted_vals:
            if x != y:
                shadow_score += (x - y) / (abs(x - y) + 1e-9)

    # Final adjustment
    final_rating = base_score - total_penalty
    scaling_constant = 1.2
    final_rating *= scaling_constant

    # Critical assignment
    final_score = int(round(final_rating))

    return final_score

# Data setup
contribution_data = {
    "entry_a": 25,
    "entry_b": 16,
    "backup_temp_3": 9,
    "entry_c": 64,
    "temp_x": 4,
    "entry_d": 49
}

penalty_map = {
    "penalty_1": 3,
    "penalty_2": 2,
    "penalty_3": 1,
    "penalty_unused": 10
}

# Execution point of interest
final_score = calculate_rating(contribution_data, penalty_map)
print(f"Result: {final_score}")