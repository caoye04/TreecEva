def analyze_performance(raw_data, threshold=10):
    count_valid = 0
    temp_sum = 0
    outlier_count = 0
    adjusted_values = []

    for val in raw_data:
        if val < 0:
            continue  # Ignore negative values
        if val > threshold * 2:
            outlier_count += 1
            corrected = threshold * 2
        else:
            corrected = val
        
        adjusted_values.append(corrected)
        temp_sum += corrected ** 0.5  # Track sqrt sum for diagnostics

    if len(adjusted_values) == 0:
        return 0

    base_score = sum(adjusted_values) / len(adjusted_values)

    # Diagnostic metric (not used in final score)
    stability_ratio = (max(adjusted_values) - min(adjusted_values)) / base_score if base_score else 0

    return base_score, len(adjusted_values)


def calculate_correction_factor(size, is_active=True):
    # Irrelevant helper that computes unused factor
    factor = 1.0
    for i in range(1, size + 1):
        if i % 3 == 0:
            factor *= 0.95
    return round(factor, 4) if is_active else 1.0

# Main execution
sensor_readings = [12, 15, 8, 3, 25, -4, 11, 21, 6]

# Preprocessing: filter and adjust readings
filtered_data = [x for x in sensor_readings if x > 5]

# Secondary analysis path (distractor)
diagnostic_stats = {}
diagnostic_stats['peak'] = max(sensor_readings)
diagnostic_stats['range'] = max(sensor_readings) - min(sensor_readings)
diagnostic_stats['count_below_threshold'] = len([x for x in sensor_readings if x <= 10])

# Compute auxiliary metrics (semi-relevant)
total_energy = sum(x * x for x in filtered_data)
energy_factor = total_energy // 100 if total_energy > 100 else 1

# Conditional expression used in meaningful context
size_category = 'large' if len(filtered_data) > 6 else 'medium' if len(filtered_data) > 3 else 'small'

# Core reasoning chain
base_value, valid_count = analyze_performance(filtered_data, threshold=12)

# Simulate environmental compensation (distraction with conditional expression)
environment_mode = 'high_interf' if energy_factor > 2 else 'normal'
compensation_delta = 0.5 if environment_mode == 'high_interf' else 0.1

# Accumulation with irrelevant adjustment
accumulator = 0
for i in range(valid_count):
    if i % 2 == 0:
        accumulator += base_value * 0.1
    else:
        accumulator -= base_value * 0.05

# Final score computation — key logic step
penalty_rate = 0.2 if outlier_detected := any(x > 20 for x in sensor_readings) else 0.0
adjusted_base = base_value - (penalty_rate * base_value)
correction_factor = calculate_correction_factor(len(filtered_data))  # Computed but not used

scaling_tuple = (1.5, 2.0, 0.8)
scaling_multiplier = scaling_tuple[valid_count % 3]

final_score = int(adjusted_base * scaling_multiplier + accumulator) + energy_factor

# Distractor: unused debug print
# print(f'Debug: {outlier_detected=}, {correction_factor=}, {stability_ratio=}')

print(f"Target result: {final_score}")