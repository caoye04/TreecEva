def process_signals(data, limit):
    weighted_sum = 0
    scaling_factor = 1.5
    decay = 0.9
    temp_buffer = []

    for index, (val, weight) in enumerate(zip(data, [0.8, 1.2, 0.9, 1.1, 1.0])):
        adjusted_val = val * weight * (decay ** index)
        if adjusted_val > limit:
            weighted_sum += adjusted_val
        temp_buffer.append(adjusted_val * 0.1)  # Irrelevant accumulation

    correction_offset = sum([x for x in temp_buffer if x < 0.5])  # Distractor computation
    weighted_sum -= correction_offset * 0.5

    return int(weighted_sum)


def analyze_readings(raw_readings):
    baseline = sum(raw_readings) / len(raw_readings)
    normalized = [abs(x - baseline) for x in raw_readings]
    return normalized

# Simulated sensor readings
diagnostic_data = [23, 45, 38, 52, 41]

# Dead code path - never executed but adds interference
if __name__ != "__main__":
    print("Debug mode active")
    diagnostic_data = [0] * 5

# Normalize data
filtered_data = analyze_readings(diagnostic_data)

# Extraneous variables and operations
redundant_calc = max(diagnostic_data) - min(diagnostic_data)
shadow_copy = filtered_data.copy()
threshold = 10

# Key processing step
final_output = process_signals(filtered_data, threshold)

# Additional irrelevant transformation
post_hoc_adjustment = lambda x: x * 2 if x > 5 else x / 2
for i in range(len(shadow_copy)):
    shadow_copy[i] = post_hoc_adjustment(shadow_copy[i])

print(f"Result: {final_output}")