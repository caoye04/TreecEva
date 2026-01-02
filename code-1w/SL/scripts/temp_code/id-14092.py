def analyze_readings(sensor_readings):
    valid_readings = [x for x in sensor_readings if 10 <= x <= 100]
    outlier_count = len([x for x in sensor_readings if x < 10 or x > 100])
    average_reading = sum(valid_readings) / len(valid_readings) if valid_readings else 0
    adjusted_average = round(average_reading * 0.95, 2)
    return adjusted_average, outlier_count


def generate_flags(reading_value, threshold=50):
    # This function is not actually used; red herring
    flags = set()
    if reading_value < 20:
        flags.add('CRITICAL_LOW')
    elif reading_value > 80:
        flags.add('HIGH_LOAD')
    return flags

sensor_data = [15, 23, 55, 67, 88, 92, 105, 45, 33, 76, 81, 9, 101]
baseline_shift = 3.5
offset_tracker = []
for i in range(len(sensor_data)):
    offset_tracker.append(baseline_shift * (i % 4))

# Misleading transformation
transformed_data = tuple(abs(x - 50) for x in sensor_data)
duplicate_filter = set(transformed_data)
processed_data, _ = analyze_readings(sensor_data)

# Irrelevant accumulator
irrelevant_sum = 0
for val in transformed_data:
    if val > 30:
        irrelevant_sum += val * 0.1

# Key computation chain
interim_result = processed_data * 1.05
correction_factor = 0.98
if interim_result > 60:
    correction_factor = 0.92
adjusted_result = interim_result * correction_factor

scaling_set = {1, 2, 3, 4}
scaling_factor = len(scaling_set) * 0.25  # Always 1.0, but obscured

final_score = int(adjusted_result * scaling_factor + 0.5)
Result: final_score