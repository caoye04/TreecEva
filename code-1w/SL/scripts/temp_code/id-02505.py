def process_signal(data_stream):
    base_offset = 17
    temp_buffer = []
    for val in data_stream:
        if val > 0:
            temp_buffer.append(abs(val) ** 0.5)
    avg_magnitude = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0

    # Irrelevant signal shaping (distractor)
    shaped = list(map(lambda x: x * 1.05 + 2, temp_buffer))
    smoothed = [shaped[i] for i in range(len(shaped)) if i % 2 == 0]

    return avg_magnitude


def calculate_efficiency(weight, shift):
    if shift <= 0:
        return 1.0
    result = 1.0
    for i in range(int(shift)):
        result *= (weight + i) / (shift - i + weight)
    return result

# Main execution
raw_input = [-4, 9, -16, 25, 36, -49, 64]

# Dead code path - never called (distractor)
if False:
    def legacy_mode(x):
        return x << 2

# Signal preprocessing
magnitude_avg = process_signal(raw_input)
logic_weight = len([x for x in raw_input if x > 0])
phase_shift = magnitude_avg // 2

# Complex but partially irrelevant string transformation chain
status_flag = "ACTIVE"
coded_status = status_flag.lower().replace('a', 'X').upper()  
encoded_length = len(coded_status)  # Unused downstream

# Set operations to compute auxiliary metric (semi-relevant)
data_points = set(raw_input)
outliers = {x for x in data_points if abs(x) > 50}
outlier_count = len(outliers)

# Correction factor influenced by outlier logic
if outlier_count > 2:
    correction_factor = 0.85
else:
    correction_factor = 1.15

# Key computational step
thermal_capacity = calculate_efficiency(logic_weight, phase_shift) * correction_factor

# Additional unused variables (distractors)
baseline = 100 * correction_factor
adjusted_baseline = baseline * (1 + phase_shift * 0.01)
diagnostic_log = f"Final state: {coded_status}"  # Not used

# Print final target result
print(f"Result: {thermal_capacity}")