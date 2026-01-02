def process_segments(data, importance):
    total = 0
    adjustments = []
    temp_offset = 0

    for i, (value, flag) in enumerate(data):
        if flag:
            scaled = value * importance[i]
            total += scaled
            adjustments.append(scaled * 0.1)
        else:
            temp_offset += value // 2

    correction_factor = sum(adjustments[:len(adjustments)])
    
    # Irrelevant computations to increase cognitive load
    dummy_list = [x ** 2 for x in range(len(importance))]
    unused_dict = {k: v for k, v in zip(dummy_list, importance)}
    redundant_calc = sum(unused_dict.values()) * 0.01

    # Simulate noise filtering
    filtered_noise = [x for x in adjustments if x > 0.5]
    noise_sum = sum(filtered_noise)

    # Final adjustment not affecting core logic
    if len(filtered_noise) > 3:
        total -= noise_sum * 0.2

    return int(total - correction_factor)

# Main execution
raw_values = [12, 18, 24, 30, 42]
activation_flags = [True, True, False, True, True]
segment_data = list(zip(raw_values, activation_flags))
weights = [1.0, 1.5, 0.8, 2.0, 1.2]

baseline_shift = 5
offset_tracker = []
for idx, val in enumerate(raw_values):
    offset_tracker.append(val % 3)

# Dead code path - never executed but looks relevant
if baseline_shift > 100:
    final_offset = sum(offset_tracker)
else:
    final_offset = 0  # Unused in final computation

final_score = process_segments(segment_data, weights)
print(f"Target result: {final_score}")