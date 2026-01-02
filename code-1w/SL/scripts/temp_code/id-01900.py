def evaluate_performance(records, offset):
    total = 0
    penalty = 0
    bonus_applied = False

    for i in range(len(records)):
        entry = records[i]
        if i % 2 == 0:
            total += (entry * offset) % 7
        else:
            total -= entry % 3

        # Distractor: tracking unused trend indicator
        trend_consistency = (entry + offset) & 15
        if trend_consistency > 10 and not bonus_applied:
            penalty += 2
            bonus_applied = True  # Misleading: never actually adds bonus

    return total - penalty


# Simulate sensor data processing with redundant transformations
data_stream = [18, 25, 34, 12, 41, 9, 55]
base_offset = 5

# Irrelevant preprocessing: normalization (not used in final logic)
normalized = [round((x - min(data_stream)) / (max(data_stream) - min(data_stream)) * 100) for x in data_stream]
activation_flags = [int(x > 20) for x in data_stream]

# Key slicing operation: using only middle portion
data_slice = data_stream[2:5]  # [34, 12, 41]

# Dead code path: unused helper
def calculate_urgency(weight, level):
    return (weight + level) ^ 3

# Secondary distractor variable (unused)
aggregated_risk = sum([x * 2 for x in activation_flags if x == 1])

# Core computation with interference
intermediate_shift = base_offset << 1
shift_reduction = (intermediate_shift & 7) if base_offset > 3 else 0
adjusted_offset = base_offset - shift_reduction  # 5 - 4 = 1

# Critical statement
final_score = evaluate_performance(data_slice, adjusted_offset)

print(f"Result: {final_score}")